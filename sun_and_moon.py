import sys
from datetime import datetime

from timezonefinder import TimezoneFinder
import pytz
import geocoder

from moon_phase.parse_timestamp import parse_timestamp
from moon_phase import get_status

def main():
    # if len(sys.argv) > 1:
    #     date_str = sys.argv[1]
    #     try:
    #         date = datetime.strptime(date_str, "%Y-%m-%d").date()
    #     except ValueError:
    #         print("Invalid date format. Please use YYYY-MM-DD.")
    #         sys.exit(1)
    # else:
    #     date = datetime.now().astimezone().date()

    if len(sys.argv) > 1:
        timestamp = sys.argv[1]
    else:
        timestamp = None

    if len(sys.argv) > 3:
        try:
            latitude = float(sys.argv[2])
            longitude = float(sys.argv[3])
        except ValueError:
            print("Invalid latitude/longitude format.")
            sys.exit(1)
    else:
        g = geocoder.ip('me')
        latitude = g.latlng[0]
        longitude = g.latlng[1]

    if timestamp is None:
        dt = datetime.now().astimezone().date()
    else:
        try:
            dt = parse_timestamp(timestamp, lat=latitude, lon=longitude)
        except (ValueError, pytz.UnknownTimeZoneError) as e:
            print(f"Invalid latitude/longitude or timezone error: {e}")
            sys.exit(1)

    print(f"{dt} {dt.tzinfo}")

    print(get_status(dt))

if __name__ == "__main__":
    main()
