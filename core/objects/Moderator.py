# Slows down neutron speed and bring it to Fission speed

import pymunk
from .Material import MaterialType as Material

class Moderator:
    def __init__(self, length, width, position, material = Material.WATER):
        self.length = length
        self.width = width

        # check if the material is valid
        assert material in Material, "Invalid material"
        self.material = material

        self.body, self.shape = self.create_moderator()
        self.body.position = position
        self.shape.collision_type = 2
        self.shape.sensor = True

    def create_moderator(self):
        rect_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        rect_shape = pymunk.Poly.create_box(rect_body, (self.length, self.width))
        return rect_body, rect_shape

    # Getters and Setters
    def get_body(self):
        return self.body

    def get_shape(self):
        return self.shape

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_position(self):
        return self.body.position
    def set_position(self, position):
        self.body.position = position

    def get_material(self):
        return self.material