# Core class
import pymunk

class Core:
    def __init__(self, fission_speed = (20, 0), thermal_speed = (1, 0), cold_speed = (0.5, 0), factor = 100):

        self.fast_speed = pymunk.Vec2d(fission_speed[0], fission_speed[1]) * factor

        self.thermal_speed = pymunk.Vec2d(thermal_speed[0], thermal_speed[1]) * factor

        self.cold_speed = pymunk.Vec2d(cold_speed[0], cold_speed[1]) * factor

        self.space = pymunk.Space()

    def add_to_core(self, neutron):
        try:
            self.space.add(neutron.get_body(), neutron.get_shape())
        except Exception as e:
            print(e)
        else:
            print("Object added to core successfully")

    def remove_from_core(self, neutron):
        try:
            self.space.remove(neutron.get_body(), neutron.get_shape())
        except Exception as e:
            print(e)
        else:
            print("Object removed from core successfully")

    # Getters and setters
    def get_space(self):
        return self.space
    def set_fast_speed(self, speed):
        self.fast_speed = speed

    def get_fast_speed(self):
        return self.fast_speed

    def get_thermal_speed(self):
        return self.thermal_speed

    def get_cold_speed(self):
        return self.cold_speed

    def set_thermal_speed(self, speed):
        self.thermal_speed = speed

    def set_cold_speed(self, speed):
        self.cold_speed = speed