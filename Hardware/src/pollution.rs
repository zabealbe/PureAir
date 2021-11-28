use embedded_hal::digital::v2::{InputPin, OutputPin};
use esp_idf_sys::EspError;
use one_wire_bus::OneWire;
use esp_idf_hal::delay;
use embedded_hal::blocking::delay::DelayUs;

pub struct PollutionSensor<P> where P: InputPin<Error=EspError> {
    pin: P,
}

impl<P> PollutionSensor<P> where P: InputPin<Error=EspError> {
    pub fn new(pin: P) -> Self {
        Self {
            pin
        }
    }

    pub fn query_pollution(&self) -> f32 {
        let mut low_count = 0;

        const SAMPLES_COUNT: u32 = 10000;

        for _ in 0..SAMPLES_COUNT {
            if self.pin.is_low().unwrap_or(false) {
                low_count += 1;
            }
            delay::Ets.delay_us(100u32);
        }

        low_count as f32 / SAMPLES_COUNT as f32
    }
}