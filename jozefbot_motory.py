from machine import Pin
import utime
import time

led = Pin(25, Pin.OUT)

echoL = Pin(15, Pin.IN)
triggerL = Pin(14, Pin.OUT)
echoM = Pin(5, Pin.IN)
triggerM = Pin(4, Pin.OUT)
echoR = Pin(3, Pin.IN)
triggerR = Pin(2, Pin.OUT)

ir1 = Pin(13, Pin.IN)
ir2 = Pin(12, Pin.IN)
ir3 = Pin(11, Pin.IN)
ir4 = Pin(10, Pin.IN)
ir5 = Pin(9, Pin.IN)

motorLB = Pin(18, Pin.OUT)
motorLF = Pin(19, Pin.OUT)
motorRB = Pin(20, Pin.OUT)
motorRF = Pin(21, Pin.OUT)

def ultra():
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
   print("The distance from object is ",distance,"cm")
   
#while True:
   #ultra()
  # utime.sleep(1)
   

while True:
    
    #print(str(ir1.value()) + str(ir2.value()) + str(ir3.value()) + str(ir4.value()) + str(ir5.value()) )
    #utime.sleep_ms(10)
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
    
    
    
