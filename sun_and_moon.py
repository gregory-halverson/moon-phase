import sys
from datetime import datetime, date

from timezonefinder import TimezoneFinder
import pytz
import geocoder

from moon_phase.parse_timestamp import parse_timestamp
from moon_phase import locate_device
from moon_phase import status_at_time
from moon_phase import status_on_date

def main():
    if len(sys.argv) > 1:
        timestamp = sys.argv[1]
    else:
        timestamp = None

    if len(sys.argv) > 3:
        try:
            lat = float(sys.argv[2])
            lon = float(sys.argv[3])
        except ValueError:
            print("Invalid latitude/longitude format.")
            sys.exit(1)
    else:
        lat, lon = locate_device()

    dt, timezone = parse_timestamp(timestamp)

    if isinstance(dt, datetime):
        print(f"Processing at time: {dt}")
        
        status = status_at_time(
            dt=dt, 
            timezone=timezone, 
            lat=lat, 
            lon=lon
        )
    elif isinstance(dt, date):
        print(f"Processing on date: {dt}")
        
        status = status_on_date(
            d=dt, 
            timezone=timezone, 
            lat=lat, 
            lon=lon
        )
    else:
        raise ValueError(f"Invalid date/time format: {type(dt)}")
    
    print(status)

if __name__ == "__main__":
    main()
