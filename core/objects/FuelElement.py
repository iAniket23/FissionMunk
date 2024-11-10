from .Material import MaterialType as Material
from .helper import get_probability
import pymunk

# Fuel Element class
class FuelElement:
    body_to_fuel_element = {}
    def __init__(self, radius, uranium_occurance_probability, xenon_occurance_probability, xenon_decay_probability, material = Material.FISSILE):
        # Probability
        self.uranium_occurance_probability = uranium_occurance_probability
        self.xenon_occurance_probability = xenon_occurance_probability
        self.xenon_decay_probability = xenon_decay_probability

        # material of the fuel element
        self.material = material

        # radius of the fuel element
        self.radius = radius

        # creating the fuel element body and shape
        self.body, self.shape = self.create_non_uranium_fuel_element() if self.material == Material.NON_FISSILE else self.create_uranium_fuel_element()

        # adding the fuel element to the dictionary
        FuelElement.body_to_fuel_element[(self.body, self.shape)] = self

    # create Uranium fuel element
    def create_uranium_fuel_element(self):
        fuel_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        fuel_shape = pymunk.Circle(fuel_body, self.radius)
        fuel_shape.collision_type = 3
        fuel_shape.sensor = True

        return fuel_body, fuel_shape

    # create non-uranium fuel element
    def create_non_uranium_fuel_element(self):
        fuel_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        fuel_shape = pymunk.Circle(fuel_body, self.radius)
        fuel_shape.collision_type = 4
        fuel_shape.sensor = True
        return fuel_body, fuel_shape

    # create xenon fuel element
    def create_xenon_fuel_element(self):
        fuel_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        fuel_shape = pymunk.Circle(fuel_body, self.radius)
        fuel_shape.collision_type = 8
        fuel_shape.sensor = True
        return fuel_body, fuel_shape

    def change_material(self):
        # get probability
        prob = get_probability((0, 1000))

        if self.material == Material.NON_FISSILE:
            if prob < self.xenon_occurance_probability:
                self.set_material(Material.XENON)
            elif prob < self.uranium_occurance_probability:
                self.set_material(Material.FISSILE)
        elif self.material == Material.XENON:
            if prob < self.xenon_decay_probability:
                self.set_material(Material.NON_FISSILE)


    def get_body(self):
        return self.body

    def get_shape(self):
        return self.shape

    def get_material(self):
        return self.material

    def set_material(self, material):
        try:
            self.material = material
            if self.material == Material.FISSILE:
                self.shape.collision_type = 3
            elif self.material == Material.NON_FISSILE:
                self.shape.collision_type = 4
            elif self.material == Material.XENON:
                self.shape.collision_type = 8

        except Exception as e:
            print(e)

    def get_radius(self):
        return self.radius