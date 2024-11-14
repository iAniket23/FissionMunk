# FissionMunk

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PyPI version](https://badge.fury.io/py/fissionmunk.svg)
[![API Reference](https://img.shields.io/badge/API%20Reference-Docs-blue)](https://ianiket23.github.io/FissionMunk/)

**FissionMunk** is a lightweight 2D physics open source python library designed to simulate nuclear fission reactor mechanics. It enables users to visualize interactions between neutrons and uranium atoms, providing valuable insights into fission dynamics with customizable parameters, such as neutron occurrence probabilities, moderators, and control rods. FissionMunk is ideal for educational simulations, nuclear physics research, and interactive demos, and is built on top of the [Pymunk](http://www.pymunk.org/) library.

2024, Aniket Mishra - [ianiket23@github.io](https://ianiket23.github.io/)

- Documentation: [https://ianiket23.github.io/FissionMunk/](https://ianiket23.github.io/FissionMunk/)
- Source code: [https://github.com/iAniket23/fissionmunk](https://github.com/iAniket23/fissionmunk)  
- Bug reports: [https://github.com/iAniket23/fissionmunk/issues](https://github.com/iAniket23/fissionmunk/issues)  

## Features
- Interactive Simulation: Visualize neutron interactions with uranium in real-time, with configurable parameters.
- Modularity: Use customizable modules to add moderators, control rods, and other reactor elements.
- Educational Tool: Ideal for students and educators to explore nuclear fission mechanics.
- Open-Source: Fully open-source and extensible for customization and additional functionality.

## Getting Started with FissionMunk
FissionMunk makes it easy to simulate and visualize nuclear fission dynamics. To get started, follow these steps:

### Installation

To install FissionMunk, use `pip`:
```bash
pip install fissionmunk
```
### Set Up Your First Simulation
Now that you’ve installed FissionMunk, let's create a basic simulation. Here's an example to help you get started:

#### Example: Basic Fission Simulation
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
```python
# Initialize Pygame
pygame.init()
display = pygame.display.set_mode((700, 600))
clock = pygame.time.Clock()
FPS = 60
```

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
