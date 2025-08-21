import time
from machine import Pin, PWM
from servo import Servo
from mechtronics import MechMovement
from UltrasonicSensor import UltrasonicSensors

Sensor = UltrasonicSensors()
Movement = MechMovement()

def Tesla():
    print("Starting top of the line navigation")
    while True:
        Turn_Left = Sensor.Front()
        Turn_Right = Sensor.Left()
        
        left_dist, front_dist = Sensor.get_distances()
        print(f"Left: {left_dist}mm, Front: {front_dist}mm")
        
        if Turn_Left and not Turn_Right:
            print("Turning Left")
            Movement.turn_left()
            time.sleep(0.9)
            
        elif Turn_Left and Turn_Right:
            print("Turning Right")
            Movement.turn_right()
            time.sleep(0.9)
            
        elif not Turn_Left:
            print("Move Forward")
            Movement.move_forward()
            time.sleep(0.5)
            
        else:
            print("180 degrees")
            Movement.turn_right()
            time.sleep(0.9)
            Movement.turn_right
            time.sleep(0.9)
        
        time.sleep(0.2)

if __name__ == "__main__":
    print("Start!")
    Tesla()