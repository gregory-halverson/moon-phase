from datetime import datetime, timezone
from typing import Optional

import ephem
import pandas as pd


def upcoming_phases(
        dt: Optional[datetime] = None,
        tz: Optional[timezone] = None) -> pd.DataFrame:
    """
    Calculates the dates of the next new, first quarter,
    full, and last quarter moon relative to a given datetime.
    Defaults to the current datetime in the local timezone if none is provided.

    Args:
        dt: The datetime for which to calculate lunation dates.
            Defaults to datetime.now(timezone.utc).astimezone().
        tz: The timezone for the output dates. If None (default),
            it uses the timezone of the input datetime.

    Returns:
        A pandas DataFrame with the lunation dates in a 'datetime' column and
        the corresponding lunation names in a 'lunation' column, sorted
        by datetime.
    """

    if dt is None:
        dt = datetime.now(timezone.utc).astimezone()  # Current datetime in local timezone

    # If tz is not provided, use the timezone of the input datetime
    if tz is None:
        tz = dt.tzinfo

    dt = ephem.Date(dt)

    data = {
        'Next New': ephem.next_new_moon(dt),
        'Next First Quarter': ephem.next_first_quarter_moon(dt),
        'Next Full': ephem.next_full_moon(dt),
        'Next Last Quarter': ephem.next_last_quarter_moon(dt)
    }

    # Convert ephem.Date objects to Python datetime objects with the specified timezone
    for key, value in data.items():
        dt_with_tz = value.datetime().replace(tzinfo=timezone.utc).astimezone(tz)
        data[key] = dt_with_tz

    df = pd.DataFrame({'lunation': data.keys(), 'datetime': data.values()})

    # Sort the DataFrame by datetime
    df.sort_values('datetime', inplace=True)
    return df
