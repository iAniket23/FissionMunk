# Import Neutron file from objects package
import pygame
import pymunk
from objects.Neutron import Neutron

# Initialize Pygame
pygame.init()
display = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
space = pymunk.Space()
FPS = 60

# Create a neutron object with velocity as a 2D vector (e.g., x, y)
neutron = Neutron((100, 0), (300, 300), 200, 0.1, 5, space)
neutron.add_to_space()

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
        space.step(1 / FPS)

game()
pygame.quit()