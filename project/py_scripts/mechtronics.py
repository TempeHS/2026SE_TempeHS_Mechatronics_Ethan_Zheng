import time
from machine import Pin, PWM
from servo import Servo

class MechMovement:
    def __init__(self):
        
        servo_pwmL = PWM(Pin(16))
        servo_pwmR = PWM(Pin(15)) 

        freq = 50          
        min_us = 500         
        max_us = 2500        
        dead_zone_us = 1500     
        
        self.left_motor = Servo(
            pwm=servo_pwmL,
            min_us=min_us,
            max_us=max_us, 
            dead_zone_us=dead_zone_us,
            freq=freq
        )
        
        self.right_motor = Servo(
            pwm=servo_pwmR,
            min_us=min_us,
            max_us=max_us,
            dead_zone_us=dead_zone_us, 
            freq=freq
        )
        
        # Starts
        self.stop()
        print("Ready!")
    
    def stop(self):
        self.left_motor.set_duty(1500)
        self.right_motor.set_duty(1500)
        print("Stops movement")
    
    def move_backward(self):
        self.left_motor.set_duty(500)  
        self.right_motor.set_duty(2500)  
        print("Reverse")
    
    def move_forward(self): 
        self.left_motor.set_duty(2500)
        self.right_motor.set_duty(500)
        print("Moving forward")
    

    def turn_right(self):
        self.left_motor.set_duty(1800)   
        self.right_motor.set_duty(1800)  
        print("Turning right")
    
    def turn_left(self):
        self.left_motor.set_duty(1200)  
        self.right_motor.set_duty(1200) 
        print("Turning left")

if __name__ == "__main__":
    robot = MechMovement()
    
    robot.move_backward()
    time.sleep(1)
    
    robot.turn_right()
    time.sleep(0.9)
    
    robot.move_forward() 
    time.sleep(1)

    robot.turn_left()
    time.sleep(0.9)
    
    robot.stop()
