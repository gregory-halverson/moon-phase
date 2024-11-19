from datetime import datetime, date
from typing import Union
from zoneinfo import ZoneInfo
import geocoder
import dateparser
import ephem
import numpy as np

from .create_ephem_body import create_ephem_body
from .calculate_ecliptic_longitude import calculate_ecliptic_longitude
from .tropical_zodiac_from_ecliptic_longitude import tropical_zodiac_from_ecliptic_longitude

def determine_sign(
        body: ephem.Body,
        dt: Union[datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    """
    Determine the astrological sign of a celestial body at a given date and time.

    Parameters:
    body (ephem.Body): The celestial body for which to determine the sign.
    dt (Union[datetime, date, str], optional): The date and time for which to determine the sign. Defaults to None.
    timezone (Union[ZoneInfo, str], optional): The timezone of the given date and time. Defaults to None.
    lat (float, optional): The latitude of the observer. Defaults to None.
    lon (float, optional): The longitude of the observer. Defaults to None.

    Returns:
    str: The astrological sign of the celestial body.
    """
    
    # If the body is given as a string, create the ephem.Body object
    if isinstance(body, str):
        body = create_ephem_body(body)

    # Calculate the ecliptic longitude of the body
    ecliptic_longitude_degrees = calculate_ecliptic_longitude(
        body=body, 
        dt=dt, 
        timezone=timezone, 
        lat=lat, 
        lon=lon
    )
    
    # Determine the astrological sign from the ecliptic longitude
    sign = tropical_zodiac_from_ecliptic_longitude(ecliptic_longitude_degrees)

    return sign