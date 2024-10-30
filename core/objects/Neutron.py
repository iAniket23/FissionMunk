# Neutron class
import pymunk

class Neutron:
    # Constructor
    def __init__(self, speed, position, mass=0.1, radius=1):
        self.speed = speed
        self.position = position
        self.mass = mass
        self.radius = radius
        self.moment_inertia = self.initialize_moment_inertia()
        self.body, self.shape = self.create_neutron()
        self.shape.elasticity = 1
        self.shape.collision_type = 1


    # Create a neutron object
    def create_neutron(self):
        circle_body = pymunk.Body(self.mass, self.moment_inertia, pymunk.Body.DYNAMIC)
        circle_shape = pymunk.Circle(circle_body, self.radius)
        circle_body.position = self.position
        circle_body.velocity = self.speed

        return circle_body, circle_shape

    def initialize_moment_inertia(self):
        circle_moment_inertia = pymunk.moment_for_circle(self.mass, 0, self.radius)
        return circle_moment_inertia


    # Getters and Setters
    def get_moment_inertia(self):
        return self.moment_inertia

    def set_moment_inertia(self, moment_inertia):
        try:
            self.moment_inertia = moment_inertia
        except Exception as e:
            print(e)
        else:
            print("Moment of inertia set successfully")

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        try:
            self.speed = speed
            self.body.velocity = self.speed

        except Exception as e:
            print(e)
        else:
            print("Speed set successfully")

    def get_position(self):
        if self.body:
            return self.body.position
        return self.position

    def set_position(self, position):
        try:
            self.position = position
            if self.body:
                self.body.position = position
        except Exception as e:
            print(e)
        else:
            print("Position set successfully")

    def get_mass(self):
        return self.mass

    def set_mass(self, mass):
        try:
            self.mass = mass
            if self.body:
                self.body.mass = mass
        except Exception as e:
            print(e)
        else:
            print("Mass set successfully")

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        try:
            self.radius = radius
            if self.shape:
                self.shape.radius = radius
        except Exception as e:
            print(e)
        else:
            print("Radius set successfully")

    def get_body(self):
        return self.body

    def set_body(self, body):
        try:
            self.body = body
        except Exception as e:
            print(e)
        else:
            print("Body set successfully")

    def get_shape(self):
        return self.shape

    def set_shape(self, shape):
        try:
            self.shape = shape
        except Exception as e:
            print(e)
        else:
            print("Shape set successfully")