# Neutron class
import pymunk

class Neutron:
    """This class represents a neutron in the simulation.
    """
    body_to_neutron = {}

    # Constructor
    def __init__(self, speed, position, mass=0.1, radius=1):
        """This method initializes the neutron object.

        :param speed: The speed of the neutron.
        :type speed: tuple
        :param position: The position of the neutron.
        :type position: tuple
        :param mass: The mass of the neutron, defaults to 0.1
        :type mass: float, optional
        :param radius: The radius of the neutron, defaults to 1
        :type radius: int, optional
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
        """This method creates a neutron object.

        :return: The body and shape of the neutron.
        :rtype: tuple
        """
        circle_body = pymunk.Body(self.mass, self.initialize_moment_inertia(), pymunk.Body.DYNAMIC)
        circle_shape = pymunk.Circle(circle_body, self.radius)
        return circle_body, circle_shape

    def remove_neutron(self):
        """This method removes the neutron from the simulation.

        :return: True if the neutron is removed, False otherwise.
        :rtype: bool
        """
        try:
            self.body_to_neutron.pop((self.body, self.shape))
        except Exception as e:
            # print(e)
            pass
        else:
            return True

    def initialize_moment_inertia(self):
        """This method initializes the moment of inertia of the neutron.

        :return: The moment of inertia of the neutron.
        :rtype: float
        """
        circle_moment_inertia = pymunk.moment_for_circle(self.mass, 0, self.radius)
        return circle_moment_inertia

    def get_speed(self):
        """This method returns the speed of the neutron.

        :return: The speed of the neutron.
        :rtype: tuple
        """
        return self.body.velocity

    def set_speed(self, speed):
        """This method sets the speed of the neutron.

        :param speed: The speed of the neutron.
        :type speed: tuple
        :return: None
        :rtype: None
        """

        try:
            self.body.velocity = speed
            return None
        except Exception as e:
            # print(e)
            pass

    def get_position(self):
        """This method returns the position of the neutron.

        :return: The position of the neutron.
        :rtype: tuple
        """
        return self.body.position

    def set_position(self, position):
        """This method sets the position of the neutron.

        :param position: The position of the neutron.
        :type position: tuple
        :return: None
        :rtype: None
        """
        self.body.position = position
        return None
    def get_mass(self):
        """This method returns the mass of the neutron.

        :return: The mass of the neutron.
        :rtype: float
        """
        return self.mass

    def get_radius(self):
        """This method returns the radius of the neutron.

        :return: The radius of the neutron.
        :rtype: int
        """
        return self.radius

    def get_body(self):
        """This method returns the body of the neutron.

        :return: The body of the neutron.
        :rtype: pymunk.Body
        """
        return self.body

    def get_shape(self):
        """This method returns the shape of the neutron.

        :return: The shape of the neutron.
        :rtype: pymunk.Shape
        """
        return self.shape
