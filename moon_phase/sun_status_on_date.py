from typing import Union
from datetime import datetime, timedelta, time
from zoneinfo import ZoneInfo
import ephem

from .determine_sun_sign import determine_sun_sign
from .generate_zodiac_emoji import generate_zodiac_emoji
from .process_date import process_date

def sun_status_on_date(
        d: Union[ephem.Date, datetime, time, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    d, timezone = process_date(d, timezone, lat, lon)

    sign = determine_sun_sign(d, lat=lat, lon=lon)
    emoji = generate_zodiac_emoji(sign)

    yesterday_sign = determine_sun_sign(d - timedelta(days=1), lat=lat, lon=lon)
    tomorrow_sign = determine_sun_sign(d + timedelta(days=1), lat=lat, lon=lon)

    if yesterday_sign != sign:
        movement_string = "enters"
    elif tomorrow_sign != sign:
        movement_string = "leaves"
    else:
        movement_string = "in"

    return f"🌞{emoji} Sun {movement_string} {sign}"
