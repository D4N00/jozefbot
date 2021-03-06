from machine import PWM, Pin
import utime

class Motor:

    def __init__(self, pin_forward, pin_backward):
        self.forward_pin = PWM(Pin(pin_forward))

        self.backward_pin = PWM(Pin(pin_backward))
        pass

    #can input speed in percents from -100 to 100 or input_tipe=1 then in u16 from -65000 to 65000
    def motor_movement(self, speed, input_tipe=0):
        if input_tipe == 0:
            if speed == 0:
                self.motor_forward(0)
                self.motor_backward(0)    
            elif speed > 100 or speed < -100:
                raise ValueError("Input speed out of range (must be between -100 and 100)")
            elif speed >= 0:
                duty_cycle = 40000 + speed*250
                self.motor_backward(0)
                self.motor_forward(duty_cycle)
            elif speed < 0:
                duty_cycle = 40000 + abs(speed)*250
                self.motor_forward(0)
                self.motor_backward(duty_cycle)
        elif input_tipe == 1:
            if speed == 0:
                self.motor_forward(0)
                self.motor_backward(0)
            elif speed > 65000 or speed < -65000:
                raise ValueError("Input speed out of range (must be between -65000 and 65000)")
            elif speed >= 0:
                duty_cycle = speed
                self.motor_backward(0)
                self.motor_forward(duty_cycle)
            elif speed < 0:
                duty_cycle = abs(speed)
                self.motor_forward(0)
                self.motor_backward(duty_cycle)

    def motor_forward(self, duty_cycle):
         self.forward_pin.duty_u16(duty_cycle)

    def motor_backward(self, duty_cycle):
        self.backward_pin.duty_u16(duty_cycle)

motor_left=Motor(18, 19)
motor_right=Motor(20, 21)


ir_output = []
ir_sensor_pinout = [Pin(13, Pin.IN), Pin(12, Pin.IN), Pin(11, Pin.IN), Pin(10, Pin.IN), Pin(9, Pin.IN)]

while True:
    ir_output = []
    for i in range(len(ir_sensor_pinout)):
        ir_output.append(ir_sensor_pinout[i].value())
    print(ir_output)
    if ir_sensor_pinout[1].value() == 0 and ir_sensor_pinout[2].value() == 0 and ir_sensor_pinout[3].value() == 0:
        motor_left.motor_movement(30000, 1)
        motor_right.motor_movement(30000, 1)
    else:
        if ir_sensor_pinout[1].value() == 1:
            motor_left.motor_movement(30000, 1)

        else:
            motor_left.motor_movement(0)
    
        if ir_sensor_pinout[3].value() == 1:
            motor_right.motor_movement(30000, 1)
        else:
            motor_right.motor_movement(0)
