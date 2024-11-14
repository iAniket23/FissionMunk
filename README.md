# FissionMunk

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PyPI version](https://badge.fury.io/py/fissionmunk.svg)
[![API Reference](https://img.shields.io/badge/API%20Reference-Docs-blue)](https://ianiket23.github.io/FissionMunk/)

**FissionMunk** is a lightweight 2D physics open source python library designed to simulate nuclear fission reactor mechanics. It enables users to visualize interactions between neutrons and uranium atoms, providing valuable insights into fission dynamics with customizable parameters, such as neutron occurrence probabilities, moderators, and control rods. FissionMunk is ideal for educational simulations, nuclear physics research, and interactive demos, and is built on top of the [Pymunk](http://www.pymunk.org/) library.

2024, Aniket Mishra - [ianiket23@github.io](https://ianiket23.github.io/)

- **Documentation**: [https://ianiket23.github.io/FissionMunk/](https://ianiket23.github.io/FissionMunk/)
- **Source code**: [https://github.com/iAniket23/fissionmunk](https://github.com/iAniket23/fissionmunk)  
- **PyPI**: [https://pypi.org/project/fissionmunk/](https://pypi.org/project/fissionmunk/)
- **Bug reports**: [https://github.com/iAniket23/fissionmunk/issues](https://github.com/iAniket23/fissionmunk/issues)  

## Features
- Interactive Simulation: Visualize neutron interactions with uranium in real-time, with configurable parameters.
- Modularity: Use customizable modules to add moderators, control rods, and other reactor elements.
- Educational Tool: Ideal for students and educators to explore nuclear fission mechanics.
- Open-Source: Fully open-source and extensible for customization and additional functionality.

## Getting Started with FissionMunk
FissionMunk makes it easy to simulate and visualize nuclear fission dynamics.
![rbmk](media/media_rbmk.gif)

To get started, follow these steps:

### Installation

To install FissionMunk, use `pip`:
```bash
pip install fissionmunk
```
### Set Up Your First Simulation
Now that you’ve installed FissionMunk, let's create a very basic simulation. First let's install a visualization library such as pygame (`pip install pygame`).
Here's an example to help you get started:

#### Example: Basic Fission Simulation
Now let's start by importing these libraries
```python
import pygame

from fissionmunk import Core
from fissionmunk import Moderator
from fissionmunk import ControlRod
from fissionmunk import Fuel
from fissionmunk import Water
from fissionmunk import Material
from fissionmunk import Mechanics
```

Initialize a display canvas using pygame
```python
# Initialize Pygame
pygame.init()
display = pygame.display.set_mode((700, 600))
clock = pygame.time.Clock()
FPS = 60
```
Now moving onto some fun stuff with Fissionmunk. In order to do simulation with fissionmunk we need to have some key items.

- **Core**: Manages the main simulation environment and fuel elements.
- **ControlRod**: Controls neutron absorption, allowing for fission rate adjustments.
- **Moderator**: Slows down neutrons to maintain optimal reaction rates.
- **FuelElement**: Represents fuel elements, such as uranium atoms, in the simulation.
- **Neutron**: Models individual neutrons and their interactions.

One thing to keep in mind is that we can tweak the probability of the occurance of the Fuel elements in a fuel rod.
Uranium-235 doesn't just occur all of a sudden in a rod but for the sake of the simulation we can pretend that Uranium-235 randomly occurs (refuel) in the rod.
```python
# Create a core object
core = Core(length=700, width=600,thermal_factor=4, cold_factor=1, fast_factor=10)

moderator = Moderator(length=10, width=580, position=(600, 290), material=Material.GRAPHITE)

control_rod = ControlRod(length=10, width=600, position=(500, 0), tag="E", movement_range=[20, 580],material=Material.BORON_CARBIDE)

fuel_rod = Fuel(fuel_element_gap=10,uranium_occurance_probability=0.0001, xenon_occurance_probability=0.00001, xenon_decay_probability=0.00001, element_radius=10, width=560, position=(300, 25))
```
We have initialized these reactor objects, and now it's time to actually add these in our Core.

```python
core.add_moderator_to_core(moderator)

core.add_control_rod_to_core(control_rod)

core.add_fuel_rod_to_core(fuel_rod)
```
Now let's add some water in our core. Water has some unique properties in the reactor. It acts as a neutron poison, as in, it absorbs neutron. One more property water have is temperature. More fission equals more heat which results in making the water heat up (ultimately resulting in water evaporating).

Now let's rather than making a big water rod, for the sake of our sample example, let's make a grid of water squares.
```python
for j in range(25, 580, 30):
    water = Water(length=25, width=25, position=(450, j), coolant=True, hard_limit=30, temperature_threshold=100, material=Material.WATER)
    core.add_water_to_core(water)
```
Now in order to handle all the collisions and properties (like regulating water temperature and random neutron generation). We need have
Mechanic object attached to our Core
```python
mechanics = Mechanics(core)
```

Now it's time to go to our pygame loop and draw objects.
```python
def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.fill((255, 255, 255))
```
Now let's grab the water in our core and draw it. We draw the water only if it is not removed (evaporated) cause of high temperature.
```python
        for water in core.get_water_list():
            pos = water.get_body().position
            pos = int(pos.x), int(pos.y)
            if water.removed:
                pygame.draw.rect(display, (255, 255, 255), (pos[0] - water.length // 2, pos[1] - water.width // 2, water.length, water.width))
            else:
                pygame.draw.rect(display, (255, 80, 80), (pos[0] - water.length // 2, pos[1] - water.width // 2, water.length, water.width))
```
Similarly let's add fuel rod
```python
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
```
It is highly probable for a neutron to cause fission when it's speed is within a threshold to thermal speed.
These speeds are Vec2D and `neutron_body.velocity` is Vec2D and `neutrong_body.velocity.length` gives magnitude of the Vec2D.
```python
        # Get the neutron's current position (convert pymunk's coordinate system to pygame's)
        for neutron in core.get_neutron_list():
            pos = neutron.get_body().position
            pos = int(pos.x), int(pos.y)
            neutron_body = neutron.get_body()
            threshold = 0.5
            if (neutron_body.velocity.length - core.thermal_speed.length) <= threshold:
                # red color for thermal neutron
                pygame.draw.circle(display, (255, 0, 0), pos, neutron.get_radius())
            else:
                # red outline for slow neutron
                pygame.draw.circle(display, (255, 0, 0), pos, neutron.get_radius(), 2)
```
Adding Moderator and Control Rods (Allowing Control Rod to react to Keyboard Up and Down keys)
```python
        for moderator in core.get_moderator_list():
            pos = moderator.get_body().position
            pos = int(pos.x), int(pos.y)
            pygame.draw.rect(display, (0, 0, 0), (pos[0] - moderator.get_length() // 2, pos[1] - moderator.width // 2, moderator.get_length(), moderator.width), 1)

        keys = pygame.key.get_pressed()

        movement = 0
        if keys[pygame.K_UP]:
            movement = -1
        elif keys[pygame.K_DOWN]:
            movement = 1

        for control_rod in core.get_control_rod_list():

            control_rod.move_control_rod(movement)
            pos = control_rod.get_body().position
            pos = int(pos.x), int(pos.y)
            pygame.draw.rect(display, (128, 128, 128), (pos[0] - control_rod.get_length() // 2, pos[1] - control_rod.width // 2, control_rod.get_length(), control_rod.width))
```

Now it's time to update our simulation both pygame canvas as well as core simulation
```python
        pygame.display.update()
        clock.tick(FPS)

        # Run the physics simulation
        mechanics.generate_random_neutron(limit=0.08)
        mechanics.regulate_water_temperature()
        mechanics.regulate_fuel_element_occurence()

        # Step the physics simulation
        core.get_space().step(1 / FPS)
```
Calling the game function
```python
game()
pygame.quit()
```
![Sample](media/media_sample.gif)

Hence the complete code would kinda look this
```python
import pygame

from fissionmunk import Core
from fissionmunk import Moderator
from fissionmunk import ControlRod
from fissionmunk import Fuel
from fissionmunk import Water
from fissionmunk import Material

from fissionmunk import Mechanics

# Initialize Pygame
pygame.init()
display = pygame.display.set_mode((700, 600))
clock = pygame.time.Clock()
FPS = 60

# Create a core object
core = Core(length=700, width=600,thermal_factor=4, cold_factor=1, fast_factor=10)


moderator = Moderator(length=10, width=580, position=(600, 290), material=Material.GRAPHITE)
core.add_moderator_to_core(moderator)


control_rod = ControlRod(length=10, width=600, position=(500, 0), tag="E", movement_range=[20, 580],material=Material.BORON_CARBIDE)
core.add_control_rod_to_core(control_rod)

fuel_rod = Fuel(fuel_element_gap=10,uranium_occurance_probability=0.0001, xenon_occurance_probability=0.00001, xenon_decay_probability=0.00001, element_radius=10, width=560, position=(300, 25))
core.add_fuel_rod_to_core(fuel_rod)


for j in range(25, 580, 30):
    water = Water(length=25, width=25, position=(450, j), coolant=True, hard_limit=30, temperature_threshold=100, material=Material.WATER)
    core.add_water_to_core(water)

# Create a mechanics object
mechanics = Mechanics(core)

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.fill((255, 255, 255))

        for water in core.get_water_list():
            pos = water.get_body().position
            pos = int(pos.x), int(pos.y)
            if water.removed:
                pygame.draw.rect(display, (255, 255, 255), (pos[0] - water.length // 2, pos[1] - water.width // 2, water.length, water.width))
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

        keys = pygame.key.get_pressed()

        movement = 0
        if keys[pygame.K_UP]:
            movement = -1
        elif keys[pygame.K_DOWN]:
            movement = 1

        for control_rod in core.get_control_rod_list():

            control_rod.move_control_rod(movement)
            pos = control_rod.get_body().position
            pos = int(pos.x), int(pos.y)
            pygame.draw.rect(display, (128, 128, 128), (pos[0] - control_rod.get_length() // 2, pos[1] - control_rod.width // 2, control_rod.get_length(), control_rod.width))

        pygame.display.update()
        clock.tick(FPS)

        # Run the physics simulation
        mechanics.generate_random_neutron(limit=0.08)
        mechanics.regulate_water_temperature()
        mechanics.regulate_fuel_element_occurence()

        # Step the physics simulation
        core.get_space().step(1 / FPS)

game()
pygame.quit()
```

Congrats! You just made your first simulation using Fissionmunk.
Well even though it doesnt quite look like a reactor but you can play around with it add more control rods and moderators and it will start resembling close to a 2D representation of a nuclear reactor

### Documentation Overview
The following modules are included in FissionMunk and offer various simulation controls:

- **Core**: Manages the main simulation environment and fuel elements.
- **ControlRod**: Controls neutron absorption, allowing for fission rate adjustments.
- **Moderator**: Slows down neutrons to maintain optimal reaction rates.
- **FuelElement**: Represents fuel elements, such as uranium atoms, in the simulation.
- **Neutron**: Models individual neutrons and their interactions.

Refer to the full documentation for module-specific details and usage examples.

## Contributing

We welcome contributions to the FissionMunk project! If you'd like to contribute, please follow these steps:

1. **Fork** this repository to your own GitHub account.
2. **Create a new branch** from the `main` branch for your feature or fix. You can name the branch something descriptive, like `feature/your-feature-name`.
3. **Commit your changes** with clear and concise commit messages.
4. **Push your branch** to your forked repository.
5. **Open a pull request** (PR) to the main repository. Be sure to provide a description of the changes you've made.

### Major Changes
If you're planning on making a major change or addition, please **open an issue** first to discuss your ideas with the maintainers before starting on the implementation. This helps ensure that your changes align with the project's goals.

Thank you for contributing!

## License
[MIT License](LICENSE)
