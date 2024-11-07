from datetime import datetime
from pyluach.dates import HebrewDate

def get_hebrew_date_string(dt: datetime = None) -> str:
    """
    Get the Hebrew date string for the given date.
    """
    if dt is None:
        dt = datetime.now()

    hebrew_date = HebrewDate.from_pydate(dt)
    formatted_date = f"{hebrew_date.day} {hebrew_date.month_name()} {hebrew_date.year}"

    return formatted_date
