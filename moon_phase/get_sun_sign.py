from datetime import datetime, date
from typing import Union
from zoneinfo import ZoneInfo

import ephem

from .get_sign import get_sign


def get_sun_sign(
        dt: Union[datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    sign = get_sign(
        body=ephem.Sun(), 
        dt=dt, 
        timezone=timezone, 
        lat=lat, 
        lon=lon
    )

    return sign
