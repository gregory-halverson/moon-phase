from typing import Union
from datetime import datetime, date
from zoneinfo import ZoneInfo

import numpy as np
import ephem

from .create_ephem_body import create_ephem_body
from .parse_timestamp import parse_timestamp
from .locate_device import locate_device
from .process_time import process_time

def calculate_ecliptic_longitude(
        body: Union[ephem.Body, str],
        dt: Union[ephem.Date, datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> float:
    """
    Calculate the ecliptic longitude of a celestial body.

    Parameters:
    body (Union[ephem.Body, str]): The celestial body to calculate the ecliptic longitude for.
                                   Can be an ephem.Body object or a string representing the body.
    dt (Union[ephem.Date, datetime, date, str], optional): The date and time for the calculation.
                                                           Can be an ephem.Date, datetime, date, or string.
                                                           Defaults to None.
    timezone (Union[ZoneInfo, str], optional): The timezone for the date and time. Can be a ZoneInfo object or a string.
                                               Defaults to None.
    lat (float, optional): The latitude of the observer. Defaults to None.
    lon (float, optional): The longitude of the observer. Defaults to None.

    Returns:
    float: The ecliptic longitude of the celestial body in degrees.
    """
    # If the body is provided as a string, create an ephem.Body object
    if isinstance(body, str):
        body = create_ephem_body(body)

    # If latitude or longitude is not provided, locate the device to get the coordinates
    if lat is None or lon is None:
        lat, lon = locate_device()

    # Process the date and time, and adjust for the provided timezone
    dt, timezone = process_time(dt, timezone, lat, lon)

    # Create an observer object with the provided or located coordinates and date/time
    observer = ephem.Observer()
    observer.lat = lat
    observer.lon = lon
    observer.date = dt

    # Compute the position of the celestial body for the observer
    body.compute(observer)

    # Convert the right ascension to ecliptic longitude in degrees
    ecliptic_longitude_degrees = np.degrees(body.g_ra)

    return ecliptic_longitude_degrees