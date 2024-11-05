from typing import Union
import ephem
import geocoder
from datetime import datetime, date, timedelta
from datetime import timezone as dt_timezone
from dateutil import parser
import dateparser
from timezonefinder import TimezoneFinder
from zoneinfo import ZoneInfo
import pytz
from dateutil import tz
import numpy as np

ZODIAC_SIGNS = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces"
]

def get_location() -> tuple:
    return geocoder.ip('me').latlng

def get_timezone(
        lat: float = None, 
        lon: float = None) -> ZoneInfo:
    if lat is None or lon is None:
        lat, lon = get_location()
        
    timezone = ZoneInfo(TimezoneFinder().timezone_at(lng=lon, lat=lat))

    return timezone

def parse_timestamp(
        timestamp: str, 
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None, 
        lon: float = None) -> datetime:
    if not isinstance(timestamp, str):
        timestamp = str(timestamp)

    datetime = dateparser.parse(timestamp)

    if datetime.tzinfo is not None and timezone is None:
        return datetime
    elif timezone is None:
        if lat is None or lon is None:
            lat, lon = get_location()

        timezone = get_timezone(lat, lon)
    else:
        timezone = ZoneInfo(timezone)

    datetime = datetime.replace(tzinfo=timezone)

    return datetime

def get_body(body_name: str):
    body_name = body_name.lower()
    
    if body_name == "sun":
        return ephem.Sun()
    elif body_name == "moon":
        return ephem.Moon()
    elif body_name == "mercury":
        return ephem.Mercury()
    elif body_name == "venus":
        return ephem.Venus()
    elif body_name == "mars":
        return ephem.Mars()
    elif body_name == "jupiter":
        return ephem.Jupiter()
    elif body_name == "saturn":
        return ephem.Saturn()
    else:
        raise ValueError(f"Unknown body: {body_name}")
    
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

def tropical_zodiac_from_ecliptic_longitude(ecliptic_longitude_degrees: float) -> str:
    return ZODIAC_SIGNS[int(ecliptic_longitude_degrees / 30)]

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

def get_moon_sign(
        dt: Union[datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    return get_sign(ephem.Moon(), dt, timezone, lat, lon)
