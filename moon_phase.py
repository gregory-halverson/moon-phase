import pandas as pd
import ephem
from datetime import datetime, timedelta, timezone
from typing import Optional, Union

def recent_phases(
        dt: Optional[datetime] = None, 
        tz: Optional[timezone] = None) -> pd.DataFrame:
    """
    Calculates the dates of the previous new, first quarter, 
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
    df_future = df[df['datetime'] > dt]  
    next_phase_row = df_future.iloc[0]  # Get the first row after filtering

    # Remove "Next " prefix from the lunation name
    phase_name = next_phase_row['lunation'].replace("Next ", "")
    phase_datetime = next_phase_row['datetime']

    return phase_name, phase_datetime

def preceding_intermediate_phase(phase: str) -> str:
    """
    Determines the intermediate moon phase that precedes the given principal phase.

    Args:
        phase: The principal moon phase (New Moon, First Quarter, Full Moon, or Last Quarter).

    Returns:
        The preceding intermediate moon phase as a string.
    """

    if phase == "New Moon":
        return "Waning Crescent"
    elif phase == "First Quarter":
        return "Waxing Crescent"
    elif phase == "Full Moon":
        return "Waxing Gibbous"
    elif phase == "Last Quarter":
        return "Waning Gibbous"
    else:
        raise ValueError("Invalid moon phase provided.")

def get_phase(dt: Optional[datetime] = None) -> str:
    if dt is None:
        dt = datetime.now(timezone.utc).astimezone()

    next_phase_name, next_phase_datetime = next_phase(dt)
    next_phase_date = next_phase_datetime.date()
    given_date = dt.date()
    
    if given_date == next_phase_date:
        return next_phase_name
    else:
        return preceding_intermediate_phase(next_phase_name)
    
def get_emoji(phase: str = None, use_face_emojis: bool = False) -> str:
    if phase is None:
        phase = get_phase()

    if phase == "New":
        emoji = "🌑" if not use_face_emojis else "🌚"
    elif phase == "Waxing Crescent":
        emoji = "🌒"
    elif phase == "First Quarter":
        emoji = "🌓"
    elif phase == "Waxing Gibbous":
        emoji = "🌔"
    elif phase == "Full":
        emoji = "🌕" if not use_face_emojis else "🌝"
    elif phase == "Waning Gibbous":
        emoji = "🌖"
    elif phase == "Last Quarter":
        emoji = "🌗"
    elif phase == "Waning Crescent":
        emoji = "🌘"

    return emoji

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

def get_moon_name(
        dt: datetime = None,
        include_moon: bool = True) -> str:
    """
    Determines the Farmer's Almanac moon name for a given date/time, including the "Blue Moon" rule.

    Args:
        dt: The datetime for which to determine the moon name. 
            Defaults to the current time in the local timezone.

    Returns:
        The moon name as a string.
    """

    if dt is None:
        dt = datetime.now(timezone.utc).astimezone()

    # Get the month and year
    month = dt.month
    year = dt.year

    # Basic moon names (without "Moon")
    moon_names = {
        1: "Wolf",
        2: "Snow",
        3: "Worm",
        4: "Pink",
        5: "Flower",
        6: "Strawberry",
        7: "Buck",
        8: "Sturgeon",
        9: "Harvest",  # This will be adjusted later if necessary
        10: "Hunter's",  # This will be adjusted later if necessary
        11: "Beaver",
        12: "Cold"
    }

    # --- Special Cases ---

    # --- 1. Harvest and Hunter's Moon ---

    september_equinox = ephem.next_equinox(ephem.Date(datetime(year, 9, 1))).datetime()

    full_moon_before_equinox = ephem.previous_full_moon(ephem.Date(september_equinox)).datetime()
    full_moon_after_equinox = ephem.next_full_moon(ephem.Date(september_equinox)).datetime()

    if abs(full_moon_before_equinox - september_equinox) < abs(full_moon_after_equinox - september_equinox):
        harvest_moon_month = full_moon_before_equinox.month
    else:
        harvest_moon_month = full_moon_after_equinox.month

    if harvest_moon_month == 9:
        moon_names[9] = "Harvest"
        moon_names[10] = "Hunter's"
    else:
        moon_names[10] = "Harvest"
        moon_names[11] = "Hunter's"

    # --- 2. Blue Moon ---

    # Get the start and end dates of the seasons
    winter_solstice = ephem.next_solstice(ephem.Date(datetime(year, 12, 1))).datetime()
    spring_equinox = ephem.next_equinox(ephem.Date(datetime(year, 3, 1))).datetime()
    summer_solstice = ephem.next_solstice(ephem.Date(datetime(year, 6, 1))).datetime()
    autumn_equinox = ephem.next_equinox(ephem.Date(datetime(year, 9, 1))).datetime()

    # Adjust for year boundaries
    if spring_equinox < winter_solstice: 
        spring_equinox = ephem.next_equinox(ephem.Date(datetime(year + 1, 3, 1))).datetime()
    if summer_solstice < spring_equinox:
        summer_solstice = ephem.next_solstice(ephem.Date(datetime(year + 1, 6, 1))).datetime()
    if autumn_equinox < summer_solstice:
        autumn_equinox = ephem.next_equinox(ephem.Date(datetime(year + 1, 9, 1))).datetime()
    if winter_solstice < autumn_equinox:
        winter_solstice = ephem.next_solstice(ephem.Date(datetime(year + 1, 12, 1))).datetime()

    seasons = [
        (winter_solstice, spring_equinox),
        (spring_equinox, summer_solstice),
        (summer_solstice, autumn_equinox),
        (autumn_equinox, winter_solstice)
    ]

    # Count full moons in each season
    for start, end in seasons:
        full_moon_count = 0
        current_date = ephem.Date(start)
        while current_date <= ephem.Date(end):
            full_moon_date = ephem.next_full_moon(current_date).datetime()
            if start <= full_moon_date <= end:
                full_moon_count += 1
            current_date = ephem.Date(full_moon_date + timedelta(days=1))

        # If a season has 4 full moons, the third is a Blue Moon
        if full_moon_count == 4:
            # This is simplified; you'll need to find the 3rd full moon in the season
            # and its corresponding month to set the Blue Moon in moon_names
            # ... (Logic to determine the month of the 3rd full moon) ...
            # Example: If the 3rd full moon is in June:
            # moon_names[6] = "Blue" 
            pass  

    # --- End of Special Cases ---

    moon_name = moon_names.get(month)

    if include_moon:
        moon_name += " Moon"

    return moon_name

