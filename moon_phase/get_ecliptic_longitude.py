from typing import Union
from datetime import datetime, date
from zoneinfo import ZoneInfo

import numpy as np

import ephem

from .get_body import get_body
from .parse_timestamp import parse_timestamp

def get_ecliptic_longitude(
        body: Union[ephem.Body, str],
        dt: Union[datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> float:
    if isinstance(body, str):
        body = get_body(body)

    if lat is None or lon is None:
        lat, lon = get_location()

    if dt is None:
        dt = datetime.now()

    if not isinstance(dt, datetime) or dt.tzinfo is None:
        dt = parse_timestamp(dt, timezone, lat, lon)

    observer = ephem.Observer()
    observer.lat = lat
    observer.lon = lon
    observer.date = dt

    # moon = ephem.Moon(observer)
    body.compute(observer)

    ecliptic_longitude_degrees = np.degrees(body.g_ra)

    return ecliptic_longitude_degrees
