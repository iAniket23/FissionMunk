import pymunk
import random
from .Material import MaterialType as Material

class Fuel:
    def __init__(self, occurence_probability, fuel_element_gap, length, width, position, water_bool = True):
        self.occurence_probability = occurence_probability
        self.length = length
        self.width = width
        self.water_bool = water_bool
        self.position = position
        self.fuel_element_gap = fuel_element_gap
        self.fuel_elements = []

        for i in range(0, self.width, self.length + self.fuel_element_gap):
            if random.random() < self.occurence_probability:
                fuel_element = FuelElement(length=self.length, occurance_probability=self.occurence_probability, water_bool=True,material=Material.FISSILE)
                fuel_element.body.position = (self.position[0], self.position[1] + i)
                fuel_element.water_body.position = (self.position[0], self.position[1] + i)
                self.fuel_elements.append(fuel_element)
            else:
                fuel_element = FuelElement(length=self.length,occurance_probability=self.occurence_probability, water_bool=True,material=Material.NON_FISSILE)
                fuel_element.body.position = (self.position[0], self.position[1] + i)
                fuel_element.water_body.position = (self.position[0], self.position[1] + i)
                self.fuel_elements.append(fuel_element)
    def get_fuel_elements(self):
        return self.fuel_elements

class FuelElement:
    body_to_fuel_element = {}
    def __init__(self, length, occurance_probability, water_bool = True, material = Material.FISSILE):
        self.occurence_probability = occurance_probability
        self.material = material
        self.length = length
        self.radius = (length // 2) - 4
        self.water_bool = water_bool

        # Adding water to the fuel element
        if self.water_bool:
            self.water_body, self.water_shape = self.create_water()

        self.body, self.shape = self.create_non_uranium_fuel_element() if self.material == Material.NON_FISSILE else self.create_uranium_fuel_element()

        if self.material == Material.FISSILE:
            self.shape.collision_type = 3
        elif self.material == Material.NON_FISSILE:
            self.shape.collision_type = 4

        FuelElement.body_to_fuel_element[(self.body, self.shape)] = self

    def create_uranium_fuel_element(self):
        fuel_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        fuel_shape = pymunk.Circle(fuel_body, self.radius)

        fuel_shape.sensor = True
        return fuel_body, fuel_shape

    def create_non_uranium_fuel_element(self):
        fuel_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        fuel_shape = pymunk.Circle(fuel_body, self.radius)
        fuel_shape.sensor = True
        return fuel_body, fuel_shape

    def create_water(self):
        water_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        water_shape = pymunk.Poly.create_box(water_body, (self.length, self.length))
        water_shape.sensor = True
        water_shape.collision_type = 6

        return water_body, water_shape

    def random_fissile_material(self):
        if self.material == Material.NON_FISSILE:
            if random.random() < 0.00001:
                self.set_material(Material.FISSILE)

    def get_body(self):
        return self.body

    def get_shape(self):
        return self.shape

    def get_water_body(self):
        return self.water_body

    def get_water_shape(self):
        return self.water_shape

    def get_material(self):
        return self.material

    def set_material(self, material):
        try:
            self.material = material
            self.shape.collision_type = 3 if self.material == Material.FISSILE else 4
        except Exception as e:
            print(e)

    def get_length(self):
        return self.length

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        try:
            self.radius = radius
        except Exception as e:
            print(e)