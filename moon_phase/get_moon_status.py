from datetime import datetime

from .get_moon_phase_emoji import get_moon_phase_emoji
from .get_phase import get_phase
from .get_moon_name import get_moon_name
from .get_moon_name_emoji import get_moon_name_emoji
from .get_moon_sign import get_moon_sign
from .get_zodiac_emoji import get_zodiac_emoji

def get_moon_status(dt: datetime = None) -> str:
    name = get_moon_name(dt, include_moon=False)
    moon_name_emoji = get_moon_name_emoji(name)
    moon_phase_emoji = get_moon_phase_emoji(dt)
    sign = get_moon_sign(dt)
    zodiac_emoji = get_zodiac_emoji(sign)
    phase = get_phase(dt)

    return f"{moon_name_emoji}{moon_phase_emoji}{zodiac_emoji} {phase} {name} Moon in {sign}"
