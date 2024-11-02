import pymunk
import random
from .Material import MaterialType as Material

class Fuel:
    def __init__(self, occurence_probability, fuel_element_gap, length, width, position):
        self.occurence_probability = occurence_probability
        self.length = length
        self.width = width
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
        self.body, self.shape = self.create_non_uranium_fuel_element() if self.material == Material.FISSILE else self.create_uranium_fuel_element()

    def create_uranium_fuel_element(self):
        pass

    def create_non_uranium_fuel_element(self):
        pass


