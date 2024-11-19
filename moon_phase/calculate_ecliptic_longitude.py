from typing import Union
from datetime import datetime, date
from zoneinfo import ZoneInfo
import numpy as np
import ephem
import math

from .create_ephem_body import create_ephem_body
from .parse_timestamp import parse_timestamp
from .locate_device import locate_device
from .process_time import process_time

def julian_century(date: datetime) -> float:
    """
    Calculate the Julian Century (T) for a given date.
    
    Parameters:
    date (datetime): The input date.
    
    Returns:
    float: Julian Century (T)
    """
    jd = date.toordinal() + 1721424.5 + (date.hour / 24) + (date.minute / 1440) + (date.second / 86400)
    jd_j2000 = 2451545.0  # Julian Date for J2000.0
    return (jd - jd_j2000) / 36525

def calculate_obliquity_of_ecliptic(date: datetime) -> float:
    """
    Calculate the mean obliquity of the ecliptic for a given date.
    
    Parameters:
    date (datetime): The input date.
    
    Returns:
    float: The mean obliquity of the ecliptic in degrees.
    """
    T = julian_century(date)
    
    epsilon_0 = 84381.406  # Mean obliquity of the ecliptic at J2000.0 in arcseconds
    epsilon = epsilon_0 - (46.836769 * T) - (0.0001831 * T**2) + (0.000000093 * T**3) - (0.0000000002 * T**4)
    
    # Convert mean obliquity from arcseconds to degrees
    return epsilon / 3600.0  # arcseconds to degrees

def nutation_in_obliquity(date: datetime) -> float:
    """
    Calculate the nutation in the obliquity of the ecliptic for a given date.
    
    Parameters:
    date (datetime): The input date.
    
    Returns:
    float: Nutation in the obliquity in degrees.
    """
    T = julian_century(date)
    
    # Mean longitude of the Moon (in degrees)
    L = (218.3164477 + 481267.88123421 * T) % 360.0  # degrees
    
    # Longitude of the ascending node of the Moon (in degrees)
    Omega = (125.04452222 - 1934.13626197 * T) % 360.0  # degrees
    
    # Convert to radians
    Omega_rad = math.radians(Omega)
    
    # Nutation in obliquity (arcseconds)
    delta_epsilon = 0.00257 * math.sin(Omega_rad)  # First term approximation
    
    # Convert to degrees
    return delta_epsilon / 3600.0  # arcseconds to degrees

def true_obliquity_of_ecliptic(date: datetime) -> float:
    """
    Calculate the true obliquity of the ecliptic (mean obliquity + nutation).
    
    Parameters:
    date (datetime): The input date.
    
    Returns:
    float: The true obliquity of the ecliptic in degrees.
    """
    epsilon_mean = calculate_obliquity_of_ecliptic(date)
    delta_epsilon = nutation_in_obliquity(date)
    
    # True obliquity of the ecliptic
    return epsilon_mean + delta_epsilon

def calculate_ecliptic_longitude(
        body: Union[ephem.Body, str],
        dt: Union[ephem.Date, datetime, date, str] = None,
        timezone: Union[ZoneInfo, str] = None,
        lat: float = None,
        lon: float = None) -> float:
    """
    Calculate the ecliptic longitude of a celestial body.

    Parameters:
    body (Union[ephem.Body, str]): The celestial body to calculate the ecliptic longitude for.
                                   Can be an ephem.Body object or a string representing the body.
    dt (Union[ephem.Date, datetime, date, str], optional): The date and time for the calculation.
                                                           Can be an ephem.Date, datetime, date, or string.
                                                           Defaults to None.
    timezone (Union[ZoneInfo, str], optional): The timezone for the date and time. Can be a ZoneInfo object or a string.
                                               Defaults to None.
    lat (float, optional): The latitude of the observer. Defaults to None.
    lon (float, optional): The longitude of the observer. Defaults to None.

    Returns:
    float: The ecliptic longitude of the celestial body in degrees.
    """
    # If the body is provided as a string, create an ephem.Body object
    if isinstance(body, str):
        body = create_ephem_body(body)

    # If latitude or longitude is not provided, locate the device to get the coordinates
    if lat is None or lon is None:
        lat, lon = locate_device()

    # Process the date and time, and adjust for the provided timezone
    dt, timezone = process_time(dt, timezone, lat, lon)

    # Create an observer object with the provided or located coordinates and date/time
    observer = ephem.Observer()
    observer.lat = lat
    observer.lon = lon
    observer.date = dt

    # Compute the position of the celestial body for the observer
    body.compute(observer)

    # Get the right ascension and declination
    ra = body.g_ra  # Right ascension in radians
    dec = body.g_dec  # Declination in radians

    # Get the true obliquity of the ecliptic
    epsilon = np.radians(true_obliquity_of_ecliptic(dt))  # Convert to radians

    # Convert right ascension and declination to ecliptic longitude
    sin_lambda = np.sin(ra) * np.cos(epsilon) + np.tan(dec) * np.sin(epsilon)
    cos_lambda = np.cos(ra)

    # Compute ecliptic longitude in radians
    lambda_rad = np.arctan2(sin_lambda, cos_lambda)

    # Convert the result to degrees
    ecliptic_longitude_degrees = np.degrees(lambda_rad) % 360  # Normalize to 0-360 degrees

    return ecliptic_longitude_degrees