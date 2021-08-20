from machine import Pin
import utime

class Ultrasound:

    def __init__(self, echo_input_pin, trigger_input_pin):
        self.echo_input_pin = echo_input_pin
        self.trigger_input_pin = trigger_input_pin    

        #ultrasound sensor distance measurment
    def measure(self):
        
        echo = Pin(self.echo_input_pin, Pin.IN)
        trigger = Pin(self.trigger_input_pin, Pin.OUT)
        trigger.low()
        utime.sleep_us(2)
        trigger.high()
        utime.sleep_us(5)
        trigger.low()

        while echo.value() == 0:
            signaloff = utime.ticks_us()
        while echo.value() == 1:
            signalon = utime.ticks_us()
        
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
        return distance
