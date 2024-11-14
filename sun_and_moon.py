import sys
from datetime import datetime

from timezonefinder import TimezoneFinder
import pytz
import geocoder

from moon_phase.parse_timestamp import parse_timestamp
from moon_phase import get_status
from moon_phase import get_location

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
        lat, lon = get_location()

    if timestamp is None:
        dt = datetime.now().astimezone()
    else:
        try:
            dt = parse_timestamp(timestamp, lat=lat, lon=lon)
        except (ValueError, pytz.UnknownTimeZoneError) as e:
            print(f"Invalid latitude/longitude or timezone error: {e}")
            sys.exit(1)

    print(get_status(dt, lat=lat, lon=lon))

if __name__ == "__main__":
    main()
