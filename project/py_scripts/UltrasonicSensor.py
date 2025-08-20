from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

class UltrasonicSensors:
    def __init__(self):
        self.left_sensor = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
        self.front_sensor = PiicoDev_Ultrasonic(id=[0, 0, 1, 0])
    
    def get_distances(self):
        return self.left_sensor.distance_mm, self.front_sensor.distance_mm
    
    def print_distances(self):
        left_sensor, front_sensor = self.get_distances()
        print(left_sensor, front_sensor)
    
    def Sense_Range(self):
        while True:
            self.print_distances()
            sleep_ms(100)

    def Front(self):
        Min_disF = self.front_sensor.distance_mm
        if Min_disF < 50:
            return True

    def Left(self):
        Min_disL = self.left_sensor.distance_mm
        if Min_disL < 90:
            return True

if __name__ == "__main__":
    sensors = UltrasonicSensors()
    sensors.Sense_Range()
