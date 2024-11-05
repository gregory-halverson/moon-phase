from datetime import datetime

from .get_sun_sign import get_sun_sign
from .get_zodiac_emoji import get_zodiac_emoji

def get_sun_status(dt: datetime = None) -> str:
    sign = get_sun_sign(dt)
    emoji = get_zodiac_emoji(sign)

    return f"🌞{emoji} Sun in {sign}"
