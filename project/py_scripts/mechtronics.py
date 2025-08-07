import time
from machine import Pin, PWM
from servo import Servo

servo_pwmL = PWM(Pin(16))
servo_pwmR = PWM(Pin(15))

my_servo = Servo(pwm=servo_pwmL)
my_servo2 = Servo(pwm=servo_pwmR)