from datetime import datetime, date
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

def get_sign(
        body: ephem.Body,
        dt: Union[datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    if isinstance(body, str):
        body = get_body(body)

    ecliptic_longitude_degrees = get_ecliptic_longitude(body, dt, timezone, lat, lon)
    sign = tropical_zodiac_from_ecliptic_longitude(ecliptic_longitude_degrees)

    return sign
