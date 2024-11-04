import math
from objects.Neutron import Neutron
from objects.Fuel import FuelElement
from .Material import MaterialType as Material
class Mechanics:
    def __init__(self, core = None):
        self.core = core
        self.space = core.get_space()
        self.angle_offset = math.radians(20)

        # Set the collision handler for neutron and moderator
        NMC_handler = self.space.add_collision_handler(1, 2)
        NMC_handler.begin = self.neutron_moderator_collision

        # Collision handler for neutron and control rod
        NCRC_handler = self.space.add_collision_handler(1, 5)
        NCRC_handler.begin = self.neutron_control_rod_collision

        # Fuel element collision handler
        NFEC_handler = self.space.add_collision_handler(1, 3)
        NFEC_handler.begin = self.neutron_fuel_element_collision

    def neutron_moderator_collision(self, arbiter, space, data):
        try:
            neutron_shape, moderator_shape = arbiter.shapes
            # Get the neutron's speed

            neutron_shape.body.velocity = self.core.get_thermal_speed()

        except Exception as e:
            print(e)
        else:
            print("Moderator Collision detected")
            return True

    def neutron_control_rod_collision(self, arbiter, space, data):
        try:
            neutron_shape, control_rod_shape = arbiter.shapes

            neutron = Neutron.body_to_neutron[(neutron_shape.body, neutron_shape)]

            self.core.remove_neutron_from_core(neutron)

        except Exception as e:
            print(e)
        else:
            print("Control Rod Collision detected")
            return True

    def neutron_fuel_element_collision(self, arbiter, space, data):
        try:
            neutron_shape, fuel_element_shape = arbiter.shapes
            neutron = Neutron.body_to_neutron[(neutron_shape.body, neutron_shape)]

            fuel_element = FuelElement.body_to_fuel_element[(fuel_element_shape.body, fuel_element_shape)]

            neutron_velocity = neutron.body.velocity
            # Check if the neutron is a thermal neutron by checking it's translational speed



            if neutron_velocity.x != 0:
                fuel_element.set_material(Material.NON_FISSILE)

                old_speed = neutron.body.velocity
                x = old_speed.x * math.cos(self.angle_offset) - old_speed.y * math.sin(self.angle_offset)
                y = old_speed.x * math.sin(self.angle_offset) + old_speed.y * math.cos(self.angle_offset)

                new_speed_n1 = (x, y)
                new_speed_n2 = (x, -y)

                neutron1 = Neutron(speed=new_speed_n1, position=neutron.get_position(), mass=neutron.get_mass(), radius=neutron.get_radius())
                neutron2 = Neutron(speed=new_speed_n2, position=neutron.get_position(), mass=neutron.get_mass(), radius=neutron.get_radius())

                self.core.add_neutron_to_core(neutron1)
                self.core.add_neutron_to_core(neutron2)

                self.core.remove_neutron_from_core(neutron)
        except Exception as e:
            print(e)
        else:
            print("Fuel Element Collision detected")
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