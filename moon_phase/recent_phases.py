from datetime import datetime, timezone, date
from zoneinfo import ZoneInfo
from typing import Optional, Union
import ephem

import ephem
import pandas as pd

from .process_time import process_time

def recent_phases(
        dt: Union[ephem.Date, datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> pd.DataFrame:
    """
    Calculates the dates of the previous new, first quarter,
    full, and last quarter moon relative to a given datetime.
    Defaults to the current datetime in the local timezone if none is provided.

    Args:
        dt: The datetime for which to calculate lunation dates.
            Defaults to datetime.now(timezone.utc).astimezone().
        timezone: The timezone for the output dates. If None (default),
            it uses the timezone of the input datetime.
        lat: The latitude for the observer's location. Optional.
        lon: The longitude for the observer's location. Optional.

    Returns:
        A pandas DataFrame with the lunation dates in a 'datetime' column and
        the corresponding lunation names in a 'lunation' column, sorted
        by datetime.
    """

    dt, timezone = process_time(dt, timezone, lat, lon)

    dt = ephem.Date(dt)

    data = {
        'Previous New': ephem.previous_new_moon(dt),
        'Previous First Quarter': ephem.previous_first_quarter_moon(dt),
        'Previous Full': ephem.previous_full_moon(dt),
        'Previous Last Quarter': ephem.previous_last_quarter_moon(dt)
    }

    # Convert ephem.Date objects to Python datetime objects with the specified timezone
    for key, value in data.items():
        dt_with_tz = value.datetime().replace(tzinfo=timezone.utc).astimezone(tz)
        data[key] = dt_with_tz

    df = pd.DataFrame({'lunation': data.keys(), 'datetime': data.values()})

    # Sort the DataFrame by datetime
    df.sort_values('datetime', inplace=True)
    return df
