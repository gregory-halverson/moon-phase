from datetime import datetime, date, timedelta
from typing import Union
from zoneinfo import ZoneInfo
import geocoder
import dateparser
import ephem
import numpy as np

from .constants import *
from .locate_device import locate_device
from .find_timezone import find_timezone
from .create_ephem_body import create_ephem_body
from .calculate_ecliptic_longitude import calculate_ecliptic_longitude
from .tropical_zodiac_from_ecliptic_longitude import tropical_zodiac_from_ecliptic_longitude
from .determine_sign import determine_sign
from .process_date import process_date

def next_sign(
        body: ephem.Body,
        current_date: Union[date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    if isinstance(body, str):
        body = create_ephem_body(body)

    if lat is None or lon is None:
        lat, lon = locate_device()

    current_date, timezone = process_date(current_date, timezone, lat, lon)
    
    current_sign = determine_sign(body, current_date, timezone, lat, lon)
    sign = current_sign
    d = current_date

    while sign == current_sign:
        d += timedelta(days=1)
        sign = determine_sign(body, d, timezone, lat, lon)

    return d, sign
