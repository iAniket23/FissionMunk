# import the necessary packages
import pymunk
from .Material import MaterialType as Material

# ControlRod class
class ControlRod:
    """
        The ControlRod class is used to create the control rod in the reactor.
        It is used to control the fission reaction in the reactor as it absorbs the neutron.
    """
    def __init__(self, length, width, position, movement_range ,tag="E",material=Material.BORON_CARBIDE):
        """
            The constructor of the ControlRod class.

            Parameters:
                length: int The length of the control rod.
                width: int
                    The width of the control rod.
                position: tuple
                    The position of the control rod.
                movement_range: tuple
                    The movement range of the control rod in the reactor space.
                tag: str
                    The tag of the control rod. It is used to identify the control rod in order to control it individually.
                material: MaterialType
                    The material of the control rod.
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
        """
            The method is used to create the control rod.
            This is not a public method.

            Returns:
                control_rod_body: pymunk.Body
                    The body of the control rod.
                control_rod_shape: pymunk.Poly
                    The shape of the control rod.
        """
        # make the control rod move with keyboard input up and down
        control_rod_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        control_rod_shape = pymunk.Poly.create_box(control_rod_body, (self.length, self.width))

        # set the sensor of the control rod, which is used to detect collision
        control_rod_shape.sensor = True
        return control_rod_body, control_rod_shape

    # move the control rod
    def move_control_rod(self, amount):
        """
            The method is used to move the control rod.

            Args:
                amount: int
                    The amount by which the control rod is moved

            Returns:
                None
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

    # Getters and Setters
    def get_position(self):
        """
            The method is used to get the position of the control rod.

            Returns:
                position: tuple
                    The position of the control rod.
        """
        return self.body.position

    def set_position(self, position):
        """
            The method is used to set the position of the control rod.

            Args:
                position: tuple
                    The position of the control rod.

            Returns:
                None
        """
        self.body.position = position

    def get_body(self):
        """
            The method is used to get the body of the control rod.

            Returns:
                body: pymunk.Body
                    The body of the control
        """
        return self.body

    def get_shape(self):
        """
            The method is used to get the shape of the control rod.

            Returns:
                shape: pymunk.Poly
                    The shape of the control rod.
        """
        return self.shape

    def get_length(self):
        """
            The method is used to get the length of the control rod.

            Returns:
                length: int
                    The length of the control
        """
        return self.length

    def get_width(self):
        """
            The method is used to get the width of the control rod.

            Returns:
                width: int
                    The width of the control
        """
        return self.width

    def get_reach_top(self):
        """
            The method is used to check if the control rod has reached the top of the reactor space. (movement range)

            Returns:
                reach_top: bool
                    True if the control rod has reached the top of the reactor space. Otherwise, False.
        """
        return self.reach_top

    def get_reach_bottom(self):
        """
            The method is used to check if the control rod has reached the bottom of the reactor space. (movement range)

            Returns:
                reach_bottom: bool
                    True if the control rod has reached the bottom of the reactor space. Otherwise, False.
        """
        return self.reach_bottom
    def get_tag(self):
        """
            The method is used to get the tag of the control rod.

            Returns:
                tag: str
                    The tag of the control rod.
        """
        return self.tag
    def set_tag(self,tag):
        """
            The method is used to set the tag of the control rod.

            Args:
                tag: str
                    The tag of the control rod.

            Returns:
                None
        """
        self.tag = tag