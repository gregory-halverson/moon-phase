from datetime import datetime, timezone, date
from zoneinfo import ZoneInfo
from typing import Optional, Union

import ephem

from .process_time import process_time
from .find_next_phase import find_next_phase
from .preceding_intermediate_phase import preceding_intermediate_phase

def determine_moon_phase(
        dt: Union[ephem.Date, datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> str:
    """
    Determine the moon phase for a given date and location.

    Parameters:
    dt (Union[ephem.Date, datetime, date, str]): The date and time for which to determine the moon phase.
    timezone (Union[ZoneInfo, str]): The timezone of the given date and time.
    lat (float): The latitude of the location.
    lon (float): The longitude of the location.

    Returns:
    str: The name of the moon phase.
    """
    # Process the input date, time, and location to get a datetime object and timezone
    dt, timezone = process_time(dt, timezone, lat, lon)

    # Get the next moon phase name and its datetime
    next_phase_name, next_phase_datetime = find_next_phase(dt)
    next_phase_date = next_phase_datetime.date()
    given_date = dt.date()

    # If the given date is the same as the next phase date, return the next phase name
    if given_date == next_phase_date:
        return next_phase_name
    else:
        # Otherwise, return the preceding intermediate phase name
        return preceding_intermediate_phase(next_phase_name)