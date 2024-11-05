import math
import pymunk
import random
from objects.Neutron import Neutron
from objects.Fuel import FuelElement
from .Material import MaterialType as Material
class Mechanics:
    def __init__(self, core = None):
        self.core = core
        self.space = core.get_space()
        self.angle_offset = math.radians(30)

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

    def neutron_moderator_collision(self, arbiter, space, data):
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
        except Exception as e:
            print(e)
        else:
            return True

    def neutron_control_rod_collision(self, arbiter, space, data):
        try:
            neutron_shape, control_rod_shape = arbiter.shapes

            neutron = Neutron.body_to_neutron[(neutron_shape.body, neutron_shape)]

            self.core.remove_neutron_from_core(neutron)

        except Exception as e:
            print(e)
        else:
            return True

    def neutron_fuel_element_collision(self, arbiter, space, data):
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

                if random.random() < 0.3:
                    new_speed_n3 = -direction * fast_speed_magnitude
                    neutron3 = Neutron(speed=new_speed_n3, position=neutron.get_position(), mass=neutron.get_mass(), radius=neutron.get_radius())
                    self.core.add_neutron_to_core(neutron3)

                self.core.add_neutron_to_core(neutron1)
                self.core.add_neutron_to_core(neutron2)

                self.core.remove_neutron_from_core(neutron)
        except Exception as e:
            print(e)
        else:
            return True

    def neutron_xenon_collision(self, arbiter, space, data):
        try:
            neutron_shape, xenon_shape = arbiter.shapes
            current_velocity = neutron_shape.body.velocity

            if abs(current_velocity.length - self.core.thermal_speed.length) < 0.5:
                neutron = Neutron.body_to_neutron[(neutron_shape.body, neutron_shape)]
                xenon = FuelElement.body_to_fuel_element[(xenon_shape.body, xenon_shape)]
                self.core.remove_neutron_from_core(neutron)
                xenon.set_material(Material.NON_FISSILE)
        except Exception as e:
            print(e)
        else:
            return True


    # Getters and Setters
    def get_space(self):
        return self.space

    def set_space(self, space):
        try:
            self.space = space
        except Exception as e:
            print(e)
        else:
            print("Space set successfully")

    def get_core(self):
        return self.core

    def set_core(self, core):
        try:
            self.core = core
            self.space = core.get_space()
        except Exception as e:
            print(e)
        else:
            print("Core set successfully")