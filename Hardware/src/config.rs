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

// The weight of the temperature delta, should be negative
// to discourage opening the window in case of a big difference between indoor and outdoor temperature
pub const K1: f32 = -1.0;

// The weight of the outside pollution, negative because the greater the pollution level outside,
// the less we want to open the window
pub const K2: f32 = -10.0;

// The weight of the co2 concentration inside the house, if high the door should be opened
pub const K3: f32 = 3.0;

// The threshold for opening the window,
// the optimal level can be determined from samples collection during the day
pub const K4: f32 = 17.4;
