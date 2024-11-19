from typing import Union
from datetime import datetime, timedelta, time
from zoneinfo import ZoneInfo
import ephem

from .determine_sun_sign import determine_sun_sign
from .generate_zodiac_emoji import generate_zodiac_emoji
from .process_time import process_time

def sun_status_at_time(
        dt: Union[ephem.Date, datetime, time, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    dt, timezone = process_time(dt, timezone, lat, lon)

    sign = determine_sun_sign(dt, lat=lat, lon=lon)
    emoji = generate_zodiac_emoji(sign)

    return f"🌞{emoji} Sun in {sign}"
