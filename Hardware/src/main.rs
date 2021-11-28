#![allow(unused_imports)]
#![allow(clippy::single_component_path_imports)]

mod temperature;
mod config;
mod pollution;
mod co2_sensor;
mod wifi_connection;
mod api;

use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::sync::{Condvar, Mutex};
use std::{cell::RefCell, env, sync::atomic::*, sync::Arc, thread, time::*};

use url;

use embedded_svc::eth;
use embedded_svc::eth::Eth;
use embedded_svc::httpd::registry::*;
use embedded_svc::httpd::*;
use embedded_svc::io;
use embedded_svc::ipv4;
use embedded_svc::ping::Ping;
use embedded_svc::utils::anyerror::*;
use embedded_svc::wifi::*;

use esp_idf_svc::eth::*;
use esp_idf_svc::httpd as idf;
use esp_idf_svc::httpd::ServerRegistry;
use esp_idf_svc::netif::*;
use esp_idf_svc::nvs::*;
use esp_idf_svc::ping;
use esp_idf_svc::sntp;
use esp_idf_svc::sysloop::*;
use esp_idf_svc::wifi::*;

use esp_idf_hal::delay;
use esp_idf_hal::gpio;
use esp_idf_hal::i2c;
use esp_idf_hal::prelude::*;
use esp_idf_hal::spi;
use esp_idf_hal::ulp;
use esp_idf_hal::gpio::ADCPin;
use esp_idf_sys::*;

use esp_idf_sys;
use esp_idf_sys::esp;

use display_interface_spi::SPIInterfaceNoCS;

use embedded_graphics::mono_font::{ascii::FONT_10X20, MonoTextStyle};
use embedded_graphics::pixelcolor::*;
use embedded_graphics::prelude::*;
use embedded_graphics::primitives::*;
use embedded_graphics::text::*;
use esp_idf_hal::gpio::Pull;

use one_wire_bus::{Address, SearchState, OneWireError};
use esp_idf_sys::EspError;
use crate::temperature::TemperatureBus;
use crate::pollution::PollutionSensor;
use crate::co2_sensor::Co2Sensor;
use crate::wifi_connection::WifiConnection;
use embedded_svc::http::{HttpMethod, HttpSendHeaders};
use embedded_svc::http::{self, client::*, status, HttpHeaders, HttpStatus};
use esp_idf_svc::http::client::*;
use crate::api::put_device_data::{PutDeviceData, API_PUT_DEVICE_DATA_ENDPOINT};
use crate::api::update_device_position::{JsonAccessPointInfo, API_UPDATE_DEVICE_POSITION_ENDPOINT};
use esp_idf_hal::delay::portTICK_PERIOD_MS;
use crate::config::*;

fn main() -> Result<()> {
    esp_idf_sys::link_patches();

    let peripherals = Peripherals::take().unwrap();

    println!("Initializing led...");

    // Green pin
    let mut green_led_gpio = unsafe { GPIO_GREEN_LED::new() }.into_input_output().unwrap();
    green_led_gpio.set_high();

    println!("Initializing sensors...");

    let mut temp_bus_internal = {
        let mut pin = unsafe { GPIO_INTERNAL_TEMP_SENSOR::new() }.into_input_output_od().unwrap();
        pin.set_pull_up();
        TemperatureBus::new(pin).unwrap()
    };

    let mut temp_bus_external = {
        let mut pin = unsafe { GPIO_EXTERNAL_TEMP_SENSOR::new() }.into_input_output_od().unwrap();
        TemperatureBus::new(pin).unwrap()
    };

    let mut pollution_sensor = {
        let mut pin = unsafe { GPIO_POLLUTION_SENSOR::new() }.into_input().unwrap();
        PollutionSensor::new(pin)
    };

    let mut co2_sensor = {
        assert_eq!(GPIO_CO2_SENSOR::adc_unit(), 1);
        let channel = GPIO_CO2_SENSOR::adc_channel();
        Co2Sensor::new(channel)
    };

    let mut wifi_manager = WifiConnection::new();


    let access_points = wifi_manager.list_access_points().unwrap();
    wifi_manager.connect_to_network(env!("PUREAIR_WIFI_SSID").into(), env!("PUREAIR_WIFI_PASSWORD").into());

    let http_config = EspHttpClientConfiguration::default();
    let mut client = EspHttpClient::new(&http_config).unwrap();

    // Send wifi endpoints data to server on startup for geolocalization
    {
        let mut wifi_ap_request = client.post(PUREAIR_API_SERVER_ADDRESS.to_string() + API_UPDATE_DEVICE_POSITION_ENDPOINT + "/" + DEVICE_ID.to_string().as_str()).unwrap()
            .content_type("application/json");

        let data: Vec<JsonAccessPointInfo> = access_points.iter()
            .map(|x| JsonAccessPointInfo::from(x.clone())).collect();

        let request_data = serde_json::to_vec(&data).unwrap();
        wifi_ap_request.send_bytes(request_data.as_slice());
    }


    loop {

        let in_temp = if let Ok(temp) = temp_bus_internal.query_temperature() {
            println!("Internal temp: {} C", temp);
            Some(temp)
        } else { None };

        let out_temp = if let Ok(temp) = temp_bus_external.query_temperature() {
            println!("External temp: {} C", temp);
            Some(temp)
        } else { None };

        let mut lpo_time = Some(pollution_sensor.query_pollution());
        println!("Pollution: {:.2}%", lpo_time.unwrap() * 100.0);

        // Do not send pollution data if the external sensor is disconnected
        if out_temp.is_none() {
            lpo_time = None;
        }

        let co2 = co2_sensor.query_co2();
        println!("Air quality: {}", co2);

        // Compute the threshold to decide if the window should be opened

        let mut open_threshold = 0.0;
        if in_temp.is_some() && out_temp.is_some() {
            open_threshold += (in_temp.unwrap() - out_temp.unwrap()).abs() * K1;
        }

        open_threshold += lpo_time.unwrap() * K2;
        open_threshold += co2 * K3;

        // Turn on the green led if we are above the threshold
        if open_threshold > K4 {
            green_led_gpio.set_high();
        }
        else {
            green_led_gpio.set_low();
        }

        let sensors_data = PutDeviceData {
            in_temp,
            out_temp,
            lpo_time,
            co2: Some(co2),
        };

        // Send updated sensors data
        {
            let mut sensors_request = client.post(PUREAIR_API_SERVER_ADDRESS.to_string() + API_PUT_DEVICE_DATA_ENDPOINT + "/" + DEVICE_ID.to_string().as_str()).unwrap()
                .content_type("application/json");

            let request_data = serde_json::to_vec(&sensors_data).unwrap();
            sensors_request.send_bytes(request_data.as_slice());
        }

        println!("Data sent to server!");

        // Sleep to send updates to server every minute
        const SECONDS_BETWEEN_UPDATES: u32 = 60;
        unsafe {
            vTaskDelay(portTICK_PERIOD_MS * 1000 * SECONDS_BETWEEN_UPDATES);
        }
    }
}