from datetime import datetime, timezone
from typing import Optional

from .upcoming_phases import upcoming_phases


def next_phase(
        dt: Optional[datetime] = None,
        tz: Optional[timezone] = None) -> tuple[str, datetime]:
    """
    Calculates the next moon phase: New, First Quarter, Full, or
    Last Quarter.

    Args:
        dt: The datetime from which to determine the next phase.
            Defaults to present time in the local timezone.
        tz: The timezone for the output datetime. Defaults to the timezone of the input date/time.

    Returns:
        A tuple containing the name of the next lunation and its datetime.
    """

    if dt is None:
        dt = datetime.now(timezone.utc).astimezone()

    df = upcoming_phases(dt, tz)  # Use only future dates

    # Filter for datetimes strictly greater than the input datetime
    # (This might be redundant now, but it's good to keep for safety)
    # df_future = df[df['datetime'] > dt]
    next_phase_row = df.iloc[0]  # Get the first row after filtering

    # Remove "Next " prefix from the lunation name
    phase_name = next_phase_row['lunation'].replace("Next ", "")
    phase_datetime = next_phase_row['datetime']

    return phase_name, phase_datetime
