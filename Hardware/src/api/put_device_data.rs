
use serde::{Serialize};

pub const API_PUT_DEVICE_DATA_ENDPOINT: &str = "/v1/iot/putDeviceData";

#[derive(Serialize)]
pub struct PutDeviceData {
    #[serde(rename = "inTemp")]
    pub in_temp: Option<f32>,
    #[serde(rename = "outTemp")]
    pub out_temp: Option<f32>,
    #[serde(rename = "LPOTime")]
    pub lpo_time: Option<f32>,
    #[serde(rename = "CO2")]
    pub co2: Option<f32>
}