from fissionmunk.core.objects import core
import pymunk

def test_create_core():
    c = core.Core(length=1220, width=600,thermal_factor=4, cold_factor=1, fast_factor=10)
    assert type(c.get_space()) == pymunk.Space