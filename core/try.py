# Import Neutron file from objects package
import pygame
from objects.Neutron import Neutron
from objects.Core import Core
from objects.Moderator import Moderator
from objects.ControlRod import ControlRod
from objects.Fuel import Fuel
from objects.Material import MaterialType as Material
from objects.mechanics import Mechanics as Mechanics
from objects.Water import Water

# Initialize Pygame
pygame.init()
display = pygame.display.set_mode((1220, 600))
clock = pygame.time.Clock()
FPS = 60

# Create a core object
core = Core(length=1220, width=600,thermal_factor=4, cold_factor=1, fast_factor=10)

# Add Moderator to the core
for i in range(10, 1220, 120):
    moderator = Moderator(length=10, width=580, position=(i, 290), material=Material.GRAPHITE)
    core.add_moderator_to_core(moderator)


for i in range(70, 1220, 120):
    if i % 2 == 0:
        tag = "E"
    else:
        tag = "O"
    control_rod = ControlRod(length=10, width=600, position=(i, 0), tag=tag, movement_range=[20, 580],material=Material.BORON_CARBIDE)
    core.add_control_rod_to_core(control_rod)

for i in range(25, 1205, 30):
    fuel_rod = Fuel(fuel_element_gap=10,uranium_occurance_probability=0.0001, xenon_occurance_probability=0.00001, xenon_decay_probability=0.00001, element_radius=10, width=560, position=(i, 25))
    core.add_fuel_rod_to_core(fuel_rod)

for i in range(25, 1205, 30):
   for j in range(25, 580, 30):
    water = Water(length=25, width=25, position=(i, j), coolant=True, hard_limit=30, temperature_threshold=100, material=Material.WATER)
    core.add_water_to_core(water)

# Create a mechanics object
mechanics = Mechanics(core)

def game():
    font = pygame.font.Font('freesansbold.ttf', 15)

    # create a text surface object,
    # on which text is drawn on it.
    # red color of text

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.fill((255, 255, 255))
        num = str(len(core.get_neutron_list()))
        text = font.render(num, True, (0, 0, 0))

        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()

        # set the center of the rectangular object.
        textRect.center = (300, 590)
        for water in core.get_water_list():
            pos = water.get_body().position
            pos = int(pos.x), int(pos.y)
            if water.removed:
                pygame.draw.rect(display, (255, 255, 255), (pos[0] - water.length // 2, pos[1] - water.width // 2, water.length, water.width))
            # gradually change the color of the water based on its temperature for every 10 degrees
            elif water.get_temperature() <= 10:
                pygame.draw.rect(display, (255, 200, 200), (pos[0] - water.length // 2, pos[1] - water.width // 2, water.length, water.width))
            elif water.get_temperature() <= 25:
                pygame.draw.rect(display, (255, 180, 180), (pos[0] - water.length // 2, pos[1] - water.width // 2, water.length, water.width))
            elif water.get_temperature() <= 50:
                pygame.draw.rect(display, (255, 160, 160), (pos[0] - water.length // 2, pos[1] - water.width // 2, water.length, water.width))
            elif water.get_temperature() <= 75:
                pygame.draw.rect(display, (255, 140, 140), (pos[0] - water.length // 2, pos[1] - water.width // 2, water.length, water.width))
            elif water.get_temperature() <= 90:
                pygame.draw.rect(display, (255, 120, 120), (pos[0] - water.length // 2, pos[1] - water.width // 2, water.length, water.width))
            elif water.get_temperature() <= 100:
                pygame.draw.rect(display, (255, 100, 100), (pos[0] - water.length // 2, pos[1] - water.width // 2, water.length, water.width))
            else:
                pygame.draw.rect(display, (255, 80, 80), (pos[0] - water.length // 2, pos[1] - water.width // 2, water.length, water.width))

        for fuel_rod in core.get_fuel_rod_list():
            for fuel_element in fuel_rod.get_fuel_elements():
                pos = fuel_element.get_body().position
                pos = int(pos.x), int(pos.y)
                if fuel_element.get_material() == Material.FISSILE:
                    # blue for fissile material
                    pygame.draw.circle(display,(48, 121, 203), pos, int(fuel_element.get_radius()))

                elif fuel_element.get_material() == Material.NON_FISSILE:
                    # dark grey for non-fissile material
                    pygame.draw.circle(display, (187, 187, 187), pos, int(fuel_element.get_radius()))

                elif fuel_element.get_material() == Material.XENON:
                    # black for xenon
                    pygame.draw.circle(display, (0, 0, 0), pos, int(fuel_element.get_radius()))
                fuel_element.change_material()

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

        for moderator in core.get_moderator_list():
            pos = moderator.get_body().position
            pos = int(pos.x), int(pos.y)
            pygame.draw.rect(display, (0, 0, 0), (pos[0] - moderator.get_length() // 2, pos[1] - moderator.width // 2, moderator.get_length(), moderator.width), 1)

        # keys = pygame.key.get_pressed()
        # movement = 0
        # if keys[pygame.K_UP]:
        #     movement = -5
        # elif keys[pygame.K_DOWN]:
        #     movement = 5

        movement = 0
        movement2 = 0
        if int(num) >=40:
            movement = 1
        else:
            movement = -1

        for control_rod in core.get_control_rod_list_E():
            control_rod.move_control_rod(movement)
            pos = control_rod.get_body().position
            pos = int(pos.x), int(pos.y)
            pygame.draw.rect(display, (128, 128, 128), (pos[0] - control_rod.get_length() // 2, pos[1] - control_rod.width // 2, control_rod.get_length(), control_rod.width))

        for control_rod in core.get_control_rod_list_O():
            control_rod.move_control_rod(movement2)
            pos = control_rod.get_body().position
            pos = int(pos.x), int(pos.y)
            pygame.draw.rect(display, (128, 128, 128), (pos[0] - control_rod.get_length() // 2, pos[1] - control_rod.width // 2, control_rod.get_length(), control_rod.width))

        display.blit(text, textRect)
        pygame.display.update()
        clock.tick(FPS)

        # Generate random neutron
        mechanics.generate_random_neutron(limit=0.08)
        mechanics.regulate_water_temperature()


        # Step the physics simulation
        core.get_space().step(1 / FPS)

game()
pygame.quit()