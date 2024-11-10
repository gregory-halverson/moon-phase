from .constants import ZODIAC_SIGNS

def tropical_zodiac_from_ecliptic_longitude(ecliptic_longitude_degrees: float) -> str:
    return ZODIAC_SIGNS[int(ecliptic_longitude_degrees / 30)]
