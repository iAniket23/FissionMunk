# import the necessary packages
import pymunk
from .Material import MaterialType as Material

# ControlRod class
class ControlRod:
    def __init__(self, length, width, position, movement_range ,tag="E",material=Material.BORON_CARBIDE):
        # initialize the control rod
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
        # make the control rod move with keyboard input up and down
        control_rod_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        control_rod_shape = pymunk.Poly.create_box(control_rod_body, (self.length, self.width))

        # set the sensor of the control rod, which is used to detect collision
        control_rod_shape.sensor = True
        return control_rod_body, control_rod_shape

    # move the control rod
    def move_control_rod(self, amount):
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
        return self.body.position

    def set_position(self, position):
        self.body.position = position

    def get_body(self):
        return self.body

    def get_shape(self):
        return self.shape

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_reach_top(self):
        return self.reach_top

    def get_reach_bottom(self):
        return self.reach_bottom
    