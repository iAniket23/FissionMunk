# Import Neutron file from objects package
import pygame
from objects.Neutron import Neutron
from objects.Core import Core
from objects.Moderator import Moderator
from objects.ControlRod import ControlRod
from objects.Fuel import Fuel
from objects.Material import MaterialType as Material
from objects.mechanics import Mechanics as Mechanics

# Initialize Pygame
pygame.init()
display = pygame.display.set_mode((1220, 600))
clock = pygame.time.Clock()
FPS = 30

# Create a core object
core = Core(thermal_factor=2, cold_factor=1, fast_factor=5)

# Create a neutron object
neutron = Neutron(speed=core.get_thermal_speed(), position=(300, 110), mass=0.1, radius=5)
core.add_neutron_to_core(neutron)

# Add Moderator to the core
for i in range(10, 1220, 120):
    moderator = Moderator(length=10, width=580, position=(i, 290), material=Material.GRAPHITE)
    core.add_moderator_to_core(moderator)

for i in range(70, 1220, 120):
    control_rod = ControlRod(length=10, width=600, position=(i, -290), material=Material.BORON_CARBIDE)
    core.add_control_rod_to_core(control_rod)

for i in range(25, 1205, 30):
    fuel_rod = Fuel(occurence_probability=0, fuel_element_gap=5, length=25, width=560, position=(i, 25), water_bool=True)
    core.add_fuel_rod_to_core(fuel_rod)

# Create a mechanics object
Mechanics(core)

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.fill((255, 255, 255))

        for fuel_rod in core.get_fuel_rod_list():
            for fuel_element in fuel_rod.get_fuel_elements():
                pos = fuel_element.get_water_body().position
                pos = int(pos.x), int(pos.y)
                # light blue for water
                pygame.draw.rect(display, (225, 235, 245), (pos[0] - fuel_element.length // 2, pos[1] - fuel_element.length // 2, fuel_element.length, fuel_element.length))

                pos = fuel_element.get_body().position
                pos = int(pos.x), int(pos.y)
                if fuel_element.get_material() == Material.FISSILE:
                    # blue for fissile material
                    pygame.draw.circle(display,(48, 121, 203), pos, int(fuel_element.get_radius()))

                else:
                    # dark grey for non-fissile material
                    pygame.draw.circle(display, (187, 187, 187), pos, int(fuel_element.get_radius()))
                fuel_element.random_fissile_material()
        # Get the neutron's current position (convert pymunk's coordinate system to pygame's)
        for neutron in core.get_neutron_list():
            pos = neutron.get_body().position
            pos = int(pos.x), int(pos.y)
            threshold = 0.5
            if (neutron.body.velocity.length - core.thermal_speed.length) <= threshold:
                # red color for thermal neutron
                pygame.draw.circle(display, (255, 0, 0), pos, neutron.get_radius())
            else:
                # red outline for slow neutron
                pygame.draw.circle(display, (255, 0, 0), pos, neutron.get_radius(), 2)

        keys = pygame.key.get_pressed()
        movement = 0
        if keys[pygame.K_UP]:
            movement = -10
        elif keys[pygame.K_DOWN]:
            movement = 10

        for moderator in core.get_moderator_list():
            pos = moderator.get_body().position
            pos = int(pos.x), int(pos.y)
            pygame.draw.rect(display, (0, 0, 0), (pos[0] - moderator.get_length() // 2, pos[1] - moderator.width // 2, moderator.get_length(), moderator.width), 1)


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