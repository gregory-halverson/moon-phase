from datetime import datetime, timedelta

from .get_sun_sign import get_sun_sign
from .get_zodiac_emoji import get_zodiac_emoji

def get_sun_status(
        dt: datetime = None,
        lat: float = None,
        lon: float = None) -> str:
    sign = get_sun_sign(dt, lat=lat, lon=lon)
    emoji = get_zodiac_emoji(sign)

    yesterday_sign = get_sun_sign(dt.date() - timedelta(days=1), lat=lat, lon=lon)
    tomorrow_sign = get_sun_sign(dt.date() + timedelta(days=1), lat=lat, lon=lon)

    if yesterday_sign != sign:
        movement_string = "enters"
    elif tomorrow_sign != sign:
        movement_string = "leaves"
    else:
        movement_string = "in"

    return f"🌞{emoji} Sun {movement_string} {sign}"
