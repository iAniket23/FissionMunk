import pymunk
from .Material import MaterialType as Material

class Water:
    """
        The Water class is used to create a water body in the simulation.
        Water absorbs neutrons and cools down the reactor. It is used as a coolant in the reactor.
    """
    body_to_water = {}
    def __init__(self, length, width, position,coolant =True, hard_limit = 30, temperature_threshold = 100, material = Material.WATER):
        """
            Constructor for the Water class.

            Args:
                length (int):
                    The length of the water.
                width (int):
                    The width of the water.
                position (tuple):
                    The position of the water.
                coolant (bool):
                    Whether the water is a coolant or not.
                hard_limit (int):
                    The hard limit of the water temperature.
                temperature_threshold (int):
                    The temperature threshold of the water.
                material (MaterialType):
                    The material of the water.

            Returns:
                None
        """
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
        """
            Creates a water body and shape.
            This method is not public.

            Returns:
                water_body (pymunk.Body):
                    The body of the water.
                water_shape (pymunk.Poly):
                    The shape of the water
        """
        # Create the water body
        water_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        water_shape = pymunk.Poly.create_box(water_body, (self.length, self.width))

        # Set the sensor of the water, which is used to detect collision
        water_shape.sensor = True
        return water_body, water_shape

    def change_temperature(self, amount):
        """
            Changes the temperature of the water.

            Args:
                amount (int):
                    The amount by which the temperature is to be changed.

            Returns:
                None
        """
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
        """
            Turns on the coolant of the water.

            Returns:
                None
        """
        self.coolant = True

    def turn_off_coolant(self):
        """
            Turns off the coolant of the water.

            Returns:
                None
        """
        self.coolant = False

    def remove_water(self):
        """
            Removes the water from the simulation.

            Returns:
                None
        """
        if not self.removed:
            self.change_collision_type(12)
            self.removed = True

    def increase_number_of_neutrons_interacting(self, amount = 1):
        self.number_of_neutrons_interacting += amount

    def decrease_number_of_neutrons_interacting(self, amount = 1):
        self.number_of_neutrons_interacting -= amount

    def recreate_water(self):
        """
            Refill the water.

            Returns:
                None
        """
        if self.removed:
            self.change_collision_type(11)
            self.removed = False

    def change_collision_type(self, collision_type = 11):
        """
            Changes the collision type of the water.

            Args:
                collision_type (int):
                    The collision type of the water.

            Returns:
                None
        """
        self.shape.collision_type = collision_type

    def get_collision_type(self):
        """
            Returns the collision type of the water.

            Returns:
                collision_type (int):
                    The collision type of the water.
        """
        return self.shape.collision_type

    def get_position(self):
        """
            Returns the position of the water.

            Returns:
                position (tuple):
                    The position of the water.
        """
        return self.body.position

    def get_temperature(self):
        """
            Returns the temperature of the water.

            Returns:
                temperature (int):
                    The temperature of the water.
        """
        return self.temperature

    def get_body(self):
        """
            Returns the body of the water.

            Returns:
                body (pymunk.Body):
                    The body of the water.
        """
        return self.body

    def get_shape(self):
        """
            Returns the shape of the water.

            Returns:
                shape (pymunk.Poly):
                    The shape of the water.
        """
        return self.shape

    def get_number_of_neutrons_interacting(self):
        return self.number_of_neutrons_interacting