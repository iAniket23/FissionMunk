from .Material import MaterialType as Material
from .FuelElement import FuelElement
from .helper import get_probability

# Fuel rod class
class Fuel:
    """The class is used to create a fuel rod.
    """
    def __init__(self, uranium_occurance_probability, xenon_occurance_probability, xenon_decay_probability, element_radius, width, position, fuel_element_gap = 5):
        """The method is used to initialize the fuel rod.

        :param uranium_occurance_probability: The probability of uranium occurance in the fuel rod.
        :type uranium_occurance_probability: float
        :param xenon_occurance_probability: The probability of xenon occurance in the fuel rod.
        :type xenon_occurance_probability: float
        :param xenon_decay_probability: The probability of xenon decay in the fuel rod.
        :type xenon_decay_probability: float
        :param element_radius: The radius of individual the fuel element.
        :type element_radius: int
        :param width: The width of the fuel rod.
        :type width: int
        :param position: The position of the fuel rod.
        :type position: tuple
        :param fuel_element_gap: The gap between fuel elements in the fuel rod.
        :type fuel_element_gap: int, optional
        """
        self.uranium_occurance_probability = uranium_occurance_probability
        self.xenon_occurance_probability = xenon_occurance_probability
        self.xenon_decay_probability = xenon_decay_probability

        # Length and width of the fuel rod
        self.length = 2*element_radius
        self.width = width
        self.radius = element_radius
        self.position = position

        # gap between fuel elements
        self.fuel_element_gap = fuel_element_gap

        # list of fuel elements in the fuel rod
        self.fuel_elements = []

        # Position of the fuel rod
        for i in range(0, self.width, self.length + self.fuel_element_gap):
            if get_probability() < self.uranium_occurance_probability:
                fuel_element = FuelElement(self.radius, self.uranium_occurance_probability, self.xenon_occurance_probability, self.xenon_decay_probability, material=Material.FISSILE)
                fuel_element.body.position = (self.position[0], self.position[1] + i)
                self.fuel_elements.append(fuel_element)
            else:
                fuel_element = FuelElement(self.radius, self.uranium_occurance_probability, self.xenon_occurance_probability, self.xenon_decay_probability, material=Material.NON_FISSILE)
                fuel_element.body.position = (self.position[0], self.position[1] + i)
                self.fuel_elements.append(fuel_element)

    # get the fuel elements list
    def get_fuel_elements(self):
        """The method is used to get the fuel elements list.

        :return: fuel_elements
        :rtype: list
        """
        return self.fuel_elements

    # get the length of the fuel rod
    def get_length(self):
        """The method is used to get the length of the fuel rod.

        :return: length
        :rtype: float
        """
        return self.length

    # get the width of the fuel rod
    def get_width(self):
        """The method is used to get the width of the fuel rod.

        :return: width
        :rtype: float
        """
        return self.width

    # get the position of the fuel rod
    def get_position(self):
        """The method is used to get the position of the fuel rod.

        :return: position
        :rtype: tuple
        """
        return self.position

    def get_radius(self):
        """The method is used to get the radius of the fuel rod.

        :return: radius
        :rtype: int
        """
        return self.radius