from objects.Neutron import Neutron
class Mechanics:
    def __init__(self, core = None):
        self.core = core
        self.space = core.get_space()

        # Set the collision handler for neutron and moderator
        NMC_handler = self.space.add_collision_handler(1, 2)
        NMC_handler.begin = self.neutron_moderator_collision

        # Collision handler for neutron and control rod
        NCRC_handler = self.space.add_collision_handler(1, 5)
        NCRC_handler.begin = self.neutron_control_rod_collision


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