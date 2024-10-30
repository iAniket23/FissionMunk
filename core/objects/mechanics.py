# Nuclear Physics mechanics module
# Speed of neutron
# Probability
# Absorption

class Mechanics:
    def __init__(self, core = None):
        self.core = core
        self.space = core.get_space()

        # Set the collision handler for neutron and moderator
        NMC_handler = self.space.add_collision_handler(1, 2)
        NMC_handler.begin = self.neutron_moderator_collision

    def neutron_moderator_collision(self, arbiter, space, data):
        try:
            neutron_body, moderator_body = arbiter.shapes
            # Get the neutron's speed
            neutron_body.body.velocity = self.core.get_thermal_speed()

        except Exception as e:
            print(e)
        else:
            print("Collision detected")
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