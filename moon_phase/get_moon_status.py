from datetime import datetime, timedelta

from .get_moon_phase_emoji import get_moon_phase_emoji
from .get_phase import get_phase
from .get_moon_name import get_moon_name
from .get_moon_name_emoji import get_moon_name_emoji
from .get_moon_sign import get_moon_sign
from .get_zodiac_emoji import get_zodiac_emoji
from .parse_timestamp import parse_timestamp
from .get_location import get_location

def get_moon_status(
        dt: datetime = None,
        lat: float = None,
        lon: float = None,
        timezone: str = None) -> str:
    if lat is None or lon is None:
        lat, lon = get_location()

    if dt is None:
        dt = datetime.now()

    if not isinstance(dt, datetime) or dt.tzinfo is None:
        dt = parse_timestamp(dt, timezone, lat, lon)

    name = get_moon_name(dt, include_moon=False)
    moon_name_emoji = get_moon_name_emoji(name)
    phase = get_phase(dt)
    moon_phase_emoji = get_moon_phase_emoji(phase)
    sign = get_moon_sign(dt, lat=lat, lon=lon)
    zodiac_emoji = get_zodiac_emoji(sign)
    
    yesterday_sign = get_moon_sign(dt.date() - timedelta(days=1), lat=lat, lon=lon)
    tomorrow_sign = get_moon_sign(dt.date() + timedelta(days=1), lat=lat, lon=lon)

    if yesterday_sign != sign:
        movement_string = "enters"
    elif tomorrow_sign != sign:
        movement_string = "leaves"
    else:
        movement_string = "in"

    return f"{moon_name_emoji}{moon_phase_emoji}{zodiac_emoji} {phase} {name} Moon {movement_string} {sign}"
