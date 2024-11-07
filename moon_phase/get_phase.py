from datetime import datetime, timezone, date
from typing import Optional, Union

from .next_phase import next_phase
from .preceding_intermediate_phase import preceding_intermediate_phase


def get_phase(dt: Optional[Union[datetime, date]] = None) -> str:
    if dt is None:
        dt = datetime.now(timezone.utc).astimezone()
    
    if isinstance(dt, date):
        if hasattr(dt, "tzinfo"):
            tzinfo = dt.tzinfo
        else:
            tzinfo = datetime.now().astimezone().tzinfo
        
        # convert date to datetime at midnight
        dt = datetime(dt.year, dt.month, dt.day, 0, 0, 0, 0, tzinfo=tzinfo)

    next_phase_name, next_phase_datetime = next_phase(dt)
    next_phase_date = next_phase_datetime.date()
    given_date = dt.date()

    if given_date == next_phase_date:
        return next_phase_name
    else:
        return preceding_intermediate_phase(next_phase_name)
