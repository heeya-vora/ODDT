from machine import Pin,PWM

import time


servo_motor = PWM(Pin(4)) #Servo Motor connected to Pin 15

servo_motor.freq(50)

while True :
    servo_motor.duty(30)
    print("Position 1")
    time.sleep(1)
    servo_motor.duty(77)
    print("Position 2")
    time.sleep(1)


# I have attached the Position table (Duty cycle, angle and corresponding valur for your reference
