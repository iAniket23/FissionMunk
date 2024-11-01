# Slows down neutron speed and bring it to Fission speed

import pymunk
from .Material import MaterialType as Material

class Moderator:
    def __init__(self, length, width, position, material = Material.WATER):
        self.length = length
        self.width = width
        self.position = position

        # check if the material is valid
        assert material in Material, "Invalid material"
        self.material = material

        self.body, self.shape = self.create_water_moderator() if self.material == Material.WATER else self.create_non_water_moderator()
        self.shape.collision_type = 2
        self.shape.sensor = True

    def create_non_water_moderator(self):
        rect_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        rect_shape = pymunk.Poly.create_box(rect_body, (self.length, self.width))
        rect_body.position = self.position
        return rect_body, rect_shape

    def create_water_moderator(self):
        pass

    # Getters and Setters
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

    def get_position(self):
        return self.position
    def set_position(self, position):
        try:
            self.position = position
        except Exception as e:
            print(e)
        else:
            print("Position set successfully")

    def get_material(self):
        return self.material

    def set_material(self, material):
        try:
            assert material in Material, "Invalid material"
            self.material = material
        except Exception as e:
            print(e)
        else:
            print("Material set successfully")