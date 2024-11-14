# import the necessary packages
import pymunk
from .Material import MaterialType as Material

# ControlRod class
class ControlRod:
    """The class is used to create a control rod in the reactor space.
    """
    def __init__(self, length, width, position, movement_range ,tag="E",material=Material.BORON_CARBIDE):
        """The method is used to initialize the control rod.

        :param length: The length of the control rod
        :type length: float
        :param width: The width of the control rod
        :type width: float
        :param position: The position of the control rod
        :type position: tuple
        :param movement_range: The movement range of the control rod
        :type movement_range: tuple
        :param tag: The tag of the control rod, defaults to "E"
        :type tag: str, optional
        :param material: The material of the control rod, defaults to Material.BORON_CARBIDE
        :type material: MaterialType, optional
        """
        self.length = length
        self.width = width
        self.tag = tag
        self.reach_top = False
        self.reach_bottom = False
        # add length // 2 to the y position to the movement range
        self.movement_range = (movement_range[0] - (width//2), movement_range[1] - (width//2))

        # set the material of the control rod
        assert material in Material, "Invalid material"
        self.material = material

        # create the control rod
        self.body, self.shape= self.create_control_rod()
        self.body.position = position

        # set the collision type of the control rod
        self.shape.collision_type = 5

    # create the control rod
    def create_control_rod(self):
        """The method is used to create the control rod.

        :return: The body and shape of the control rod
        :rtype: tuple
        """
        # make the control rod move with keyboard input up and down
        control_rod_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        control_rod_shape = pymunk.Poly.create_box(control_rod_body, (self.length, self.width))

        # set the sensor of the control rod, which is used to detect collision
        control_rod_shape.sensor = True
        return control_rod_body, control_rod_shape

    # move the control rod
    def move_control_rod(self, amount):
        """The method is used to move the control rod.

        :param amount: The amount to move the control rod
        :type amount: float
        :return: None
        :rtype: None
        """
        x, y = self.body.position
        if y + amount < self.movement_range[0]:
            self.body.position = x, self.movement_range[0]
            self.reach_top = True
        elif y + amount > self.movement_range[1]:
            self.body.position = x, self.movement_range[1]
            self.reach_bottom = True
        else:
            self.body.position = x, y + amount
            self.reach_top = False
            self.reach_bottom = False
        return None
    # Getters and Setters
    def get_position(self):
        """The method is used to get the position of the control rod.

        :return: The position of the control rod
        :rtype: tuple
        """
        return self.body.position

    def set_position(self, position):
        """The method is used to set the position of the control rod.

        :param position: The position of the control rod
        :type position: tuple
        :return: None
        :rtype: None
        """
        self.body.position = position

        return None

    def get_body(self):
        """The method is used to get the body of the control rod.

        :return: The body of the control rod
        :rtype: pymunk.Body
        """
        return self.body

    def get_shape(self):
        """The method is used to get the shape of the control rod.

        :return: The shape of the control rod
        :rtype: pymunk.Shape
        """
        return self.shape

    def get_length(self):
        """The method is used to get the length of the control rod.

        :return: The length of the control rod
        :rtype: float
        """
        return self.length

    def get_width(self):
        """The method is used to get the width of the control rod.

        :return: The width of the control rod
        :rtype: float
        """
        return self.width

    def get_reach_top(self):
        """The method is used to get the reach top boolean of the control rod.

        :return: The reach top boolean of the control rod
        :rtype: bool
        """
        return self.reach_top

    def get_reach_bottom(self):
        """The method is used to get the reach bottom boolean of the control rod.

        :return: The reach bottom boolean of the control rod
        :rtype: bool
        """
        return self.reach_bottom
    def get_tag(self):
        """The method is used to get the tag of the control rod.

        :return: The tag of the control rod
        :rtype: str
        """
        return self.tag
    def set_tag(self,tag):
        """The method is used to set the tag of the control rod.

        :param tag: The tag of the control rod
        :type tag: str
        :return: None
        :rtype: None
        """
        self.tag = tag
        return None