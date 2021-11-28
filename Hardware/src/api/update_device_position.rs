
use serde::{Serialize};
use embedded_svc::wifi::AccessPointInfo;

pub const API_UPDATE_DEVICE_POSITION_ENDPOINT: &str = "/v1/iot/updateDevicePosition";

#[derive(Serialize)]
pub struct JsonAccessPointInfo {
    #[serde(rename = "macAddress")]
    pub mac_address: String,
    #[serde(rename = "strength")]
    pub signal_strength: u8,
    #[serde(rename = "SNR")]
    pub snr: u8,
    #[serde(rename = "channel")]
    pub channel: u8
}

impl From<AccessPointInfo> for JsonAccessPointInfo {
    fn from(info: AccessPointInfo) -> Self {
        Self {
            mac_address: format!("{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}",
                                 info.bssid[0],
                                 info.bssid[1],
                                 info.bssid[2],
                                 info.bssid[3],
                                 info.bssid[4],
                                 info.bssid[5],
            ),
            signal_strength: info.signal_strength,
            snr: 0,
            channel: info.channel
        }
    }
}