import enum

class MaterialType(enum.Enum):
    """
        Enum class for the different types of materials that can be used in the simulation.
    """
    WATER = "water"
    GRAPHITE = "graphite"
    BORON = "boron"
    XENON = "xenon"
    FISSILE = "fissile"
    NON_FISSILE = "non-fissile"
    BORON_CARBIDE = "boron carbide"