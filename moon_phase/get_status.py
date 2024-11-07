from datetime import datetime
import dateparser

from .is_retrograde import is_retrograde
from .get_planet_emoji import get_planet_emoji
from .get_zodiac_emoji import get_zodiac_emoji
from .get_hebrew_date_string import get_hebrew_date_string
from .get_roman_date_string import get_roman_date_string
from .get_moon_status import get_moon_status
from .get_sun_status import get_sun_status
from .get_sign import get_sign

def get_status(dt: datetime = None) -> str:
    if dt is None:
        dt = datetime.now()
    elif isinstance(dt, str):
        dt = dateparser.parse(dt)

    sun_status = get_sun_status(dt)
    roman_date = get_roman_date_string(dt)
    moon_status = get_moon_status(dt)
    hebrew_date = get_hebrew_date_string(dt)
    status = f"{sun_status}\n{roman_date}\n{moon_status}\n{hebrew_date}"

    for planet in ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]:
        planet_emoji = get_planet_emoji(planet)
        sign = get_sign(planet, dt)
        sign_emoji = get_zodiac_emoji(sign)
        retrograde = is_retrograde(planet, dt)
        status += f"\n{planet_emoji}{sign_emoji} {planet} {'Retrograde ' if retrograde else ''}in {sign}"

    return status
