import random
from .Material import MaterialType as Material
from .FuelElement import FuelElement
from .helper import get_probability

# Fuel rod class
class Fuel:
    def __init__(self, uranium_occurance_probability, xenon_occurance_probability, xenon_decay_probability, element_radius, width, position, fuel_element_gap = 5):
        # Probability of uranium and xenon occurance and decay
        self.uranium_occurance_probability = uranium_occurance_probability
        self.xenon_occurance_probability = xenon_occurance_probability
        self.xenon_decay_probability = xenon_decay_probability

        # Length and width of the fuel rod
        self.length = 2*element_radius
        self.width = width
        self.radius = element_radius
        self.position = position

        # gap between fuel elements
        self.fuel_element_gap = fuel_element_gap

        # list of fuel elements in the fuel rod
        self.fuel_elements = []

        # Position of the fuel rod
        for i in range(0, self.width, self.length + self.fuel_element_gap):
            if get_probability() < self.uranium_occurance_probability:
                fuel_element = FuelElement(self.radius, self.uranium_occurance_probability, self.xenon_occurance_probability, self.xenon_decay_probability, material=Material.FISSILE)
                fuel_element.body.position = (self.position[0], self.position[1] + i)
                self.fuel_elements.append(fuel_element)
            else:
                fuel_element = FuelElement(self.radius, self.uranium_occurance_probability, self.xenon_occurance_probability, self.xenon_decay_probability, material=Material.NON_FISSILE)
                fuel_element.body.position = (self.position[0], self.position[1] + i)
                self.fuel_elements.append(fuel_element)

    # get the fuel elements list
    def get_fuel_elements(self):
        return self.fuel_elements