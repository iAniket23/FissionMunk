# Core class
from .Neutron import Neutron
import pymunk

class Core:
    def __init__(self, fission_speed = (40, 0), thermal_speed = (10, 0), cold_speed = (5, 0), factor = 100):
        self.fast_speed = pymunk.Vec2d(fission_speed[0], fission_speed[1]) * factor
        self.thermal_speed = pymunk.Vec2d(thermal_speed[0], thermal_speed[1]) * factor
        self.cold_speed = pymunk.Vec2d(cold_speed[0], cold_speed[1]) * factor

        self.space = pymunk.Space()

        self.neutron_list = []
        self.moderator_list = []
        self.control_rod_list = []
        self.fuel_rod_list = []

    def add_neutron_to_core(self, neutron):
        try:
            self.space.add(neutron.get_body(), neutron.get_shape())
            self.neutron_list.append(neutron)
        except Exception as e:
            print(e)
        else:
            print("Object added to core successfully")

    def remove_neutron_from_core(self, neutron):
        try:
            self.space.remove(neutron.get_body(), neutron.get_shape())
            self.neutron_list.remove(neutron)
        except Exception as e:
            print(e)
        else:
            print("Object removed from core successfully")

    def add_moderator_to_core(self, moderator):
        try:
            self.space.add(moderator.get_body(), moderator.get_shape())
            self.moderator_list.append(moderator)
        except Exception as e:
            print(e)
        else:
            print("Object added to core successfully")

    def remove_moderator_from_core(self, moderator):
        try:
            self.space.remove(moderator.get_body(), moderator.get_shape())
            self.moderator_list.remove(moderator)
        except Exception as e:
            print(e)
        else:
            print("Object removed from core successfully")

    def add_control_rod_to_core(self, control_rod):
        try:
            self.space.add(control_rod.get_body(), control_rod.get_shape())
            self.control_rod_list.append(control_rod)
        except Exception as e:
            print(e)
        else:
            print("Object added to core successfully")

    def remove_control_rod_from_core(self, control_rod):
        try:
            self.space.remove(control_rod.get_body(), control_rod.get_shape())
            self.control_rod_list.remove(control_rod)
        except Exception as e:
            print(e)
        else:
            print("Object removed from core successfully")

    def add_fuel_rod_to_core(self, fuel_rod):
        try:
            for fuel_element in fuel_rod.get_fuel_elements():
                self.space.add(fuel_element.get_body(), fuel_element.get_shape())
                self.space.add(fuel_element.get_water_body(), fuel_element.get_water_shape())
                self.fuel_rod_list.append(fuel_rod)

        except Exception as e:
            print(e)
        else:
            print("Object added to core successfully")

    def remove_fuel_rod_from_core(self, fuel_rod):
        try:
            for fuel_element in fuel_rod.get_fuel_elements():
                self.space.remove(fuel_element.get_body(), fuel_element.get_shape())
                self.space.remove(fuel_element.get_water_body(), fuel_element.get_water_shape())
                self.fuel_rod_list.remove(fuel_rod)
        except Exception as e:
            print(e)
        else:
            print("Object removed from core successfully")

    # Getters and setters
    def get_neutron_list(self):
        return self.neutron_list

    def get_moderator_list(self):
        return self.moderator_list

    def get_control_rod_list(self):
        return self.control_rod_list

    def get_fuel_rod_list(self):
        return self.fuel_rod_list
    

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