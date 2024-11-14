import pymunk
from .Material import MaterialType as Material

class Water:
    """This class represents water in the simulation.
    """
    body_to_water = {}
    def __init__(self, length, width, position,coolant =True, hard_limit = 30, temperature_threshold = 100, material = Material.WATER):
        """This method initializes the water object.

        :param length: The length of the water.
        :type length: float
        :param width: The width of the water.
        :type width: float
        :param position: The position of the water.
        :type position: tuple
        :param coolant: The coolant of the water, defaults to True
        :type coolant: bool, optional
        :param hard_limit: The hard limit for the temperature of the water allowed, defaults to 30
        :type hard_limit: int, optional
        :param temperature_threshold: The temperature threshold of the water, defaults to 100
        :type temperature_threshold: int, optional
        :param material: The material of the water, defaults to Material.WATER
        :type material: MaterialType, optional
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
        """This method creates the water.

        :return: The body and shape of the water.
        :rtype: tuple
        """
        # Create the water body
        water_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        water_shape = pymunk.Poly.create_box(water_body, (self.length, self.width))

        # Set the sensor of the water, which is used to detect collision
        water_shape.sensor = True
        return water_body, water_shape

    def change_temperature(self, amount):
        """This method changes the temperature of the water.

        :param amount: The amount to change the temperature of the water.
        :type amount: int
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
        """This method turns on the coolant of the water.

        :return: None
        :rtype: None
        """
        self.coolant = True
        return None

    def turn_off_coolant(self):
        """This method turns off the coolant of the water.

        :return: None
        :rtype: None
        """
        self.coolant = False
        return None

    def remove_water(self):
        """This method removes the water from the simulation.

        :return: None
        :rtype: None
        """
        if not self.removed:
            self.change_collision_type(12)
            self.removed = True
        return None

    def increase_number_of_neutrons_interacting(self, amount = 1):
        self.number_of_neutrons_interacting += amount

    def decrease_number_of_neutrons_interacting(self, amount = 1):
        self.number_of_neutrons_interacting -= amount

    def recreate_water(self):
        """This method recreates the water in the simulation.

        :return: None
        :rtype: None
        """
        if self.removed:
            self.change_collision_type(11)
            self.removed = False
        return None

    def change_collision_type(self, collision_type = 11):
        """This method changes the collision type of the water.

        :param collision_type: The collision type of the water, defaults to 11
        :type collision_type: int, optional
        :return: None
        :rtype: None
        """
        self.shape.collision_type = collision_type
        return None

    def get_collision_type(self):
        """This method returns the collision type of the water.

        :return: The collision type of the water.
        :rtype: int
        """
        return self.shape.collision_type

    def get_position(self):
        """This method returns the position of the water.

        :return: The position of the water.
        :rtype: tuple
        """
        return self.body.position

    def get_temperature(self):
        """This method returns the temperature of the water.

        :return: The temperature of the water.
        :rtype: int
        """
        return self.temperature

    def get_body(self):
        """This method returns the body of the water.

        :return: The body of the water.
        :rtype: pymunk.Body
        """
        return self.body

    def get_shape(self):
        """This method returns the shape of the water.

        :return: The shape of the water.
        :rtype: pymunk.Poly
        """
        return self.shape

    def get_number_of_neutrons_interacting(self):
        return self.number_of_neutrons_interacting