from datetime import datetime, timezone, date
from zoneinfo import ZoneInfo
from typing import Optional, Union
import ephem

from .process_time import process_time
from .upcoming_phases import upcoming_phases


def find_next_phase(
        dt: Union[ephem.Date, datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> tuple[str, datetime]:
    """
    Calculates the next moon phase: New, First Quarter, Full, or
    Last Quarter.

    Args:
        dt: The datetime from which to determine the next phase.
            Defaults to present time in the local timezone.
        timezone: The timezone for the output datetime. Defaults to the timezone of the input date/time.
        lat: The latitude for the location to determine the moon phase.
        lon: The longitude for the location to determine the moon phase.

    Returns:
        A tuple containing the name of the next lunation and its datetime.
    """

    dt, timezone = process_time(dt, timezone, lat, lon)

    df = upcoming_phases(dt, timezone, lat, lon)  # Use only future dates

    # Filter for datetimes strictly greater than the input datetime
    # (This might be redundant now, but it's good to keep for safety)
    # df_future = df[df['datetime'] > dt]
    next_phase_row = df.iloc[0]  # Get the first row after filtering

    # Remove "Next " prefix from the lunation name
    phase_name = next_phase_row['lunation'].replace("Next ", "")
    phase_datetime = next_phase_row['datetime']

    return phase_name, phase_datetime
