# Core class
import pymunk

class Core:
    def __init__(self, length, width, neutron_speed = (40, 0), thermal_factor = 50, cold_factor = 10, fast_factor = 100):
        # Core dimensions
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
        self.space.add(neutron.get_body(), neutron.get_shape())
        self.neutron_list.append(neutron)

    def remove_neutron_from_core(self, neutron):
        self.space.remove(neutron.get_body(), neutron.get_shape())
        self.neutron_list.remove(neutron)

    def add_water_to_core(self, water):
        self.space.add(water.get_body(), water.get_shape())
        self.water_list.append(water)

    def remove_water_from_core(self, water):
        self.space.remove(water.get_body(), water.get_shape())
        self.water_list.remove(water)

    # Add and remove moderator from the core
    def add_moderator_to_core(self, moderator):
        self.space.add(moderator.get_body(), moderator.get_shape())
        self.moderator_list.append(moderator)


    def remove_moderator_from_core(self, moderator):
        self.space.remove(moderator.get_body(), moderator.get_shape())
        self.moderator_list.remove(moderator)

    # Add and remove control rod from the core
    def add_control_rod_to_core(self, control_rod):
        self.space.add(control_rod.get_body(), control_rod.get_shape())
        self.control_rod_list.append(control_rod)


    def remove_control_rod_from_core(self, control_rod):
        self.space.remove(control_rod.get_body(), control_rod.get_shape())
        self.control_rod_list.remove(control_rod)

    # Add and remove fuel rod from the core
    def add_fuel_rod_to_core(self, fuel_rod):
        for fuel_element in fuel_rod.get_fuel_elements():
            self.space.add(fuel_element.get_body(), fuel_element.get_shape())
            self.fuel_rod_list.append(fuel_rod)

    def remove_fuel_rod_from_core(self, fuel_rod):
        for fuel_element in fuel_rod.get_fuel_elements():
            self.space.remove(fuel_element.get_body(), fuel_element.get_shape())
            self.fuel_rod_list.remove(fuel_rod)

    # Getters and setters
    def get_water_list(self):
        return self.water_list

    def get_neutron_list(self):
        return self.neutron_list

    def get_moderator_list(self):
        return self.moderator_list

    def get_control_rod_list(self):
        return self.control_rod_list

    def get_fuel_rod_list(self):
        return self.fuel_rod_list

    def get_space(self):
        return self.space

    def set_fast_speed(self, speed):
        self.fast_speed = speed

    def get_fast_speed(self):
        return self.fast_speed

    def get_thermal_speed(self):
        return self.thermal_speed

    def get_cold_speed(self):
        return self.cold_speed

    def set_thermal_speed(self, speed):
        self.thermal_speed = speed

    def set_cold_speed(self, speed):
        self.cold_speed = speed