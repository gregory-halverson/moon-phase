from datetime import datetime
from pyluach.dates import HebrewDate

def generate_hebrew_date_string(dt: datetime = None) -> str:
    """
    Get the Hebrew date string for the given date.

    If no date is provided, the current date is used.

    Args:
        dt (datetime, optional): The Gregorian date for which to generate the Hebrew date string. Defaults to None.

    Returns:
        str: The Hebrew date string in the format "day month_name year".
    """
    if dt is None:
        # If no date is provided, use the current date
        dt = datetime.now()

    # Convert the Gregorian date to a Hebrew date
    hebrew_date = HebrewDate.from_pydate(dt)
    
    # Format the Hebrew date as a string
    formatted_date = f"{hebrew_date.day} {hebrew_date.month_name()} {hebrew_date.year}"

    return formatted_date