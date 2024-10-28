# This file contains the Neutron class which is used to create neutron objects
import pymunk

class Neutron:
    # Constructor
    def __init__(self, speed, position, fission_speed, mass = 0.1, radius = 1):
        self.speed = speed
        self.position = position
        self.mass = mass
        self.radius = radius
        self.fission_speed = fission_speed

    # Create a neutron object
    def createNeutron(self):
        circle_body = pymunk.Body(self.mass, 0, pymunk.Body.DYNAMIC)
        circle = pymunk.Circle(circle_body, self.radius)
        circle_body.position = self.position
        circle_body.velocity = self.speed

        return circle

    # Getters and Setters
    def get_speed(self):
        return self.speed

    def get_position(self):
        return self.position

    def get_mass(self):
        return self.mass

    def get_radius(self):
        return self.radius

    def get_fission_speed(self):
        return self.fission_speed

    def set_speed(self, speed):
        self.speed = speed

    def set_position(self, position):
        self.position = position

    def set_mass(self, mass):
        self.mass = mass

    def set_radius(self, radius):
        self.radius = radius

    def set_fission_speed(self, fission_speed):
        self.fission_speed = fission_speed