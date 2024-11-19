from datetime import datetime, date
from typing import Union
from zoneinfo import ZoneInfo

import ephem

from .determine_sign import determine_sign

def determine(
        dt: Union[datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    """
    Calculate the moon sign for a given date, time, and location.

    Parameters:
    dt (Union[datetime, date, str], optional): The date and time for which to calculate the moon sign. 
                                               Can be a datetime object, date object, or string. Defaults to None.
    timezone (Union[ZoneInfo, str], optional): The timezone for the given date and time. Can be a ZoneInfo object or string. Defaults to None.
    lat (float, optional): The latitude of the location. Defaults to None.
    lon (float, optional): The longitude of the location. Defaults to None.

    Returns:
    str: The moon sign for the given date, time, and location.
    """
    # Use the get_sign function to calculate the moon sign
    return determine_sign(ephem.Moon(), dt, timezone, lat, lon)