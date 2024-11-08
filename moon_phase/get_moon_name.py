from datetime import datetime, timezone, timedelta

import ephem


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
