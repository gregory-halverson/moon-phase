from typing import Optional, Union
from datetime import datetime, date, timedelta
import dateparser

from .is_retrograde import is_retrograde
from .get_planet_emoji import get_planet_emoji
from .get_zodiac_emoji import get_zodiac_emoji
from .get_hebrew_date_string import get_hebrew_date_string
from .get_roman_date_string import get_roman_date_string
from .get_moon_status import get_moon_status
from .get_sun_status import get_sun_status
from .get_sign import get_sign

def get_status(
        dt: Optional[Union[datetime, date]] = None, 
        lat: Optional[float] = None, 
        lon: Optional[float] = None) -> str:
    if dt is None:
        dt = datetime.now()
    elif isinstance(dt, str):
        dt = dateparser.parse(dt)
    elif isinstance(dt, date):
        if isinstance(dt, date):
            if hasattr(dt, "tzinfo"):
                tzinfo = dt.tzinfo
            else:
                tzinfo = datetime.now().astimezone().tzinfo
            
            # convert date to datetime at midnight
            dt = datetime(dt.year, dt.month, dt.day, 0, 0, 0, 0, tzinfo=tzinfo)

    sun_status = get_sun_status(dt, lat=lat, lon=lon)
    roman_date = get_roman_date_string(dt)
    moon_status = get_moon_status(dt, lat=lat, lon=lon)
    hebrew_date = get_hebrew_date_string(dt)
    status = f"{sun_status}\n{roman_date}\n{moon_status}\n{hebrew_date}"

    for planet in ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]:
        planet_emoji = get_planet_emoji(planet)
        sign = get_sign(planet, dt, lat=lat, lon=lon)
        sign_emoji = get_zodiac_emoji(sign)
        retrograde = is_retrograde(planet, dt, lat=lat, lon=lon)
        retrograde_string = 'Retrograde ' if retrograde else ''

        yesterday_sign = get_sign(planet, dt.date() - timedelta(days=1), lat=lat, lon=lon)
        tomorrow_sign = get_sign(planet, dt.date() + timedelta(days=1), lat=lat, lon=lon)

        if yesterday_sign != sign:
            movement_string = "enters"
        elif tomorrow_sign != sign:
            movement_string = "leaves"
        else:
            movement_string = "in"

        status += f"\n{planet_emoji}{sign_emoji} {planet} {retrograde_string}{movement_string} {sign}"

    return status