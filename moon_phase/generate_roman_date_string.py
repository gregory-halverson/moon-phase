from datetime import datetime

def generate_roman_date_string(dt: datetime = None) -> str:
    """
    Generate a formatted date string in the format 'day month year'.
    
    If no date is provided, the current date and time will be used.
    
    Args:
        dt (datetime, optional): The date to format. Defaults to None.
        
    Returns:
        str: The formatted date string.
    """
    if dt is None:
        # Use the current date and time if no date is provided
        dt = datetime.now()
    
    # Format the date as 'day month year'
    formatted_date = f"{dt:%-d %B %Y}"

    return formatted_date