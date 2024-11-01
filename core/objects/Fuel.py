import pymunk
import random

from .Material import MaterialType as Material

class Fuel:
    def __init__(self, occurrence_probability, length, position):
        self.occurrence_probability = occurrence_probability
        self.length = 10
        self.width = 10
        self.position = position
        self.fuel_elements = []

        self.create_fuel_rod()

    def create_fuel_rod(self):
        for i in range(0, self.length):
            c = random.random()
            if c < self.occurrence_probability:
                fuel_element = FuelElement((self.position[0], self.position[1]+(i*30)), 1, Material.FISSILE)
            else:
                fuel_element = FuelElement((self.position[0], self.position[1]+(i*30)), 1, Material.NONFISSILE)
            self.fuel_elements.append(fuel_element)

class FuelElement:
    def __init__(self, position, radius,  type = Material.NONFISSILE):
        self.type = type
        self.position = position
        self.radius = radius
        self.body, self.shape = self.create_fuel_element()

    def create_fuel_element(self):
        if self.type == Material.FISSILE:
            return self.create_fuel_element_fissionable()
        else:
            return self.create_fuel_element_non_fissionable()

    def create_fuel_element_fissionable(self):
        circle_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        circle_shape = pymunk.Circle(circle_body, self.radius)
        circle_body.position = self.position
        circle_shape.collision_type = 3
        return circle_body, circle_shape

    def create_fuel_element_non_fissionable(self):
        circle_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        circle_shape = pymunk.Circle(circle_body, self.radius)
        circle_body.position = self.position
        circle_shape.collision_type = 4
        circle_shape.sensor = True
        return circle_body, circle_shape

    def get_body(self):
        return self.body

    def set_body(self, body):
        try:
            self.body = body
        except Exception as e:
            print(e)
        else:
            print("Body set successfully")

    def get_shape(self):
        return self.shape

    def set_shape(self, shape):
        try:
            self.shape = shape
        except Exception as e:
            print(e)
        else:
            print("Shape set successfully")

    def get_position(self):
        if self.body:
            return self.body.position
        return self.position

    def set_position(self, position):
        try:
            self.position = position
            self.body.position = self.position
        except Exception as e:
            print(e)
        else:
            print("Position set successfully")

    def get_length(self):
        return self.length

    def set_length(self, length):
        try:
            self.length = length
        except Exception as e:
            print(e)
        else:
            print("Length set successfully")

    def get_width(self):
        return self.width

    def set_width(self, width):
        try:
            self.width = width
        except Exception as e:
            print(e)
        else:
            print("Width set successfully")