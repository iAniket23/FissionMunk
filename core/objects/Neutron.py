# This file contains the Neutron class which is used to create neutron objects
import pymunk
class Neutron:
    # Constructor
    def __init__(self, speed, position, mass=0.1, radius=1, space=None):
        self.speed = speed
        self.position = position
        self.mass = mass
        self.radius = radius

        self.space = space
        self.body = None
        self.shape = self.create_neutron()

    # Create a neutron object
    def create_neutron(self):
        circle_body = pymunk.Body(self.mass, pymunk.moment_for_circle(self.mass, 0, self.radius), pymunk.Body.DYNAMIC)
        circle_shape = pymunk.Circle(circle_body, self.radius)
        circle_body.position = self.position
        circle_body.velocity = self.speed
        self.body = circle_body
        self.shape = circle_shape
        return self.shape

    def add_to_space(self, space=None):
        if space is None and self.space is None:
            raise ValueError("Space is not defined")
        elif space is None:
            self.space.add(self.body, self.shape)
        else:
            self.set_space(space)
            self.space.add(self.body, self.shape)
        return True

    # Getters and Setters
    def get_speed(self):
        return self.speed

    def get_position(self):
        if self.body:
            return self.body.position
        return self.position

    def get_mass(self):
        return self.mass

    def get_radius(self):
        return self.radius

    def get_body(self):
        return self.body

    def get_shape(self):
        return self.shape

    def set_space(self, space):
        self.space = space

    def get_space(self):
        return self.space

    def set_speed(self, speed):
        self.speed = speed

    def set_position(self, position):
        self.position = position
        if self.body:
            self.body.position = position

    def set_mass(self, mass):
        self.mass = mass

    def set_radius(self, radius):
        self.radius = radius

    def set_body(self, body):
        self.body = body

    def set_shape(self, shape):
        self.shape = shape