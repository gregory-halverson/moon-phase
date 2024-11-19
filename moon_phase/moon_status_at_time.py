from typing import Union
from datetime import datetime, date
from zoneinfo import ZoneInfo
import ephem

from .generate_moon_phase_emoji import generate_moon_phase_emoji
from .determine_moon_phase import determine_moon_phase
from .generate_moon_name import generate_moon_name
from .generate_moon_name_emoji import generate_moon_name_emoji
from .determine_moon_sign import determine
from .generate_zodiac_emoji import generate_zodiac_emoji
from .parse_timestamp import parse_timestamp
from .locate_device import locate_device
from .process_time import process_time

def moon_status_at_time(
        dt: Union[ephem.Date, datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    """
    Generate a string describing the moon's status at a given time and location.

    Parameters:
    dt (Union[ephem.Date, datetime, date, str]): The date and time for which to get the moon status.
    timezone (Union[ZoneInfo, str]): The timezone for the given date and time.
    lat (float): The latitude of the location.
    lon (float): The longitude of the location.

    Returns:
    str: A string describing the moon's phase, name, and zodiac sign with corresponding emojis.
    """
    # If latitude and longitude are not provided, locate the device
    if lat is None or lon is None:
        lat, lon = locate_device()

    # Process the time and timezone
    dt, timezone = process_time(dt, timezone, lat, lon) 

    # Generate moon name and corresponding emoji
    name = generate_moon_name(dt, include_moon=False)
    moon_name_emoji = generate_moon_name_emoji(name)

    # Get moon phase and corresponding emoji
    phase = determine_moon_phase(dt)
    moon_phase_emoji = generate_moon_phase_emoji(phase)

    # Get moon sign and corresponding zodiac emoji
    sign = determine(dt, lat=lat, lon=lon)
    zodiac_emoji = generate_zodiac_emoji(sign)

    # Return the formatted string
    return f"{moon_name_emoji}{moon_phase_emoji}{zodiac_emoji} {phase} {name} Moon in {sign}"