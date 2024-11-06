import pymunk
from .Material import MaterialType as Material
class ControlRod:
    def __init__(self, length, width, position, material=Material.BORON_CARBIDE):
        self.length = length
        self.width = width
        self.position = position
        self.orginal_position = position

        assert material in Material, "Invalid material"
        self.material = material

        self.body, self.shape = self.create_control_rod()


    def create_control_rod(self):
        # make the control rod move with keyboard input up and down
        control_rod_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        control_rod_shape = pymunk.Poly.create_box(control_rod_body, (self.length, self.width))
        control_rod_body.position = self.position
        control_rod_shape.sensor = True
        control_rod_shape.collision_type = 5
        return control_rod_body, control_rod_shape

    def move_control_rod(self, amount):
        x, y = self.body.position
        if y + amount < -290:
            self.body.position = x, -290
        elif y + amount > 280:
            self.body.position = x, 280
        else:
            self.body.position = x, y + amount


    def reset_position(self):
        self.body.position = self.orginal_position

    def get_position(self):
        return self.position

    def set_position(self, position):
        try:
            self.position = position
            self.orginal_position = position
            if self.body:
                self.body.position = position
        except Exception as e:
            print(e)

    def get_body(self):
        return self.body

    def set_body(self, body):
        try:
            self.body = body
        except Exception as e:
            print(e)

    def get_shape(self):
        return self.shape

    def set_shape(self, shape):
        try:
            self.shape = shape
        except Exception as e:
            print(e)

    def get_length(self):
        return self.length

    def set_length(self, length):
        try:
            self.length = length
        except Exception as e:
            print(e)

    def get_width(self):
        return self.width

    def set_width(self, width):
        try:
            self.width = width
        except Exception as e:
            print(e)