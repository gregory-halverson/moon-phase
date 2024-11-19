from .constants import ZODIAC_SIGNS

def tropical_zodiac_from_ecliptic_longitude(ecliptic_longitude_degrees: float) -> str:
    """
    Determine the tropical zodiac sign from the given ecliptic longitude.

    Parameters:
    ecliptic_longitude_degrees (float): The ecliptic longitude in degrees.

    Returns:
    str: The corresponding tropical zodiac sign.
    """
    return ZODIAC_SIGNS[int(ecliptic_longitude_degrees / 30)]
