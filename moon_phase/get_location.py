import geocoder

def get_location() -> tuple:
    lat, lon = geocoder.ip('me').latlng

    return lat, lon
