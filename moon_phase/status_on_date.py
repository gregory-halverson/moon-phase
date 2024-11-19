from typing import Optional, Union
from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import dateparser
import ephem

from .is_retrograde import is_retrograde
from .generate_planet_emoji import generate_planet_emoji
from .generate_zodiac_emoji import generate_zodiac_emoji
from .generate_hebrew_date_string import generate_hebrew_date_string
from .generate_roman_date_string import generate_roman_date_string
from .moon_status_on_date import moon_status_on_date
from .sun_status_on_date import sun_status_on_date
from .determine_sign import determine_sign
from .process_date import process_date

def status_on_date(
        d: Union[ephem.Date, datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    """
    Generate a status report for a given date, including sun and moon status,
    Roman and Hebrew date strings, and planetary positions.

    Parameters:
    d (Union[ephem.Date, datetime, date, str], optional): The date for which to generate the status. Defaults to None.
    timezone (Union[ZoneInfo, str], optional): The timezone for the date. Defaults to None.
    lat (float, optional): The latitude for the location. Defaults to None.
    lon (float, optional): The longitude for the location. Defaults to None.

    Returns:
    str: A status report for the given date.
    """
    # Process the input date and timezone
    d, timezone = process_date(d, timezone, lat, lon)

    # Get the status of the sun on the given date
    sun_status = sun_status_on_date(d, lat=lat, lon=lon)
    # Generate the Roman date string
    roman_date = generate_roman_date_string(d)

    # Get the status of the moon on the given date
    moon_status = moon_status_on_date(d, lat=lat, lon=lon)
    # Generate the Hebrew date string
    hebrew_date = generate_hebrew_date_string(d)
    
    # Initialize the status report with sun, moon, Roman, and Hebrew date information
    status = f"{sun_status}\n{roman_date}\n{moon_status}\n{hebrew_date}"

    # Iterate over the planets to get their status
    for planet in ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]:
        # Generate the planet emoji
        planet_emoji = generate_planet_emoji(planet)
        # Determine the zodiac sign of the planet on the given date
        sign = determine_sign(planet, d, lat=lat, lon=lon)
        # Generate the zodiac emoji
        sign_emoji = generate_zodiac_emoji(sign)
        # Check if the planet is in retrograde
        retrograde = is_retrograde(planet, d, lat=lat, lon=lon)
        retrograde_string = 'Retrograde ' if retrograde else ''

        yesterday = d - timedelta(days=1)
        tomorrow = d + timedelta(days=1)

        # Determine the planet's sign on the previous and next day
        yesterday_sign = determine_sign(
            body=planet, 
            dt=yesterday, 
            timezone=timezone,
            lat=lat, 
            lon=lon
        )
        
        tomorrow_sign = determine_sign(
            body=planet, 
            dt=tomorrow, 
            timezone=timezone,
            lat=lat, 
            lon=lon
        )

        # Determine the movement of the planet
        if yesterday_sign != sign:
            movement_string = "enters"
        elif tomorrow_sign != sign:
            movement_string = "leaves"
        else:
            movement_string = "in"

        # Append the planet's status to the report
        status += f"\n{planet_emoji}{sign_emoji} {planet} {retrograde_string}{movement_string} {sign}"

    return status