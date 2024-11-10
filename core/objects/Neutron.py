# Neutron class
import pymunk

# import pygame
# pygame.mixer.init()

class Neutron:
    body_to_neutron = {}

    # Constructor
    def __init__(self, speed, position, mass=0.1, radius=1):
        self.mass = mass
        self.radius = radius

        self.body, self.shape = self.create_neutron()
        self.body.position = position
        self.body.velocity = speed

        self.shape.collision_type = 1
        self.shape.sensor = True

        # self.geiger_tick_sound = pygame.mixer.Sound("geiger_tick.mp3")
        # self.geiger_tick_sound.play()  # Play the sound

        Neutron.body_to_neutron[(self.body, self.shape)] = self

    # Create a neutron object
    def create_neutron(self):
        circle_body = pymunk.Body(self.mass, self.initialize_moment_inertia(), pymunk.Body.DYNAMIC)
        circle_shape = pymunk.Circle(circle_body, self.radius)
        return circle_body, circle_shape

    def remove_neutron(self):
        try:
            self.body_to_neutron.pop((self.body, self.shape))
        except Exception as e:
            # print(e)
            pass
        else:
            return True

    def initialize_moment_inertia(self):
        circle_moment_inertia = pymunk.moment_for_circle(self.mass, 0, self.radius)
        return circle_moment_inertia

    def get_speed(self):
        return self.body.velocity

    def set_speed(self, speed):
        try:
            self.body.velocity = speed

        except Exception as e:
            # print(e)
            pass

    def get_position(self):
        return self.body.position

    def set_position(self, position):
        self.body.position = position

    def get_mass(self):
        return self.mass

    def get_radius(self):
        return self.radius

    def get_body(self):
        return self.body

    def get_shape(self):
        return self.shape
