import time
from machine import Pin, PWM
from servo import Servo
from machine import RTC


class Controller:
    def __init__(self)
    servo_pwmL = PWM(Pin(16))
    servo_pwmR = PWM(Pin(15))

    freq = 50
    min_us = 500
    max_us = 2500
    dead_zone_us = 1500

    my_servo = Servo(
    pwm=servo_pwmL, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
    )
    my_servo2 = Servo(
    pwm=servo_pwmR, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
    )