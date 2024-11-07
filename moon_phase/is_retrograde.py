from typing import Union
from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import ephem

from .get_sign import parse_timestamp
from .get_sign import get_body
from .get_sign import get_ecliptic_longitude
from .get_sign import get_location

def is_retrograde(
        body: Union[ephem.Body, str],
        dt: Union[datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> bool:
    if isinstance(body, str):
        body = get_body(body)

    if not isinstance(body, (ephem.Mercury, ephem.Venus, ephem.Mars, ephem.Jupiter, ephem.Saturn)):
        return False

    if lat is None or lon is None:
        lat, lon = get_location()

    if dt is None:
        dt = datetime.now()
    
    if not isinstance(dt, datetime) or dt.tzinfo is None:
        dt = parse_timestamp(dt, timezone, lat, lon)

    ecliptic_longitude_degrees = get_ecliptic_longitude(body, dt, timezone, lat, lon)
    previous_day_ecliptic_longitude_degrees = get_ecliptic_longitude(body, dt - timedelta(days=1), timezone, lat, lon)
    difference = ecliptic_longitude_degrees - previous_day_ecliptic_longitude_degrees
    is_retrograde = difference < 0

    return is_retrograde
