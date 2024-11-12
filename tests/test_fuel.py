from fissionmunk.Fuel import Fuel
from fissionmunk.FuelElement import FuelElement
from fissionmunk.Core import Core
from fissionmunk.Material import MaterialType as Material

def create_core():
    c = Core(length=1220, width=600,thermal_factor=4, cold_factor=1, fast_factor=10)
    return c

def test_create_fuels():
    f = Fuel(uranium_occurance_probability=0.5, xenon_occurance_probability=0.5, xenon_decay_probability=0.5, element_radius=10, width=580, position=(10, 290), fuel_element_gap=5)
    c = create_core()
    c.add_fuel_rod_to_core(f)
    assert len(c.get_fuel_rod_list()) == len(f.get_fuel_elements())
    c.remove_fuel_rod_from_core(f)

def test_remove_fuels():
    f = Fuel(uranium_occurance_probability=0.5, xenon_occurance_probability=0.5, xenon_decay_probability=0.5, element_radius=10, width=580, position=(10, 290), fuel_element_gap=5)
    c = create_core()
    c.add_fuel_rod_to_core(f)
    c.remove_fuel_rod_from_core(f)
    assert c.get_fuel_rod_list() == []

def test_get_length():
    f = Fuel(uranium_occurance_probability=0.5, xenon_occurance_probability=0.5, xenon_decay_probability=0.5, element_radius=10, width=580, position=(10, 290), fuel_element_gap=5)
    assert f.get_length() == 20

def test_get_width():
    f = Fuel(uranium_occurance_probability=0.5, xenon_occurance_probability=0.5, xenon_decay_probability=0.5, element_radius=10, width=580, position=(10, 290), fuel_element_gap=5)
    assert f.get_width() == 580

def test_get_position():
    f = Fuel(uranium_occurance_probability=0.5, xenon_occurance_probability=0.5, xenon_decay_probability=0.5, element_radius=10, width=580, position=(10, 290), fuel_element_gap=5)
    assert f.get_position() == (10, 290)

def test_get_radius():
    f = Fuel(uranium_occurance_probability=0.5, xenon_occurance_probability=0.5, xenon_decay_probability=0.5, element_radius=10, width=580, position=(10, 290), fuel_element_gap=5)
    assert f.get_radius() == 10

def test_create_fuel_element():
    fe_U = FuelElement(radius=10, uranium_occurance_probability=0.5, xenon_occurance_probability=0.5, xenon_decay_probability=0.5, material=Material.FISSILE)
    assert fe_U.get_material() == Material.FISSILE
    assert fe_U.get_radius() == 10
    assert fe_U.get_collision_type() == 3

    fe_NF = FuelElement(radius=10, uranium_occurance_probability=0.5, xenon_occurance_probability=0.5, xenon_decay_probability=0.5, material=Material.NON_FISSILE)
    assert fe_NF.get_material() == Material.NON_FISSILE
    assert fe_NF.get_collision_type() == 4

    fe_X = FuelElement(radius=10, uranium_occurance_probability=0.5, xenon_occurance_probability=0.5, xenon_decay_probability=0.5, material=Material.XENON)
    assert fe_X.get_material() == Material.XENON
    assert fe_X.get_collision_type() == 8

def test_change_material():
    fe = FuelElement(radius=10, uranium_occurance_probability=0.5, xenon_occurance_probability=0.5, xenon_decay_probability=0.5, material=Material.FISSILE)
    fe.change_material()
    assert fe.get_material() in [Material.FISSILE, Material.NON_FISSILE, Material.XENON]