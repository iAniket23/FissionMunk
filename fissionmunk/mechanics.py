import math
import random
import pymunk
from .Neutron import Neutron
from .Water import Water
from .FuelElement import FuelElement
from .Fuel import Fuel
from .Material import MaterialType as Material
from .helper import get_probability
# Mechanics class
class Mechanics:
    """The Mechanics class is responsible for handling the physics of the simulation.
    """
    def __init__(self, core = None):
        """The constructor for the Mechanics class.

        :param core: The core object, defaults to None
        :type core: Core, optional
        """
        self.core = core
        self.space = core.get_space()
        self.angle_offset = math.radians(30)
        self.water_absorption = 0.05

        # Set the collision handler for neutron and moderator
        NMC_handler = self.space.add_collision_handler(1, 2)
        NMC_handler.begin = self.neutron_moderator_collision

        # Collision handler for neutron and control rod
        NCRC_handler = self.space.add_collision_handler(1, 5)
        NCRC_handler.begin = self.neutron_control_rod_collision

        # Fuel element collision handler
        NFEC_handler = self.space.add_collision_handler(1, 3)
        NFEC_handler.begin = self.neutron_fuel_element_collision

        # Xenon collision handler
        NX_handler = self.space.add_collision_handler(1, 8)
        NX_handler.begin = self.neutron_xenon_collision

        # Boundary collision handler
        NB_handler = self.space.add_collision_handler(1, 10)
        NB_handler.begin = self.neutron_boundary_collision
        NB_handler.separate = self.neutron_boundary_collision

        NW_handler = self.space.add_collision_handler(1, 11)
        NW_handler.begin = self.neutron_water_collision_add
        NW_handler.separate = self.neutron_water_collision_remove

    def neutron_water_collision_add(self, arbiter, space, data):
        """The method to handle neutron-water collision

        :param arbiter: arbiter object
        :type arbiter: Arbiter
        :param space: space object
        :type space: Space
        :param data: data object
        :type data: Data
        :return: True if successful, False otherwise
        :rtype: bool
        """
        try:
            prob = get_probability()
            neutron_shape, water_shape = arbiter.shapes
            if prob < self.water_absorption:
                neutron = Neutron.body_to_neutron[(neutron_shape.body, neutron_shape)]
                neutron.remove_neutron()
                self.core.remove_neutron_from_core(neutron)

            water = Water.body_to_water[(water_shape.body, water_shape)]
            water.increase_number_of_neutrons_interacting()

            water.change_temperature(20)

            return True

        except Exception as e:
            return False

    def neutron_water_collision_remove(self, arbiter, space, data):
        """The method to handle neutron-water collision

        :param arbiter: arbiter object
        :type arbiter: Arbiter
        :param space: space object
        :type space: Space
        :param data: data object
        :type data: Data
        :return: True if successful, False otherwise
        :rtype: bool
        """
        try:
            neutron_shape, water_shape = arbiter.shapes
            water = Water.body_to_water[(water_shape.body, water_shape)]
            water.decrease_number_of_neutrons_interacting()
            return True
        except Exception as e:
            return False

    def regulate_water_temperature(self):
        """The method to regulate the water temperature

        :return: None
        :rtype: None
        """
        for water in self.core.get_water_list():
            water.change_temperature(-0.5)
        return None

    def regulate_fuel_element_occurence(self):
        """The method to regulate the fuel element occurence

        :return: None
        :rtype: None
        """
        for fuel_rod in self.core.get_fuel_rod_list():
            for fuel_element in fuel_rod.get_fuel_elements():
                fuel_element.change_material()
        return None

    def neutron_boundary_collision(self, arbiter, space, data):
        """The method to handle neutron-boundary collision

        :param arbiter: arbiter object
        :type arbiter: Arbiter
        :param space: space object
        :type space: Space
        :param data: data object
        :type data: Data
        :return: True if successful, False otherwise
        :rtype: bool
        """
        try:
            neutron_shape, boundary_shape = arbiter.shapes
            neutron = Neutron.body_to_neutron[(neutron_shape.body, neutron_shape)]
            neutron.remove_neutron()
            self.core.remove_neutron_from_core(neutron)
            return True

        except Exception as e:
            # print(e)
            return False

    def neutron_moderator_collision(self, arbiter, space, data):
        """The method to handle neutron-moderator collision

        :param arbiter: arbiter object
        :type arbiter: Arbiter
        :param space: space object
        :type space: Space
        :param data: data object
        :type data: Data
        :return: True if successful, False otherwise
        :rtype: bool
        """
        try:
            neutron_shape, moderator_shape = arbiter.shapes
            # Get the neutron's speed
            current_velocity = neutron_shape.body.velocity

            if abs(current_velocity.length - self.core.fast_speed.length) < 0.5:
                # Get the collision normal, which represents the moderator surface at the collision point
                collision_normal = arbiter.contact_point_set.normal

                # Calculate the reflection of the current velocity across the collision normal
                dot_product = current_velocity.dot(collision_normal)
                reflected_direction = current_velocity - 2 * dot_product * collision_normal
                reflected_direction = reflected_direction.normalized()  # Normalize to get direction only

                # Set the reflected direction to thermal speed
                thermal_speed_magnitude = self.core.thermal_speed.length
                new_velocity = reflected_direction * thermal_speed_magnitude

                # Apply the new velocity to the neutron
                neutron_shape.body.velocity = new_velocity
            return True
        except Exception as e:
            # print(e)
            return False

    def neutron_control_rod_collision(self, arbiter, space, data):
        """The method to handle neutron-control rod collision

        :param arbiter: arbiter object
        :type arbiter: Arbiter
        :param space: space object
        :type space: Space
        :param data: data object
        :type data: Data
        :return: True if successful, False otherwise
        :rtype: bool
        """
        try:
            neutron_shape, control_rod_shape = arbiter.shapes

            neutron = Neutron.body_to_neutron[(neutron_shape.body, neutron_shape)]
            neutron.remove_neutron()
            self.core.remove_neutron_from_core(neutron)

            return True

        except Exception as e:
            # print(e)
            return False

    def neutron_fuel_element_collision(self, arbiter, space, data):
        """The method to handle neutron-fuel element collision

        :param arbiter: arbiter object
        :type arbiter: Arbiter
        :param space: space object
        :type space: Space
        :param data: data object
        :type data: Data
        :return: True if successful, False otherwise
        :rtype: bool
        """
        try:
            neutron_shape, fuel_element_shape = arbiter.shapes
            neutron = Neutron.body_to_neutron[(neutron_shape.body, neutron_shape)]

            fuel_element = FuelElement.body_to_fuel_element[(fuel_element_shape.body, fuel_element_shape)]

            neutron_velocity = neutron.body.velocity

            neutron_speed = neutron_velocity.length

            threshold = 0.5

            if abs(neutron_speed - self.core.thermal_speed.length) <= threshold:
                fuel_element.set_material(Material.NON_FISSILE)
                # Original direction
                direction = neutron_velocity.normalized()

                # Small angle offset in radians for deviation (5 degrees)
                small_angle_offset = self.angle_offset

                # Calculate the two slightly different directions
                x1 = direction.x * math.cos(small_angle_offset) - direction.y * math.sin(small_angle_offset)
                y1 = direction.x * math.sin(small_angle_offset) + direction.y * math.cos(small_angle_offset)
                new_direction_n1 = pymunk.Vec2d(x1, y1)

                x2 = direction.x * math.cos(-small_angle_offset) - direction.y * math.sin(-small_angle_offset)
                y2 = direction.x * math.sin(-small_angle_offset) + direction.y * math.cos(-small_angle_offset)
                new_direction_n2 = pymunk.Vec2d(x2, y2)

                # Set the new speed for both directions to fast speed
                fast_speed_magnitude = self.core.fast_speed.length
                new_speed_n1 = new_direction_n1 * fast_speed_magnitude
                new_speed_n2 = new_direction_n2 * fast_speed_magnitude

                neutron1 = Neutron(speed=new_speed_n1, position=neutron.get_position(), mass=neutron.get_mass(), radius=neutron.get_radius())
                neutron2 = Neutron(speed=new_speed_n2, position=neutron.get_position(), mass=neutron.get_mass(), radius=neutron.get_radius())

                if get_probability() < 0.5:
                    new_speed_n3 = -direction * fast_speed_magnitude
                    neutron3 = Neutron(speed=new_speed_n3, position=neutron.get_position(), mass=neutron.get_mass(), radius=neutron.get_radius())
                    self.core.add_neutron_to_core(neutron3)

                self.core.add_neutron_to_core(neutron1)
                self.core.add_neutron_to_core(neutron2)

                neutron.remove_neutron()
                self.core.remove_neutron_from_core(neutron)

            return True

        except Exception as e:
            # print(e)
            return False

    def neutron_xenon_collision(self, arbiter, space, data):
        """The method to handle neutron-xenon collision

        :param arbiter: arbiter object
        :type arbiter: Arbiter
        :param space: space object
        :type space: Space
        :param data: data object
        :type data: Data
        :return: True if successful, False otherwise
        :rtype: bool
        """
        try:
            neutron_shape, xenon_shape = arbiter.shapes
            current_velocity = neutron_shape.body.velocity

            if abs(current_velocity.length - self.core.thermal_speed.length) < 0.5:
                neutron = Neutron.body_to_neutron[(neutron_shape.body, neutron_shape)]
                xenon = FuelElement.body_to_fuel_element[(xenon_shape.body, xenon_shape)]
                neutron.remove_neutron()
                self.core.remove_neutron_from_core(neutron)
                xenon.set_material(Material.NON_FISSILE)

            return True
        except Exception as e:
            return False

    def generate_random_neutron(self, limit):
        """The method to generate a random neutron

        :param limit: The limit for the probability
        :type limit: float
        :return: The neutron object if successful, False otherwise
        :rtype: Neutron
        """
        try:
            prob = get_probability()
            if prob < limit:
                neutron_speed = self.core.thermal_speed
                random_angle = random.uniform(0, 2 * math.pi)
                x = math.cos(random_angle)
                y = math.sin(random_angle)
                new_direction = pymunk.Vec2d(x, y)
                neutron_speed = new_direction * neutron_speed.length
                neutron_position = (random.uniform(0, self.core.length), random.uniform(0, self.core.width))
                neutron = Neutron(speed=neutron_speed, position=neutron_position, mass=0.1, radius=5)
                self.core.add_neutron_to_core(neutron)
            return True
        except Exception as e:
            # print(e)
            return False