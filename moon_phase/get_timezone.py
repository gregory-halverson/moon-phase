from timezonefinder import TimezoneFinder
from zoneinfo import ZoneInfo

def get_timezone(
        lat: float = None,
        lon: float = None) -> ZoneInfo:
    if lat is None or lon is None:
        lat, lon = get_location()

    timezone = ZoneInfo(TimezoneFinder().timezone_at(lng=lon, lat=lat))

    return timezone
