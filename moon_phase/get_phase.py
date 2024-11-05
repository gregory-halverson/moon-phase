from datetime import datetime, timezone
from typing import Optional

from .next_phase import next_phase
from .preceding_intermediate_phase import preceding_intermediate_phase


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
