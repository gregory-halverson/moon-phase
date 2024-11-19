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
from .moon_status_at_time import moon_status_at_time
from .sun_status_at_time import sun_status_at_time
from .determine_sign import determine_sign
from .process_time import process_time

def status_at_time(
        dt: Union[ephem.Date, datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    dt, timezone = process_time(dt, timezone, lat, lon)

    sun_status = sun_status_at_time(
        dt=dt,
        timezone=timezone,
        lat=lat, 
        lon=lon
    )
    
    roman_date = generate_roman_date_string(dt)

    moon_status = moon_status_at_time(
        dt=dt, 
        timezone=timezone,
        lat=lat, 
        lon=lon
    )
    
    hebrew_date = generate_hebrew_date_string(dt)
    status = f"{sun_status}\n{roman_date}\n{moon_status}\n{hebrew_date}"

    for planet in ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]:
        planet_emoji = generate_planet_emoji(planet)
        
        sign = determine_sign(
            body=planet, 
            dt=dt, 
            timezone=timezone,
            lat=lat, 
            lon=lon
        )
        
        sign_emoji = generate_zodiac_emoji(sign)
        retrograde = is_retrograde(planet, dt, lat=lat, lon=lon)
        retrograde_string = 'Retrograde ' if retrograde else ''

        status += f"\n{planet_emoji}{sign_emoji} {planet} {retrograde_string}in {sign}"

    return status