# Core class
import pymunk

class Core:
    """
        The class is used to create a core object.
        Core is the main object of the simulation. It contains all the objects that are used in the simulation.
    """
    def __init__(self, length, width, neutron_speed = (40, 0), thermal_factor = 50, cold_factor = 10, fast_factor = 100):
        """
            The method is used to initialize the Core object.

            Args:
                length: int
                    The length of the core.
                width: int
                    The width of the core.
                neutron_speed: tuple
                    The speed of the neutron.
                thermal_factor: int
                    The factor to multiply the neutron speed to get the thermal speed.
                cold_factor: int
                    The factor to multiply the neutron speed to get the cold speed.
                fast_factor: int
                    The factor to multiply the neutron speed to get the fast speed.
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
        """
            The method is used to create the core boundaries.
            This is not a public method.
        """
        # Create the core boundaries
        core_boundaries = [pymunk.Segment(self.space.static_body, (0, 0), (0, self.width), 1),
                           pymunk.Segment(self.space.static_body, (0, self.width), (self.length, self.width), 1),
                           pymunk.Segment(self.space.static_body, (self.length, self.width), (self.length, 0), 1),
                           pymunk.Segment(self.space.static_body, (self.length, 0), (0, 0), 1)]
        for boundary in core_boundaries:
            boundary.collision_type = 10
            self.space.add(boundary)

    # Add and remove neutron from the core
    def add_neutron_to_core(self, neutron):
        """
            The method is used to add the neutron to the core.

            Args:
                neutron: Neutron
                    The neutron object to be added to the core.

            Returns:
                None
        """
        self.space.add(neutron.get_body(), neutron.get_shape())
        self.neutron_list.append(neutron)

    def remove_neutron_from_core(self, neutron):
        """
            The method is used to remove the neutron from the core.

            Args:
                neutron: Neutron
                    The neutron object to be removed from the core.

            Returns:
                None
        """
        self.space.remove(neutron.get_body(), neutron.get_shape())
        self.neutron_list.remove(neutron)
        neutron.remove_neutron()

    def add_water_to_core(self, water):
        """
            The method is used to add the water to the core.

            Args:
                water: Water
                    The water object to be added to the core.

            Returns:
                None
        """
        self.space.add(water.get_body(), water.get_shape())
        self.water_list.append(water)

    def remove_water_from_core(self, water):
        """
            The method is used to remove the water from the core.

            Args:
                water: Water
                    The water object to be removed from the core.

            Returns:
                None
        """
        self.space.remove(water.get_body(), water.get_shape())
        self.water_list.remove(water)

    # Add and remove moderator from the core
    def add_moderator_to_core(self, moderator):
        """
            The method is used to add the moderator to the core.

            Args:
                moderator: Moderator
                    The moderator object to be added to the core.

            Returns:
                None
        """
        self.space.add(moderator.get_body(), moderator.get_shape())
        self.moderator_list.append(moderator)


    def remove_moderator_from_core(self, moderator):
        """
            The method is used to remove the moderator from the core.

            Args:
                moderator: Moderator
                    The moderator object to be removed from the core.

            Returns:
                None
        """
        self.space.remove(moderator.get_body(), moderator.get_shape())
        self.moderator_list.remove(moderator)

    # Add and remove control rod from the core
    def add_control_rod_to_core(self, control_rod):
        """
            The method is used to add the control rod to the core.

            Args:
                control_rod: ControlRod
                    The control rod object to be added to the core.

            Returns:
                None
        """
        self.space.add(control_rod.get_body(), control_rod.get_shape())
        self.control_rod_list.append(control_rod)


    def remove_control_rod_from_core(self, control_rod):
        """
            The method is used to remove the control rod from the core.

            Args:
                control_rod: ControlRod
                    The control rod object to be removed from the core.

            Returns:
                None
        """
        self.space.remove(control_rod.get_body(), control_rod.get_shape())
        self.control_rod_list.remove(control_rod)

    # Add and remove fuel rod from the core
    def add_fuel_rod_to_core(self, fuel_rod):
        """
            The method is used to add the fuel rod to the core.

            Args:
                fuel_rod: FuelRod
                    The fuel rod object to be added to the core.

            Returns:
                None
        """
        for fuel_element in fuel_rod.get_fuel_elements():
            self.space.add(fuel_element.get_body(), fuel_element.get_shape())
            self.fuel_rod_list.append(fuel_rod)

    def remove_fuel_rod_from_core(self, fuel_rod):
        """
            The method is used to remove the fuel rod from the core.

            Args:
                fuel_rod: FuelRod
                    The fuel rod object to be removed from the core.

            Returns:
                None
        """
        for fuel_element in fuel_rod.get_fuel_elements():
            self.space.remove(fuel_element.get_body(), fuel_element.get_shape())
            self.fuel_rod_list.remove(fuel_rod)

    # Getters and setters
    def get_water_list(self):
        """
            The method is used to get the list of water in the core.

            Returns:
                water_list: list
                    The list of water in the core.
        """
        return self.water_list

    def get_neutron_list(self):
        """
            The method is used to get the list of neutron in the core.

            Returns:
                neutron_list: list
                    The list of neutron in the core.
        """
        return self.neutron_list

    def get_moderator_list(self):
        """
            The method is used to get the list of moderator in the core.

            Returns:
                moderator_list: list
                    The list of moderator in the core.
        """
        return self.moderator_list

    def get_control_rod_list(self):
        """
            The method is used to get the list of control rod in the core.

            Returns:
                control_rod_list: list
                    The list of control rod in the core.
        """
        return self.control_rod_list

    def get_fuel_rod_list(self):
        """
            The method is used to get the list of fuel rod in the core.

            Returns:
                fuel_rod_list: list
                    The list of fuel rod in the core.

        """
        return self.fuel_rod_list

    def get_space(self):
        """
            The method is used to get the space of the core.

            Returns:
                space: pymunk.Space
                    The space of the core.
        """
        return self.space

    def set_fast_speed(self, speed):
        """
            The method is used to set the fast speed of the neutron.

            Args:
                speed: tuple
                    The speed of the neutron.
        """
        self.fast_speed = speed

    def get_fast_speed(self):
        """
            The method is used to get the fast speed of the neutron.

            Returns:
                fast_speed: tuple
                    The speed of the neutron.
        """
        return self.fast_speed

    def get_thermal_speed(self):
        """
            The method is used to get the thermal speed of the neutron.

            Returns:
                thermal_speed: tuple
                    The speed of the neutron.
        """
        return self.thermal_speed

    def get_cold_speed(self):
        """
            The method is used to get the cold speed of the neutron.

            Returns:
                cold_speed: tuple
                    The speed of the neutron.
        """
        return self.cold_speed

    def set_thermal_speed(self, speed):
        """
            The method is used to set the thermal speed of the neutron.

            Args:
                speed: tuple
                    The speed of the neutron.

            Returns:
                None
        """
        self.thermal_speed = speed

    def set_cold_speed(self, speed):
        """
            The method is used to set the cold speed of the neutron.

            Args:
                speed: tuple
                    The speed of the neutron.

            Returns:
                None
        """
        self.cold_speed = speed