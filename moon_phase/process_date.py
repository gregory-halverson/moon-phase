from typing import Union, Tuple
from datetime import datetime, date
from zoneinfo import ZoneInfo
import numpy as np
import ephem

from .process_time import process_time

def process_date(
        d: Union[ephem.Date, datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> Tuple[date, ZoneInfo]:
    """
    Process the input date and return a date object.

    Parameters:
    d (Union[ephem.Date, datetime, date, str], optional): The input date which can be of various types.
    timezone (Union[ZoneInfo, str], optional): The timezone information.
    lat (float, optional): Latitude for location-based processing.
    lon (float, optional): Longitude for location-based processing.

    Returns:
    date: The processed date object.
    """
    if d is None:
        # If no date is provided, use the current date
        d = datetime.now().date()

    if not isinstance(d, date):
        # If the input is not a date object, process it to get date and timezone
        d, timezone = process_time(d, timezone, lat, lon)
        
    if isinstance(d, datetime):
        # Convert datetime object to date object
        d = d.date()

    return d, timezone