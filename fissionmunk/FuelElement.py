from .Material import MaterialType as Material
from .helper import get_probability
import pymunk

# Fuel Element class
class FuelElement:
    """
        This class is used to create a fuel element.
    """
    body_to_fuel_element = {}
    def __init__(self, radius, uranium_occurance_probability, xenon_occurance_probability, xenon_decay_probability, material = Material.FISSILE):
        # Probability
        """
            The method is used to initialize the fuel element.

            Args:
                radius: int
                    The radius of the fuel element.
                uranium_occurance_probability: float
                    The probability of uranium occurance in the fuel element.
                xenon_occurance_probability: float
                    The probability of xenon occurance in the fuel element.
                xenon_decay_probability: float
                    The probability of xenon decay in the fuel element.
                material: Material
                    The material of the fuel element.

            Returns:
                None
        """
        self.uranium_occurance_probability = uranium_occurance_probability
        self.xenon_occurance_probability = xenon_occurance_probability
        self.xenon_decay_probability = xenon_decay_probability

        # material of the fuel element
        self.material = material

        # radius of the fuel element
        self.radius = radius

        # creating the fuel element body and shape
        if self.material == Material.NON_FISSILE:
            self.body, self.shape = self.create_non_uranium_fuel_element()
        elif self.material == Material.FISSILE:
            self.body, self.shape = self.create_uranium_fuel_element()
        elif self.material == Material.XENON:
            self.body, self.shape = self.create_xenon_fuel_element()

        # adding the fuel element to the dictionary
        FuelElement.body_to_fuel_element[(self.body, self.shape)] = self

    # create Uranium fuel element
    def create_uranium_fuel_element(self):
        """
            The method is used to create a uranium fuel element.
            This method is not public and should not be called from outside the class.

            Returns:
                fuel_body: pymunk.Body
                    The body of the fuel element.
                fuel_shape: pymunk.Circle
                    The shape of the fuel element.
        """
        fuel_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        fuel_shape = pymunk.Circle(fuel_body, self.radius)
        fuel_shape.collision_type = 3
        fuel_shape.sensor = True

        return fuel_body, fuel_shape

    # create non-uranium fuel element
    def create_non_uranium_fuel_element(self):
        """
            The method is used to create a non-uranium fuel element.
            This method is not public and should not be called from outside the class.

            Returns:
                fuel_body: pymunk.Body
                    The body of the fuel element.
                fuel_shape: pymunk.Circle
                    The shape of the fuel element.
        """
        fuel_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        fuel_shape = pymunk.Circle(fuel_body, self.radius)
        fuel_shape.collision_type = 4
        fuel_shape.sensor = True
        return fuel_body, fuel_shape

    # create xenon fuel element
    def create_xenon_fuel_element(self):
        """
            The method is used to create a xenon fuel element.
            This method is not public and should not be called from outside the class.
            
            Returns:
                fuel_body: pymunk.Body
                    The body of the fuel element.
                fuel_shape: pymunk.Circle
                    The shape of the fuel
        """
        fuel_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        fuel_shape = pymunk.Circle(fuel_body, self.radius)
        fuel_shape.collision_type = 8
        fuel_shape.sensor = True
        return fuel_body, fuel_shape

    def change_material(self):
        """
            The method is used to change the material of the fuel element.

            Returns:
                None
        """
        # get probability
        prob = get_probability()

        if self.material == Material.NON_FISSILE:
            if prob < self.xenon_occurance_probability:
                self.set_material(Material.XENON)
            elif prob < self.uranium_occurance_probability:
                self.set_material(Material.FISSILE)
        elif self.material == Material.XENON:
            if prob < self.xenon_decay_probability:
                self.set_material(Material.NON_FISSILE)


    def get_body(self):
        """
            The method is used to get the body of the fuel element.

            Returns:
                body: pymunk.Body
                    The body of the fuel element.
        """
        return self.body

    def get_shape(self):
        """
            The method is used to get the shape of the fuel element.

            Returns:
                shape: pymunk.Circle
                    The shape of the fuel element.
        """
        return self.shape

    def get_material(self):
        """
            The method is used to get the material of the fuel element.

            Returns:
                material: Material
                    The material of the fuel element.
        """
        return self.material

    def set_material(self, material):
        """
            The method is used to set the material of the fuel element.

            Args:
                material: Material
                    The material of the fuel element.

            Returns:
                None
        """
        self.material = material
        if self.material == Material.FISSILE:
            self.shape.collision_type = 3
        elif self.material == Material.NON_FISSILE:
            self.shape.collision_type = 4
        elif self.material == Material.XENON:
            self.shape.collision_type = 8

    def get_radius(self):
        """
            The method is used to get the radius of the fuel element.

            Returns:
                radius: int
                    The radius of the fuel element.
        """
        return self.radius

    def get_collision_type(self):
        """
            The method is used to get the collision type of the fuel element.

            Returns:
                collision_type: int
                    The collision type of the fuel element.
        """
        return self.shape.collision_type