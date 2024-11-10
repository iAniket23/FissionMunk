import pymunk
from .Material import MaterialType as Material

class Water:
    def __init__(self, length, width, position, material = Material.WATER):
        # Water dimensions
        self.length = length
        self.width = width
        self.temperature = 0


        assert material in Material, "Invalid material"
        self.material = material

        # Create the water body and shape
        self.body, self.shape = self.create_water()
        self.body.position = position

        # Set the collision type of the water
        self.shape.collision_type = 11

    # Create the water
    def create_water(self):
        # Create the water body
        water_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        water_shape = pymunk.Poly.create_box(water_body, (self.length, self.width))

        # Set the sensor of the water, which is used to detect collision
        water_shape.sensor = True
        return water_body, water_shape

    def change_temperature(self, amount):
        self.temperature += amount

    def change_collision_type(self, collision_type = 11):
        self.shape.collision_type = collision_type

    def get_collision_type(self):
        return self.shape.collision_type

    def get_position(self):
        return self.body.position

    def get_temperature(self):
        return self.temperature
