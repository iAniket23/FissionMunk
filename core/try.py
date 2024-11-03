# Import Neutron file from objects package
import pygame
from objects.Neutron import Neutron
from objects.Core import Core
from objects.Moderator import Moderator
from objects.ControlRod import ControlRod
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
moderator2 = Moderator(length=10, width=600, position=(200, 300), material=Material.GRAPHITE)

# Add Control Rod to the core
control_rod = ControlRod(length=10, width=600, position=(500, 300), material=Material.BORON_CARBIDE)
control_rod2 = ControlRod(length=10, width=600, position=(300, 300), material=Material.BORON_CARBIDE)

# Add the neutron to the core
core.add_neutron_to_core(neutron)

# Add the moderator to the core
core.add_moderator_to_core(moderator)
core.add_moderator_to_core(moderator2)

# Add the control rod to the core
core.add_control_rod_to_core(control_rod)
core.add_control_rod_to_core(control_rod2)

# Create a mechanics object
Mechanics(core)

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        display.fill((255, 255, 255))

        # Get the neutron's current position (convert pymunk's coordinate system to pygame's)
        for neutron in core.get_neutron_list():
            pos = neutron.get_body().position
            pos = int(pos.x), int(pos.y)
            pygame.draw.circle(display, (128, 128, 128), pos, int(neutron.get_radius()))

        for moderator in core.get_moderator_list():
            pos = moderator.get_body().position
            pos = int(pos.x), int(pos.y)
            pygame.draw.rect(display, (0, 0, 0), (pos[0] - moderator.get_length() // 2, pos[1] - moderator.width // 2, moderator.get_length(), moderator.width), 1)

        keys = pygame.key.get_pressed()
        movement = 0
        if keys[pygame.K_UP]:
            movement = -10
        elif keys[pygame.K_DOWN]:
            movement = 10


        for control_rod in core.get_control_rod_list():
            control_rod.move_control_rod(movement)
            pos = control_rod.get_body().position
            pos = int(pos.x), int(pos.y)
            pygame.draw.rect(display, (128, 128, 128), (pos[0] - control_rod.get_length() // 2, pos[1] - control_rod.width // 2, control_rod.get_length(), control_rod.width))

        pygame.display.update()
        clock.tick(FPS)

        # Step the physics simulation
        core.get_space().step(1 / FPS)

game()
pygame.quit()