#![allow(non_camel_case_types)]

use esp_idf_hal::gpio::*;

/*
 * Device configuration parameters
*/

pub type GPIO_CO2_SENSOR = Gpio35<Unknown>;
pub type GPIO_POLLUTION_SENSOR = Gpio32<Unknown>;
pub type GPIO_INTERNAL_TEMP_SENSOR = Gpio18<Unknown>;
pub type GPIO_EXTERNAL_TEMP_SENSOR = Gpio19<Unknown>;
pub type GPIO_GREEN_LED = Gpio27<Unknown>;

// The address that is accessed to send the updated sensors data
pub const PUREAIR_API_SERVER_ADDRESS: &str = "http://pureair.zurini.dev";

// The unique id of this device
pub const DEVICE_ID: u32 = 1;
