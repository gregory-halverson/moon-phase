from typing import Union
from datetime import datetime
import dateparser
from zoneinfo import ZoneInfo

from .get_timezone import get_timezone

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

    print(timezone)

    datetime = datetime.replace(tzinfo=timezone)

    return datetime
