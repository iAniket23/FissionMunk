import enum

class MaterialType(enum.Enum):
    """The type of material that is being used in the simulation.

    :param enum: The type of material that is being used in the simulation.
    :type enum: enum.Enum
    """
    WATER = "water"
    GRAPHITE = "graphite"
    BORON = "boron"
    XENON = "xenon"
    FISSILE = "fissile"
    NON_FISSILE = "non-fissile"
    BORON_CARBIDE = "boron carbide"