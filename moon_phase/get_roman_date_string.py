from datetime import datetime

def get_roman_date_string(dt: datetime = None) -> str:
    if dt is None:
        dt = datetime.now()
    
    formatted_date = f"{dt:%-d %B %Y}"

    return formatted_date
