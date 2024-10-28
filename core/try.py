# Import Neutron file from objects package
import pygame
import pymunk
# This file contains the Neutron class which is used to create neutron objects
import pymunk

class Neutron:
    # Constructor
    def __init__(self, speed, position, fission_speed, mass = 0.1, radius = 1, space = None):
        self.speed = speed
        self.position = position
        self.mass = mass
        self.radius = radius
        self.fission_speed = fission_speed
        self.space = space

    # Create a neutron object
    def create_neutron(self):
        circle_body = pymunk.Body(self.mass, 0, pymunk.Body.DYNAMIC)
        circle = pymunk.Circle(circle_body, self.radius)
        circle_body.position = self.position
        circle_body.velocity = self.speed
        return circle

    def add_to_space(self, space = None):
        if space is None and self.space is None:
            raise ValueError("Space is not defined")
            return False
        elif space is None:
            self.space.add(self.create_neutron())
        else:
            self.set_space(space)
            self.space.add(self.create_neutron())
        return True

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

    def set_space(self, space):
        self.space = space

    def get_space(self):
        return self.space

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
pygame.init()
display = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
space = pymunk.Space()
FPS = 60

# Create a neutron object
neutron = Neutron(100, (300, 300), 200, 0.1, 1, space)
neutron.add_to_space()
def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 255, 255))
        pos = int(neutron.get_position.x), 600 - int(neutron.get_position.y)
        pygame.draw.circle(display, (0, 0, 0), pos, int(neutron.get_radius), 1)
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pygame.quit()

