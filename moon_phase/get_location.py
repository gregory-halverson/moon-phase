import geocoder

def get_location() -> tuple:
    return geocoder.ip('me').latlng
