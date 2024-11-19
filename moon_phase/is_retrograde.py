from typing import Union
from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import ephem

from .process_time import process_time
from .locate_device import locate_device
from .create_ephem_body import create_ephem_body
from .calculate_ecliptic_longitude import calculate_ecliptic_longitude

def is_retrograde(
        body: Union[ephem.Body, str],
        dt: Union[datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> bool:
    """
    Determine if a celestial body is in retrograde motion.

    Parameters:
    body (Union[ephem.Body, str]): The celestial body to check. Can be an ephem.Body object or a string.
    dt (Union[datetime, date, str], optional): The date and time to check. Defaults to None.
    timezone (Union[ZoneInfo, str], optional): The timezone of the location. Defaults to None.
    lat (float, optional): The latitude of the location. Defaults to None.
    lon (float, optional): The longitude of the location. Defaults to None.

    Returns:
    bool: True if the body is in retrograde motion, False otherwise.
    """
    # If the body is provided as a string, create an ephem.Body object
    if isinstance(body, str):
        body = create_ephem_body(body)

    # Check if the body is one of the planets that can be in retrograde motion
    if not isinstance(body, (ephem.Mercury, ephem.Venus, ephem.Mars, ephem.Jupiter, ephem.Saturn)):
        return False

    # If latitude or longitude is not provided, locate the device to get the coordinates
    if lat is None or lon is None:
        lat, lon = locate_device()

    # Process the date, time, and timezone
    dt, timezone = process_time(dt, timezone, lat, lon)

    # Calculate the ecliptic longitude for the given date and the previous day
    ecliptic_longitude_degrees = calculate_ecliptic_longitude(body, dt, timezone, lat, lon)
    previous_day_ecliptic_longitude_degrees = calculate_ecliptic_longitude(body, dt - timedelta(days=1), timezone, lat, lon)

    # Determine the difference in ecliptic longitude between the two days
    difference = ecliptic_longitude_degrees - previous_day_ecliptic_longitude_degrees

    # If the difference is negative, the body is in retrograde motion
    is_retrograde = difference < 0

    return is_retrograde
