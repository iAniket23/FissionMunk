from fissionmunk.Core import Core
from fissionmunk.Water import Water
from fissionmunk.Material import MaterialType as Material

def create_core():
    c = Core(length=1220, width=600,thermal_factor=4, cold_factor=1, fast_factor=10)
    return c

def test_create_water():
    c = create_core()
    w = Water(length=100, width=100, position=(100, 100))
    c.add_water_to_core(w)
    assert c.get_water_list() == [w]
    c.remove_water_from_core(w)

def test_remove_water():
    c = create_core()
    w = Water(length=100, width=100, position=(100, 100))
    c.add_water_to_core(w)
    c.remove_water_from_core(w)
    assert c.get_water_list() == []

def test_change_temperature():
    c = create_core()
    w = Water(length=100, width=100, position=(100, 100))
    c.add_water_to_core(w)
    w.change_temperature(10)
    assert w.temperature == 10
    w.change_temperature(-10)
    assert w.temperature == 0
    c.remove_water_from_core(w)

def test_switch_coolant():
    c = create_core()
    w = Water(length=100, width=100, position=(100, 100))
    c.add_water_to_core(w)
    w.turn_on_coolant()
    assert w.coolant == True
    w.turn_off_coolant()
    assert w.coolant == False
    c.remove_water_from_core(w)

def test_water_removed():
    c = create_core()
    w = Water(length=100, width=100, position=(100, 100), hard_limit=10, temperature_threshold=30)
    c.add_water_to_core(w)
    w.change_temperature(40)
    assert w.removed == True
    c.remove_water_from_core(w)

def test_water_recreated():
    c = create_core()
    w = Water(length=100, width=100, position=(100, 100), hard_limit=10, temperature_threshold=100)
    c.add_water_to_core(w)
    w.change_temperature(120)
    assert w.removed == True
    w.change_temperature(-50)
    assert w.removed == False
    c.remove_water_from_core(w)

def test_collision_type():
    c = create_core()
    w = Water(length=100, width=100, position=(100, 100))
    c.add_water_to_core(w)
    assert w.shape.collision_type == 11
    w.change_collision_type(12)
    assert w.shape.collision_type == 12
    c.remove_water_from_core(w)