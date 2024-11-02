# Import Neutron file from objects package
import pygame
from objects.Neutron import Neutron
from objects.Core import Core
from objects.Moderator import Moderator
from objects.Material import MaterialType as Material
from objects.mechanics import Mechanics as Mechanics

# Initialize Pygame
pygame.init()
display = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
FPS = 60

# Create a core object
core = Core(factor=10)

# Create a neutron object
neutron = Neutron(speed=core.get_fast_speed(), position=(0, 100), mass=0.1, radius=5)

# Add Moderator to the core
moderator = Moderator(length=10, width=600, position=(400, 300), material=Material.GRAPHITE)


# Add the neutron to the core
core.add_to_core(neutron)
# Add the moderator to the core
core.add_to_core(moderator)

# Create a mechanics object
Mechanics(core)

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        display.fill((255, 255, 255))

        # Get the neutron's current position (convert pymunk's coordinate system to pygame's)
        pos = neutron.get_position()
        pos = int(pos.x), int(pos.y)  # Pygame's y-axis is inverted

        pos_moderator = moderator.get_body().position
        pos_moderator = int(pos_moderator.x), int(pos_moderator.y)

        # Draw the neutron on the screen with grey color
        pygame.draw.circle(display, (128, 128, 128), pos, int(neutron.get_radius()))

        # Draw the moderator on the screen with black color outline
        pygame.draw.rect(display, (0, 0, 0), (pos_moderator[0] - moderator.get_length() // 2, pos_moderator[1] - moderator.width // 2, moderator.get_length(), moderator.width), 1)

        pygame.display.update()
        clock.tick(FPS)
        
        # Step the physics simulation
        core.get_space().step(1 / FPS)

game()
pygame.quit()