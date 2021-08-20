from machine import Pin
import utime
import time

#Pinout setup
#on board led
led = Pin(25, Pin.OUT)

#ultrasonic pinout
echoL = 15
triggerL = 14
echoM = 5
triggerM = 4
echoR = 3
triggerR = 2

#line sensor pinout
#from left to right(forward orientation)
ir1 = Pin(13, Pin.IN)
ir2 = Pin(12, Pin.IN)
ir3 = Pin(11, Pin.IN)
ir4 = Pin(10, Pin.IN)
ir5 = Pin(9, Pin.IN)

#engine pinout high low
motorLB = Pin(18, Pin.OUT)
motorLF = Pin(19, Pin.OUT)
motorRB = Pin(20, Pin.OUT)
motorRF = Pin(21, Pin.OUT)

#ultrasound sensor distance measurment
def ultra(echo_input_pin, trigger_input_pin):
   echo = Pin(echo_input_pin, Pin.IN)
   trigger = Pin(trigger_input_pin, Pin.OUT)
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


while True:
   
    motorLF.high()
    motorRF.high()
    motorLB.low()
    motorRB.low()
    utime.sleep(0.5)

    motorLF.low()
    motorRF.low()
    motorLB.high()
    motorRB.high()
    utime.sleep(0.5)
    
    
    
