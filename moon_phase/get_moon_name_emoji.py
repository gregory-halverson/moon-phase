from .get_moon_name import get_moon_name

def get_moon_name_emoji(moon_name: str = None) -> str:
    """
    Returns an emoji corresponding to the given moon name.

    Args:
        moon_name: The name of the moon as a string (without "Moon").

    Returns:
        An emoji representing the moon name.
    """

    if moon_name is None:
        moon_name = get_moon_name(include_moon=False)

    MOON_EMOJI = {
        "Wolf": "🐺",
        "Snow": "☃️",
        "Worm": "🪱",
        "Pink": "🌸",
        "Flower": "🌼",
        "Strawberry": "🍓",
        "Buck": "🦌",
        "Sturgeon": "🐟",
        "Harvest": "🌾",
        "Hunter's": "🏹",
        "Beaver": "🦫",
        "Cold": "🥶",
        "Blue": "🔵"  
    }

    moon_name_emoji = MOON_EMOJI[moon_name]

    return moon_name_emoji