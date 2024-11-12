from fissionmunk.Moderator import Moderator
from fissionmunk.Core import Core
from fissionmunk.Material import MaterialType as Material

def create_core():
    c = Core(length=1220, width=600,thermal_factor=4, cold_factor=1, fast_factor=10)
    return c

def test_create_moderator():
    m = Moderator(length=10, width=580, position=(10, 290), material=Material.GRAPHITE)
    c = create_core()
    c.add_moderator_to_core(m)
    assert c.get_moderator_list() == [m]
    c.remove_moderator_from_core(m)

def test_remove_moderator():
    m = Moderator(length=10, width=580, position=(10, 290), material=Material.GRAPHITE)
    c = create_core()
    c.add_moderator_to_core(m)
    c.remove_moderator_from_core(m)
    assert c.get_moderator_list() == []

def test_get_length():
    m = Moderator(length=10, width=580, position=(10, 290), material=Material.GRAPHITE)
    assert m.get_length() == 10

def test_get_width():
    m = Moderator(length=10, width=580, position=(10, 290), material=Material.GRAPHITE)
    assert m.get_width() == 580

def test_get_position():
    m = Moderator(length=10, width=580, position=(10, 290), material=Material.GRAPHITE)
    assert m.get_position() == (10, 290)

def test_set_position():
    m = Moderator(length=10, width=580, position=(10, 290), material=Material.GRAPHITE)
    m.set_position((20, 300))
    assert m.get_position() == (20, 300)