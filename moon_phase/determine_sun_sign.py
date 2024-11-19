from datetime import datetime, date
from typing import Union
from zoneinfo import ZoneInfo

import ephem

from .determine_sign import determine_sign

def determine_sun_sign(
        dt: Union[datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    """
    Determine the sun sign based on the provided date, time, and location.

    Parameters:
    dt (Union[datetime, date, str], optional): The date and time for which to determine the sun sign. 
                                               Can be a datetime object, date object, or string. Defaults to None.
    timezone (Union[ZoneInfo, str], optional): The timezone information. Can be a ZoneInfo object or string. Defaults to None.
    lat (float, optional): The latitude of the location. Defaults to None.
    lon (float, optional): The longitude of the location. Defaults to None.

    Returns:
    str: The sun sign for the given date, time, and location.
    """
    # Determine the sun sign using the determine_sign function
    sign = determine_sign(
        body=ephem.Sun(), 
        dt=dt, 
        timezone=timezone, 
        lat=lat, 
        lon=lon
    )

    # Return the determined sun sign
    return sign