# Neutron class
import pymunk

class Neutron:
    """
        This class creates a neutron object.
    """
    body_to_neutron = {}

    # Constructor
    def __init__(self, speed, position, mass=0.1, radius=1):
        """
            Initializes the neutron object.

            Args:
                speed (tuple):
                    The speed of the neutron.
                position (tuple):
                    The position of the neutron.
                mass (float):
                    The mass of the neutron.
                radius (float):
                    The radius of the neutron.

            Returns:
                None
        """
        self.mass = mass
        self.radius = radius

        self.body, self.shape = self.create_neutron()
        self.body.position = position
        self.body.velocity = speed

        self.shape.collision_type = 1
        self.shape.sensor = True

        Neutron.body_to_neutron[(self.body, self.shape)] = self

    # Create a neutron object
    def create_neutron(self):
        """
            Creates a neutron.
            This method is not public.

            Returns:
                circle_body (pymunk.Body):
                    The body of the neutron.
                circle_shape (pymunk.Circle):
                    The shape of the neutron.
        """
        circle_body = pymunk.Body(self.mass, self.initialize_moment_inertia(), pymunk.Body.DYNAMIC)
        circle_shape = pymunk.Circle(circle_body, self.radius)
        return circle_body, circle_shape

    def remove_neutron(self):
        """
            Removes the neutron from the simulation.

            Returns:
                True (bool):
                    If the neutron is removed successfully.

                False (bool):
                    If the neutron is not removed successfully
        """
        try:
            self.body_to_neutron.pop((self.body, self.shape))
        except Exception as e:
            # print(e)
            pass
        else:
            return True

    def initialize_moment_inertia(self):

        """
            Initializes the moment of inertia of the neutron.

            Returns:
                circle_moment_inertia (float):
                    The moment of inertia of the neutron.
        """
        circle_moment_inertia = pymunk.moment_for_circle(self.mass, 0, self.radius)
        return circle_moment_inertia

    def get_speed(self):
        """
            Returns the speed of the neutron.

            Returns:
                self.body.velocity (tuple):
                    The speed of the neutron.
        """
        return self.body.velocity

    def set_speed(self, speed):
        """
            Sets the speed of the neutron.

            Args:
                speed (tuple):
                    The speed of the neutron.

            Returns:
                None
        """
        try:
            self.body.velocity = speed

        except Exception as e:
            # print(e)
            pass

    def get_position(self):
        """
            Returns the position of the neutron.

            Returns:
                self.body.position (tuple):
                    The position of the neutron.
        """
        return self.body.position

    def set_position(self, position):
        """
            Sets the position of the neutron.

            Args:
                position (tuple):
                    The position of the neutron.

            Returns:
                None
        """
        self.body.position = position

    def get_mass(self):
        """
            Returns the mass of the neutron.

            Returns:
                self.mass (float):
                    The mass of the neutron
        """
        return self.mass

    def get_radius(self):
        """
            Returns the radius of the neutron.

            Returns:
                self.radius (float):
                    The radius of the neutron.
        """
        return self.radius

    def get_body(self):
        """
            Returns the body of the neutron.

            Returns:
                self.body (pymunk.Body):
                    The body of the neutron.
        """
        return self.body

    def get_shape(self):
        """
            Returns the shape of the neutron.

            Returns:
                self.shape (pymunk.Circle):
                    The shape of the neutron.
        """
        return self.shape
