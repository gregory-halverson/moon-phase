from typing import Union, Tuple
from datetime import datetime, date
import dateparser
from zoneinfo import ZoneInfo

from .locate_device import locate_device
from .find_timezone import find_timezone

def parse_timestamp(
        timestamp: str,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> Tuple[Union[datetime, date], Union[ZoneInfo, None]]:
    """
    Parses a timestamp string and returns a datetime object if a time is given,
    even if the time is midnight. Returns a date object if no time is given.
    Also returns the timezone used.

    Args:
        timestamp (str): The timestamp string to parse.
        timezone (Union[ZoneInfo, str], optional): The timezone to use. Defaults to None.
        lat (float, optional): Latitude for timezone lookup if timezone is not provided. Defaults to None.
        lon (float, optional): Longitude for timezone lookup if timezone is not provided. Defaults to None.

    Returns:
        Tuple[Union[datetime, date], Union[ZoneInfo, None]]: A tuple containing a datetime object if a time is given,
        otherwise a date object, and the timezone used.
    """
    if not isinstance(timestamp, str):
        timestamp = str(timestamp)

    # Parse the timestamp string into a datetime object
    dt = dateparser.parse(timestamp)

    # If the parsed datetime has timezone info and no explicit timezone is provided
    if dt.tzinfo is not None and timezone is None:
        # Check if the time is exactly midnight and no time component is present in the string
        if dt.time() == datetime.min.time() and timestamp.strip().count(':') == 0:
            return dt.date(), dt.tzinfo
        return dt, dt.tzinfo
    elif timezone is None:
        # If no timezone is provided, find the timezone based on latitude and longitude
        if lat is None or lon is None:
            lat, lon = locate_device()

        timezone = find_timezone(lat, lon)
    else:
        # Use the provided timezone
        timezone = ZoneInfo(timezone)

    # Replace the timezone info in the parsed datetime
    dt = dt.replace(tzinfo=timezone)

    # Check if the time is exactly midnight and no time component is present in the string
    if dt.time() == datetime.min.time() and timestamp.strip().count(':') == 0:
        return dt.date(), timezone
    
    return dt, timezone