import pymunk
from .material import MaterialType as Material

class Water:
    body_to_water = {}
    def __init__(self, length, width, position,coolant =True, hard_limit = 30, temperature_threshold = 100, material = Material.WATER):
        # Water dimensions
        self.length = length
        self.width = width
        self.temperature = 0
        self.coolant = coolant
        self.temperature_threshold = temperature_threshold
        self.hard_limit = hard_limit

        assert material in Material, "Invalid material"
        self.material = material

        # Create the water body and shape
        self.body, self.shape = self.create_water()
        self.body.position = position

        # Set the collision type of the water
        self.shape.collision_type = 11

        self.number_of_neutrons_interacting = 0

        self.removed = False

        self.body_to_water[(self.body, self.shape)] = self

    # Create the water
    def create_water(self):
        # Create the water body
        water_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        water_shape = pymunk.Poly.create_box(water_body, (self.length, self.width))

        # Set the sensor of the water, which is used to detect collision
        water_shape.sensor = True
        return water_body, water_shape

    def change_temperature(self, amount):
        if self.coolant:
            if self.temperature >= self.temperature_threshold + self.hard_limit:
                self.temperature = self.temperature_threshold

        self.temperature += amount

        if self.temperature < 0:
            self.temperature = 0
        elif self.temperature > self.temperature_threshold:
            self.remove_water()
        elif self.temperature <= self.temperature_threshold - self.hard_limit and self.removed and self.coolant:
            self.recreate_water()

    def turn_on_coolant(self):
        self.coolant = True

    def turn_off_coolant(self):
        self.coolant = False

    def remove_water(self):
        if not self.removed:
            self.change_collision_type(12)
            self.removed = True

    def increase_number_of_neutrons_interacting(self, amount = 1):
        self.number_of_neutrons_interacting += amount

    def decrease_number_of_neutrons_interacting(self, amount = 1):
        self.number_of_neutrons_interacting -= amount

    def recreate_water(self):
        if self.removed:
            self.change_collision_type(11)
            self.removed = False

    def change_collision_type(self, collision_type = 11):
        self.shape.collision_type = collision_type

    def get_collision_type(self):
        return self.shape.collision_type

    def get_position(self):
        return self.body.position

    def get_temperature(self):
        return self.temperature

    def get_body(self):
        return self.body

    def get_shape(self):
        return self.shape

    def get_number_of_neutrons_interacting(self):
        return self.number_of_neutrons_interacting