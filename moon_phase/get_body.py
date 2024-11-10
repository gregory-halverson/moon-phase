import ephem

def get_body(body_name: str):
    body_name = body_name.lower()

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
        raise ValueError(f"Unknown body: {body_name}")
    