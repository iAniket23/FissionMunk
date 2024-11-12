from fissionmunk.core.objects import controlRod
from fissionmunk.core.objects import core
from fissionmunk.core.objects.material import MaterialType as material

def create_core():
    c = core.Core(length=1220, width=600,thermal_factor=4, cold_factor=1, fast_factor=10)
    return c

def test_create_controlRod():
    c = create_core()
    cr = controlRod.ControlRod(length=10, width=600, position=(0, 0), movement_range=[20, 580],material=material.BORON_CARBIDE)
    c.add_control_rod_to_core(cr)
    assert c.control_rod_list == [cr]
    c.remove_control_rod_from_core(cr)

def test_remove_controlRod():
    c = create_core()
    cr = controlRod.ControlRod(length=10, width=600, position=(0, 0), movement_range=[20, 580],material=material.BORON_CARBIDE)
    c.add_control_rod_to_core(cr)
    c.remove_control_rod_from_core(cr)
    assert c.control_rod_list == []

def test_get_tag():
    cr = controlRod.ControlRod(length=10, width=600, position=(0, 0), movement_range=[20, 580],material=material.BORON_CARBIDE)
    assert cr.get_tag() == "E"

def test_set_tag():
    cr = controlRod.ControlRod(length=10, width=600, position=(0, 0), movement_range=[20, 580],material=material.BORON_CARBIDE)
    cr.set_tag("O")
    assert cr.get_tag() == "O"

def test_get_position():
    cr = controlRod.ControlRod(length=10, width=600, position=(0, 0), movement_range=[20, 580],material=material.BORON_CARBIDE)
    assert cr.get_position() == (0, 0)

def test_set_position():
    cr = controlRod.ControlRod(length=10, width=600, position=(0, 0), movement_range=[20, 580],material=material.BORON_CARBIDE)
    cr.set_position((10, 10))
    assert cr.get_position() == (10, 10)

def test_reach_top():
    cr = controlRod.ControlRod(length=10, width=600, position=(10, 0), movement_range=[20, 580],material=material.BORON_CARBIDE)
    assert cr.reach_top == False
    cr.move_control_rod(-300)
    assert cr.reach_top == True

def test_reach_bottom():
    cr = controlRod.ControlRod(length=10, width=600, position=(10, 0), movement_range=[20, 580],material=material.BORON_CARBIDE)
    assert cr.reach_bottom == False
    cr.move_control_rod(600)
    assert cr.reach_bottom == True

def test_collision_type():
    cr = controlRod.ControlRod(length=10, width=600, position=(10, 0), movement_range=[20, 580],material=material.BORON_CARBIDE)
    assert cr.get_shape().collision_type == 5