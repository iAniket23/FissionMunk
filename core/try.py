# Import Neutron file from objects package
import pygame
from objects.Neutron import Neutron
from objects.Core import Core
from objects.Moderator import Moderator
from objects.Fuel import Fuel
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
neutron = Neutron(core.get_fast_speed(), (100, 200), 0.1, 5)
# Add Moderator to the core
moderator = Moderator(10, 200, (10, 10), Material.GRAPHITE)

# Add the fuel to the core
fuel = Fuel(0.3, 10, (200, 300))

# Add the neutron to the core
core.add_to_core(neutron)
# Add the moderator to the core
core.add_to_core(moderator)

# Add the fuel to the core
for fuel_element in fuel.fuel_elements:
    core.add_to_core(fuel_element)

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
        pos = int(pos.x), 600 - int(pos.y)  # Pygame's y-axis is inverted
        # Draw the neutron on the screen with grey color
        pygame.draw.circle(display, (128, 128, 128), pos, int(neutron.get_radius()))


        pos_moderator = moderator.get_position()
        pos_moderator = int(pos_moderator.x), 600 - int(pos_moderator.y)
        pygame.draw.rect(display, (0, 0, 0), (pos_moderator[0], pos_moderator[1], 10, 200))

        # Draw the moderator on the screen with black color


        # Draw the fuel on the screen with red color
        for fuel_element in fuel.fuel_elements:
            if fuel_element.type == Material.FISSILE:
                pos_fuel = fuel_element.get_position()
                pos_fuel = int(pos_fuel.x), 600 - int(pos_fuel.y)
                # outline the fuel element with white color and fill it with red color
                pygame.draw.circle(display, (255, 0, 0), pos_fuel, fuel.width)
            else:
                pos_fuel = fuel_element.get_position()
                pos_fuel = int(pos_fuel.x), 600 - int(pos_fuel.y)

                # outline the fuel element with white color and fill it with green color
                pygame.draw.circle(display, (0, 255, 0), pos_fuel, fuel.width)


        pygame.display.update()
        clock.tick(FPS)
        
        # Step the physics simulation
        core.get_space().step(1 / FPS)

game()
pygame.quit()