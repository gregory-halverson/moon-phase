from datetime import datetime, date
from typing import Union
from zoneinfo import ZoneInfo

import ephem

from .get_sign import get_sign


def get_moon_sign(
        dt: Union[datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    return get_sign(ephem.Moon(), dt, timezone, lat, lon)
