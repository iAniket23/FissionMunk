from fissionmunk.core.objects import neutron
from fissionmunk.core.objects import core

def create_core():
    c = core.Core(length=1220, width=600,thermal_factor=4, cold_factor=1, fast_factor=10)
    return c

def test_create_neutron():
    n = neutron.Neutron(speed = (20, 20), position = (300, 300))
    c = create_core()
    c.add_neutron_to_core(n)
    assert c.get_neutron_list() == [n]
    assert neutron.Neutron.body_to_neutron[(n.get_body(), n.get_shape())] == n
    c.remove_neutron_from_core(n)

def test_remove_neutron():
    n = neutron.Neutron(speed = (20, 20), position = (300, 300))
    c = create_core()
    c.add_neutron_to_core(n)
    c.remove_neutron_from_core(n)
    assert c.get_neutron_list() == []
    assert ((n.get_body(), n.get_shape()) not in neutron.Neutron.body_to_neutron)

def test_get_speed():
    n = neutron.Neutron(speed = (20, 20), position = (300, 300))
    assert n.get_speed() == (20, 20)

def test_set_speed():
    n = neutron.Neutron(speed = (20, 20), position = (300, 300))
    n.set_speed((30, 30))
    assert n.get_speed() == (30, 30)

def test_get_position():
    n = neutron.Neutron(speed = (20, 20), position = (300, 300))
    assert n.get_position() == (300, 300)

def test_set_position():
    n = neutron.Neutron(speed = (20, 20), position = (300, 300))
    n.set_position((400, 400))
    assert n.get_position() == (400, 400)

def test_collision_type():
    n = neutron.Neutron(speed = (20, 20), position = (300, 300))
    assert n.get_shape().collision_type == 1