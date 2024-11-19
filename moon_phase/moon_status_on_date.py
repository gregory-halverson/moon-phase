from typing import Union
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo
import ephem

from .generate_moon_phase_emoji import generate_moon_phase_emoji
from .determine_moon_phase import determine_moon_phase
from .generate_moon_name import generate_moon_name
from .generate_moon_name_emoji import generate_moon_name_emoji
from .determine_moon_sign import determine
from .generate_zodiac_emoji import generate_zodiac_emoji
from .locate_device import locate_device
from .process_date import process_date

def moon_status_on_date(
        d: Union[ephem.Date, datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    """
    Returns a string describing the moon's status on a given date.

    Parameters:
    d (Union[ephem.Date, datetime, date, str], optional): The date for which to get the moon status. Defaults to None.
    timezone (Union[ZoneInfo, str], optional): The timezone for the date. Defaults to None.
    lat (float, optional): The latitude for the location. Defaults to None.
    lon (float, optional): The longitude for the location. Defaults to None.

    Returns:
    str: A string describing the moon's phase, name, and zodiac sign.
    """
    # If latitude and longitude are not provided, locate the device to get them
    if lat is None or lon is None:
        lat, lon = locate_device()

    # Process the date and timezone
    d, timezone = process_date(d, timezone, lat, lon) 

    # Generate the moon's name and corresponding emoji
    name = generate_moon_name(d, include_moon=False)
    moon_name_emoji = generate_moon_name_emoji(name)

    # Get the moon's phase and corresponding emoji
    phase = determine_moon_phase(d)
    moon_phase_emoji = generate_moon_phase_emoji(phase)

    # Get the moon's zodiac sign and corresponding emoji
    sign = determine(d, lat=lat, lon=lon)
    zodiac_emoji = generate_zodiac_emoji(sign)
    
    # Determine the moon's zodiac sign for the previous and next day
    yesterday_sign = determine(d - timedelta(days=1), lat=lat, lon=lon)
    tomorrow_sign = determine(d + timedelta(days=1), lat=lat, lon=lon)

    # Determine the movement of the moon in the zodiac
    if yesterday_sign != sign:
        movement_string = "enters"
    elif tomorrow_sign != sign:
        movement_string = "leaves"
    else:
        movement_string = "in"

    # Return the formatted string describing the moon's status
    return f"{moon_name_emoji}{moon_phase_emoji}{zodiac_emoji} {phase} {name} Moon {movement_string} {sign}"