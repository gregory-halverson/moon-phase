from typing import Union, Tuple
from datetime import datetime, date, time
from zoneinfo import ZoneInfo
import numpy as np
import ephem

from .create_ephem_body import create_ephem_body
from .parse_timestamp import parse_timestamp
from .locate_device import locate_device
from .find_timezone import find_timezone

def process_time(
        dt: Union[ephem.Date, datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> Tuple[datetime, ZoneInfo]:
    """
    Process the given time and timezone information, and return a datetime object with the appropriate timezone.

    Parameters:
    dt (Union[ephem.Date, datetime, date, str], optional): The date/time to process. Defaults to None.
    timezone (Union[ZoneInfo, str], optional): The timezone information. Defaults to None.
    lat (float, optional): Latitude for location-based timezone determination. Defaults to None.
    lon (float, optional): Longitude for location-based timezone determination. Defaults to None.

    Returns:
    Tuple[datetime, ZoneInfo]: A tuple containing the processed datetime object and the timezone.
    """
    # If latitude or longitude is not provided, locate the device to get them
    if lat is None or lon is None:
        lat, lon = locate_device()

    # If datetime is not provided, use the current datetime
    if dt is None:
        dt = datetime.now()

    # If datetime is a string, parse it to get the datetime object and timezone
    if isinstance(dt, str):
        dt, timezone = parse_timestamp(dt, timezone, lat, lon)

    # If datetime is an ephem.Date, convert it to a datetime object
    if isinstance(dt, ephem.Date):
        dt = dt.datetime()

    # If datetime is a date, convert it to a datetime object with time set to midnight
    if isinstance(dt, date) and not isinstance(dt, datetime):
        dt = datetime.combine(dt, time.min)

    # If timezone is not provided, find the timezone based on latitude and longitude
    if timezone is None:
        timezone = find_timezone(lat, lon)
    
    # If datetime is a datetime object and does not have timezone info, set the timezone
    if isinstance(dt, datetime) and dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone)

    return dt, timezone