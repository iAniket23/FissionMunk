# Import Neutron file from objects package
import pygame
import pymunk
from objects.Neutron import Neutron
from objects.Core import Core

# Initialize Pygame
pygame.init()
display = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
space = pymunk.Space()
FPS = 60

# Create a core object
core = Core()

# Create a neutron object
neutron = Neutron(core.get_fast_speed(), (300, 300), 0.1, 5)

# Add the neutron to the core
core.add_to_core(neutron)

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        display.fill((255, 255, 255))

        # Get the neutron's current position (convert pymunk's coordinate system to pygame's)
        pos = neutron.get_position()
        pos = int(pos.x), 600 - int(pos.y)  # Pygame's y-axis is inverted

        # Draw the neutron on the screen with grey color
        pygame.draw.circle(display, (128, 128, 128), pos, int(neutron.get_radius()))

        pygame.display.update()
        clock.tick(FPS)
        
        # Step the physics simulation
        core.get_space().step(1 / FPS)

game()
pygame.quit()