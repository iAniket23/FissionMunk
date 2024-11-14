# Core class
import pymunk

class Core:
    """The Core class is used to create the core of the reactor.
    """
    def __init__(self, length, width, neutron_speed = (40, 0), thermal_factor = 50, cold_factor = 10, fast_factor = 100):
        """The constructor of the Core class.

        :param length: The length of the core.
        :type length: float
        :param width: The width of the core.
        :type width: float
        :param neutron_speed: The speed of the neutron, defaults to (40, 0)
        :type neutron_speed: tuple, optional
        :param thermal_factor: factor to multiply the neutron speed to get the thermal speed, defaults to 50
        :type thermal_factor: int, optional
        :param cold_factor: factor to multiply the neutron speed to get the cold speed, defaults to 10
        :type cold_factor: int, optional
        :param fast_factor: factor to multiply the neutron speed to get the fast speed, defaults to 100
        :type fast_factor: int, optional
        """
        self.length = length
        self.width = width

        # Neutron speed
        self.fast_speed = pymunk.Vec2d(neutron_speed[0], neutron_speed[1]) * fast_factor
        self.thermal_speed = pymunk.Vec2d(neutron_speed[0], neutron_speed[1]) * thermal_factor
        self.cold_speed = pymunk.Vec2d(neutron_speed[0], neutron_speed[1]) * cold_factor

        # Space
        self.space = pymunk.Space()

        # Lists of objects in the core
        self.neutron_list = []
        self.moderator_list = []
        self.control_rod_list = []
        self.fuel_rod_list = []
        self.water_list = []

        # Create core boundaries
        self.create_core_boundaries()

    # Create core boundaries
    def create_core_boundaries(self):
        """The method is used to create the core boundaries.

        :return: None
        :rtype: None
        """
        # Create the core boundaries
        core_boundaries = [pymunk.Segment(self.space.static_body, (0, 0), (0, self.width), 1),
                           pymunk.Segment(self.space.static_body, (0, self.width), (self.length, self.width), 1),
                           pymunk.Segment(self.space.static_body, (self.length, self.width), (self.length, 0), 1),
                           pymunk.Segment(self.space.static_body, (self.length, 0), (0, 0), 1)]
        for boundary in core_boundaries:
            boundary.collision_type = 10
            self.space.add(boundary)
        return None

    # Add and remove neutron from the core
    def add_neutron_to_core(self, neutron):
        """The method is used to add the neutron to the core.

        :param neutron: The neutron object to be added to the core.
        :type neutron: Neutron
        :return: None
        :rtype: None
        """
        self.space.add(neutron.get_body(), neutron.get_shape())
        self.neutron_list.append(neutron)

        return None

    def remove_neutron_from_core(self, neutron):
        """The method is used to remove the neutron from the core.

        :param neutron: The neutron object to be removed from the core.
        :type neutron: Neutron
        :return: None
        :rtype: None
        """
        self.space.remove(neutron.get_body(), neutron.get_shape())
        self.neutron_list.remove(neutron)
        neutron.remove_neutron()
        return None

    def add_water_to_core(self, water):
        """The method is used to add the water to the core.

        :param water: The water object to be added to the core.
        :type water: Water
        :return: None
        :rtype: None
        """
        self.space.add(water.get_body(), water.get_shape())
        self.water_list.append(water)

        return None

    def remove_water_from_core(self, water):
        """The method is used to remove the water from the core.

        :param water: The water object to be removed from the core.
        :type water: Water
        :return: None
        :rtype: None
        """
        self.space.remove(water.get_body(), water.get_shape())
        self.water_list.remove(water)

        return None

    # Add and remove moderator from the core
    def add_moderator_to_core(self, moderator):
        """The method is used to add the moderator to the core.

        :param moderator: The moderator object to be added to the core.
        :type moderator: Moderator
        """
        self.space.add(moderator.get_body(), moderator.get_shape())
        self.moderator_list.append(moderator)
        return None

    def remove_moderator_from_core(self, moderator):
        """The method is used to remove the moderator from the core.

        :param moderator: The moderator object to be removed from the core.
        :type moderator: Moderator
        :return: None
        :rtype: None
        """
        self.space.remove(moderator.get_body(), moderator.get_shape())
        self.moderator_list.remove(moderator)
        return None
    # Add and remove control rod from the core
    def add_control_rod_to_core(self, control_rod):
        """The method is used to add the control rod to the core.

        :param control_rod: The control rod object to be added to the core.
        :type control_rod: ControlRod
        :return: None
        :rtype: None
        """
        self.space.add(control_rod.get_body(), control_rod.get_shape())
        self.control_rod_list.append(control_rod)
        return None

    def remove_control_rod_from_core(self, control_rod):
        """The method is used to remove the control rod from the core.

        :param control_rod: The control rod object to be removed from the core.
        :type control_rod: ControlRod
        :return: None
        :rtype: None
        """
        self.space.remove(control_rod.get_body(), control_rod.get_shape())
        self.control_rod_list.remove(control_rod)
        return None
    # Add and remove fuel rod from the core
    def add_fuel_rod_to_core(self, fuel_rod):
        """The method is used to add the fuel rod to the core.

        :param fuel_rod: The fuel rod object to be added to the core.
        :type fuel_rod: FuelRod
        :return: None
        :rtype: None
        """
        for fuel_element in fuel_rod.get_fuel_elements():
            self.space.add(fuel_element.get_body(), fuel_element.get_shape())
            self.fuel_rod_list.append(fuel_rod)

        return None

    def remove_fuel_rod_from_core(self, fuel_rod):
        """The method is used to remove the fuel rod from the core.

        :param fuel_rod: The fuel rod object to be removed from the core.
        :type fuel_rod: FuelRod
        :return: None
        :rtype: None
        """
        for fuel_element in fuel_rod.get_fuel_elements():
            self.space.remove(fuel_element.get_body(), fuel_element.get_shape())
            self.fuel_rod_list.remove(fuel_rod)
        return None
    # Getters and setters
    def get_water_list(self):
        """The method is used to get the list of water in the core.

        :return: water_list
        :rtype: list
        """
        return self.water_list

    def get_neutron_list(self):
        """The method is used to get the list of neutron in the core.

        :return: neutron_list
        :rtype: list
        """
        return self.neutron_list

    def get_moderator_list(self):
        """The method is used to get the list of moderator in the core.

        :return: moderator_list
        :rtype: list
        """
        return self.moderator_list

    def get_control_rod_list(self):
        """The method is used to get the list of control rod in the core.

        :return: control_rod_list
        :rtype: list
        """
        return self.control_rod_list

    def get_fuel_rod_list(self):
        """The method is used to get the list of fuel rod in the core.

        :return: fuel_rod_list
        :rtype: list
        """
        return self.fuel_rod_list

    def get_space(self):
        """The method is used to get the space of the core.

        :return: space
        :rtype: pymunk.Space
        """
        return self.space

    def set_fast_speed(self, speed):
        """This method is used to set the fast speed of the neutron.

        :param speed: The speed of the neutron.
        :type speed: tuple
        :return: None
        :rtype: None
        """
        self.fast_speed = speed
        return None
    def get_fast_speed(self):
        """This method is used to get the fast speed of the neutron.

        :return: fast_speed
        :rtype: tuple
        """
        return self.fast_speed

    def get_thermal_speed(self):
        """This method is used to get the thermal speed of the neutron.

        :return: thermal_speed
        :rtype: tuple
        """
        return self.thermal_speed

    def get_cold_speed(self):
        """This method is used to get the cold speed of the neutron.

        :return: cold_speed
        :rtype: tuple
        """
        return self.cold_speed

    def set_thermal_speed(self, speed):
        """This method is used to set the thermal speed of the neutron.

        :param speed: The speed of the neutron.
        :type speed: tuple
        :return: None
        :rtype: None
        """
        self.thermal_speed = speed
        return None

    def set_cold_speed(self, speed):
        """This method is used to set the cold speed of the neutron.

        :param speed: The speed of the neutron.
        :type speed: tuple
        :return: None
        :rtype: None
        """
        self.cold_speed = speed
        return None