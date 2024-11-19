import ephem

def create_ephem_body(body_name: str) -> ephem.Body:
    """
    Create an ephem body object based on the given body name.

    Parameters:
    body_name (str): The name of the celestial body (e.g., 'sun', 'moon', 'mars').

    Returns:
    ephem.Body: An ephem body object corresponding to the given body name.

    Raises:
    ValueError: If the body name is unknown.
    """
    # Convert the body name to lowercase to ensure case-insensitive matching
    body_name = body_name.lower()

    # Return the corresponding ephem body object based on the body name
    if body_name == "sun":
        return ephem.Sun()
    elif body_name == "moon":
        return ephem.Moon()
    elif body_name == "mercury":
        return ephem.Mercury()
    elif body_name == "venus":
        return ephem.Venus()
    elif body_name == "mars":
        return ephem.Mars()
    elif body_name == "jupiter":
        return ephem.Jupiter()
    elif body_name == "saturn":
        return ephem.Saturn()
    else:
        # Raise an error if the body name is not recognized
        raise ValueError(f"Unknown body: {body_name}")