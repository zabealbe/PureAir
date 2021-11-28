use esp_idf_sys::*;

pub struct Co2Sensor {
    channel: u32
}

impl Co2Sensor {
    pub fn new(adc1_channel: u32) -> Self {
        unsafe {
            adc1_config_width(adc_bits_width_t_ADC_WIDTH_BIT_12);
            adc1_config_channel_atten(adc1_channel, adc_atten_t_ADC_ATTEN_DB_11);
        }
        Self {
            channel: adc1_channel
        }
    }

    pub fn query_co2(&mut self) -> f32 {
        unsafe {
            adc1_get_raw(self.channel) as f32 / 4096.0
        }
    }
}