# Slows down neutron speed and bring it to Fission speed
import pymunk
from .Material import MaterialType as Material

class Moderator:
    """The Moderator class represents a moderator in the simulation.
    """
    def __init__(self, length, width, position, material = Material.WATER):
        """The constructor for the Moderator class.

        :param length: The length of the moderator.
        :type length: float
        :param width: The width of the moderator.
        :type width: float
        :param position: The position of the moderator.
        :type position: tuple
        :param material: The material of the moderator, defaults to Material.WATER
        :type material: MaterialType, optional
        """
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
        """The create_moderator method creates the moderator body and shape.

        :return: The moderator body and shape.
        :rtype: tuple
        """
        rect_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        rect_shape = pymunk.Poly.create_box(rect_body, (self.length, self.width))
        return rect_body, rect_shape

    # Getters and Setters
    def get_body(self):
        """The get_body method returns the body of the moderator.

        :return: The body of the moderator.
        :rtype: pymunk.Body
        """
        return self.body

    def get_shape(self):
        """The get_shape method returns the shape of the moderator.

        :return: The shape of the moderator.
        :rtype: pymunk.Shape
        """
        return self.shape

    def get_length(self):
        """The get_length method returns the length of the moderator.

        :return: The length of the moderator.
        :rtype: float
        """
        return self.length

    def get_width(self):
        """The get_width method returns the width of the moderator.

        :return: The width of the moderator.
        :rtype: float
        """
        return self.width

    def get_position(self):
        """The get_position method returns the position of the moderator.

        :return: The position of the moderator.
        :rtype: tuple
        """
        return self.body.position
    def set_position(self, position):
        """The set_position method sets the position of the moderator.

        :param position: The position of the moderator.
        :type position: tuple
        :return: None
        :rtype: None
        """
        self.body.position = position
        return None

    def get_material(self):
        """The get_material method returns the material of the moderator.

        :return: The material of the moderator.
        :rtype: MaterialType
        """
        return self.material