from timezonefinder import TimezoneFinder
from zoneinfo import ZoneInfo

from .locate_device import locate_device

def find_timezone(
        lat: float = None,
        lon: float = None) -> ZoneInfo:
    """
    Find the timezone for a given latitude and longitude.

    If latitude and longitude are not provided, the function will
    attempt to get the current location's coordinates.

    Args:
        lat (float, optional): Latitude of the location. Defaults to None.
        lon (float, optional): Longitude of the location. Defaults to None.

    Returns:
        ZoneInfo: The timezone information for the given coordinates.
    """
    if lat is None or lon is None:
        # Get the current location's coordinates if not provided
        lat, lon = locate_device()

    # Find the timezone using the provided or obtained coordinates
    timezone = ZoneInfo(TimezoneFinder().timezone_at(lng=lon, lat=lat))

    return timezone