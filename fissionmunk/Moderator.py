# Slows down neutron speed and bring it to Fission speed
import pymunk
from .Material import MaterialType as Material

class Moderator:
    """
        A class to represent a moderator in a nuclear reactor.
        Moderators are used to slow down neutrons to speeds that are more likely to cause fission.
    """
    def __init__(self, length, width, position, material = Material.WATER):
        """
            Constructor for the Moderator class.

            Args:
                length (int):
                    The length of the moderator.
                width (int):
                    The width of the moderator.
                position (tuple):
                    The position of the moderator.
                material (MaterialType):
                    The material of the moderator.
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
        """
        Creates a moderator body and shape.

        Returns:
            rect_body (pymunk.Body): body of the moderator.
            rect_shape (pymunk.Poly): shape of the moderator.
        """
        rect_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        rect_shape = pymunk.Poly.create_box(rect_body, (self.length, self.width))
        return rect_body, rect_shape

    # Getters and Setters
    def get_body(self):
        """
            Returns the body of the moderator.

            Returns:
                body (pymunk.Body):
                    The body of the moderator.
        """
        return self.body

    def get_shape(self):
        """
            Returns the shape of the moderator.

            Returns:
                shape (pymunk.Poly):
                    The shape of the moderator.
        """
        return self.shape

    def get_length(self):
        """
            Returns the length of the moderator.

            Returns:
                length (int):
                    The length of the moderator.
        """
        return self.length

    def get_width(self):
        """
            Returns the width of the moderator.

            Returns:
                width (int):
                    The width of the moderator.
        """
        return self.width

    def get_position(self):
        """
            Returns the position of the moderator.

            Returns:
                position (tuple):
                    The position of the moderator.
        """
        return self.body.position
    def set_position(self, position):
        """
            Sets the position of the moderator.

            Args:
                position (tuple):
                    The position of the moderator.

            Returns:
                None
        """
        self.body.position = position

    def get_material(self):
        """
            Returns the material of the moderator.

            Returns:
                material (MaterialType):
                    The material of the moderator.
        """
        return self.material