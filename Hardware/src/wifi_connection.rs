use esp_idf_svc::wifi::EspWifi;
use std::sync::Arc;
use esp_idf_svc::netif::EspNetifStack;
use esp_idf_svc::sysloop::EspSysLoopStack;
use esp_idf_svc::nvs::EspDefaultNvs;
use embedded_svc::wifi::{AccessPointInfo, Configuration, ClientConfiguration, Wifi, AccessPointConfiguration, Status, ClientStatus, ClientConnectionStatus, ClientIpStatus, ApIpStatus, ApStatus};
use esp_idf_sys::EspError;

pub struct WifiConnection {
    wifi: Box<EspWifi>
}

impl WifiConnection {
    pub fn new() -> Self {
        let netif_stack = Arc::new(EspNetifStack::new().unwrap());
        let sys_loop_stack = Arc::new(EspSysLoopStack::new().unwrap());
        let default_nvs = Arc::new(EspDefaultNvs::new().unwrap());

        Self {
            wifi: Box::new(EspWifi::new(netif_stack, sys_loop_stack, default_nvs).unwrap())
        }
    }

    pub fn list_access_points(&mut self) -> Result<Vec<AccessPointInfo>, <EspWifi as Wifi>::Error> {
        self.wifi.scan()
    }

    pub fn connect_to_network(&mut self, ssid: String, pass: String) -> Result<(), <EspWifi as Wifi>::Error> {

        let access_points = self.list_access_points()?;

        let ours = access_points.into_iter().find(|a| a.ssid == ssid);

        let channel = if let Some(ours) = ours {
            println!(
                "Found configured access point {} on channel {}",
                ssid, ours.channel
            );
            Some(ours.channel)
        } else {
            println!(
                "Configured access point {} not found during scanning, will go with unknown channel",
                ssid
            );
            None
        };

        self.wifi.set_configuration(&Configuration::Mixed(
            ClientConfiguration {
                ssid: ssid.into(),
                password: pass.into(),
                channel,
                ..Default::default()
            },
            AccessPointConfiguration {
                ssid: "aptest".into(),
                channel: channel.unwrap_or(1),
                ..Default::default()
            },
        ))?;

        println!("Wifi configuration set, about to get status");

        let status = self.wifi.get_status();

        if let Status(
            ClientStatus::Started(ClientConnectionStatus::Connected(ClientIpStatus::Done(ip_settings))),
            ApStatus::Started(ApIpStatus::Done),
        ) = status
        {
            println!("Wifi connected");

            Ok(())
        } else {
            println!("Unexpected Wifi status: {:?}", status);
            Err(EspError::from(0x103).unwrap())
        }
    }
}