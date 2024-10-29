# Core class
import pymunk

class Core:
    def __init__(self, fission_speed = 2, thermal_speed = 1, cold_speed = 0.5):
        self.fast_speed = fission_speed
        self.thermal_speed = thermal_speed
        self.cold_speed = cold_speed
        self.space = pymunk.Space()

    def add_to_core(self, obj):
        self.space.add(obj)

    # Getters and setters
    def get_space(self):
        return self.space

    def get_fast_speed(self):
        return self.fast_speed

    def get_thermal_speed(self):
        return self.thermal_speed

    def get_cold_speed(self):
        return self.cold_speed

    def set_fast_speed(self, speed):
        self.fast_speed = speed

    def set_thermal_speed(self, speed):
        self.thermal_speed = speed

    def set_cold_speed(self, speed):
        self.cold_speed = speed