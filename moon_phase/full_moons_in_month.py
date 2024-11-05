from datetime import timezone, datetime, timedelta
from typing import Optional

import ephem


def full_moons_in_month(year: Optional[int] = None, month: Optional[int] = None, tz: Optional[timezone] = None) -> list[datetime]:
    """
    Calculates the dates of all full moons occurring in a given month and year.
    Defaults to the current month and year in the local timezone.

    Args:
        year: The year. Defaults to the current year.
        month: The month (1-12). Defaults to the current month.
        tz: The timezone for the output dates. If None (default),
            it uses the local timezone.

    Returns:
        A list of datetime objects representing the full moons in the specified month.
    """

    if year is None:
        year = datetime.now().year
    if month is None:
        month = datetime.now().month
    if tz is None:
        tz = datetime.now(timezone.utc).astimezone().tzinfo  # Get local timezone

    # Start with the first day of the month
    dt = datetime(year, month, 1, tzinfo=tz)
    dt = ephem.Date(dt)

    full_moons = []

    full_moon_date = ephem.next_full_moon(dt).datetime().replace(tzinfo=timezone.utc).astimezone(tz)
    full_moons.append(full_moon_date)

    next_full_moon_date = ephem.next_full_moon(ephem.Date(full_moon_date + timedelta(days=1))).datetime().replace(tzinfo=timezone.utc).astimezone(tz)

    if next_full_moon_date.month == month:
        full_moons.append(next_full_moon_date)

    return full_moons
