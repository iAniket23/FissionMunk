import pymunk
import random
from .Material import MaterialType as Material

class Fuel:
    def __init__(self, occurence_probability, fuel_element_gap, water_bool, length, width, position):
        self.occurence_probability = occurence_probability
        self.length = length
        self.width = width
        self.water_bool = water_bool
        self.position = position
        self.fuel_element_gap = fuel_element_gap
        self.fuel_elements = []

        for i in range(0, self.width, 10 + self.fuel_element_gap):
            if random.random() < self.occurence_probability:
                fuel_element = FuelElement(material=Material.FISSILE)
                self.fuel_elements.append(fuel_element)
            else:
                fuel_element = FuelElement(material=Material.NON_FISSILE)
                self.fuel_elements.append(fuel_element)

class FuelElement:
    def __init__(self, material = Material.FISSILE):
        self.material = material
        if self.water_bool:
            self.body, self.shape = self.create_water()
        self.body, self.shape = self.create_non_uranium_fuel_element() if self.material == Material.FISSILE else self.create_uranium_fuel_element()

    def create_uranium_fuel_element(self):
        fuel_body = pymunk.Body(0.1, pymunk.moment_for_circle(0.1, 0, self.radius), body_type=pymunk.Body.DYNAMIC)
        pass

    def create_non_uranium_fuel_element(self):
        pass

    def create_water(self):
        pass