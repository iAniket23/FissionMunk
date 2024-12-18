from fissionmunk.Neutron import Neutron
from fissionmunk.Core import Core

def create_core():
    c = Core(length=1220, width=600,thermal_factor=4, cold_factor=1, fast_factor=10)
    return c

def test_create_neutron():
    n = Neutron(speed = (20, 20), position = (300, 300))
    c = create_core()
    c.add_neutron_to_core(n)
    assert c.get_neutron_list() == [n]
    assert Neutron.body_to_neutron[(n.get_body(), n.get_shape())] == n
    c.remove_neutron_from_core(n)

def test_remove_neutron():
    n = Neutron(speed = (20, 20), position = (300, 300))
    c = create_core()
    c.add_neutron_to_core(n)
    c.remove_neutron_from_core(n)
    assert c.get_neutron_list() == []
    assert ((n.get_body(), n.get_shape()) not in Neutron.body_to_neutron)

def test_get_speed():
    n = Neutron(speed = (20, 20), position = (300, 300))
    assert n.get_speed() == (20, 20)

def test_set_speed():
    n = Neutron(speed = (20, 20), position = (300, 300))
    n.set_speed((30, 30))
    assert n.get_speed() == (30, 30)

def test_get_position():
    n = Neutron(speed = (20, 20), position = (300, 300))
    assert n.get_position() == (300, 300)

def test_set_position():
    n = Neutron(speed = (20, 20), position = (300, 300))
    n.set_position((400, 400))
    assert n.get_position() == (400, 400)

def test_collision_type():
    n = Neutron(speed = (20, 20), position = (300, 300))
    assert n.get_shape().collision_type == 1