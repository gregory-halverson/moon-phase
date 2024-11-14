from datetime import datetime, date, timedelta
from typing import Union
from zoneinfo import ZoneInfo
import geocoder
import dateparser
import ephem
import numpy as np

from .constants import *
from .get_location import get_location
from .get_timezone import get_timezone
from .parse_timestamp import parse_timestamp
from .get_body import get_body
from .get_ecliptic_longitude import get_ecliptic_longitude
from .tropical_zodiac_from_ecliptic_longitude import tropical_zodiac_from_ecliptic_longitude
from .get_sign import get_sign

def next_sign(
        body: ephem.Body,
        current_date: Union[date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    if isinstance(body, str):
        body = get_body(body)

    if lat is None or lon is None:
        lat, lon = get_location()

    if current_date is None:
        current_date = datetime.now().date()

    if not isinstance(current_date, date):
        current_date = parse_timestamp(current_date, timezone, lat, lon).date()
    
    current_sign = get_sign(body, current_date, timezone, lat, lon)
    sign = current_sign
    d = current_date

    while sign == current_sign:
        print(d, sign)
        d += timedelta(days=1)
        sign = get_sign(body, d, timezone, lat, lon)

    return d, sign
