import geocoder

def locate_device() -> tuple:
    """
    Locate the device's current position using IP geolocation.

    This function uses the geocoder library to get the latitude and longitude
    of the device based on its IP address.

    Returns:
        tuple: A tuple containing the latitude and longitude of the device.
    """
    # Get the latitude and longitude of the device using IP geolocation
    lat, lon = geocoder.ip('me').latlng

    return lat, lon
