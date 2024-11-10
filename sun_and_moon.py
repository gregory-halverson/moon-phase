import sys
from datetime import datetime
from moon_phase import get_status
from timezonefinder import TimezoneFinder
import pytz
import geocoder

def main():
    if len(sys.argv) > 1:
        date_str = sys.argv[1]
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            sys.exit(1)
    else:
        date = datetime.now().astimezone().date()

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

    try:
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lng=longitude, lat=latitude)
        if timezone_str is None:
            raise ValueError("Could not determine timezone.")
        timezone = pytz.timezone(timezone_str)
    except (ValueError, pytz.UnknownTimeZoneError) as e:
        print(f"Invalid latitude/longitude or timezone error: {e}")
        sys.exit(1)

    print(f"Date: {date}, Timezone: {timezone}")

    print(get_status(date))

if __name__ == "__main__":
    main()