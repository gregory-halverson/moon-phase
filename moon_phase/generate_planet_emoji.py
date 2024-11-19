def generate_planet_emoji(planet: str, use_graphical: bool = True) -> str:
    """
    This function takes the name of a traditional visible planet as a string
    and returns the corresponding emoji. The function supports both graphical
    emojis and unicode symbols for the planets.

    Args:
        planet (str): The name of the planet (e.g., "Mercury", "Venus", "Mars", etc.)
        use_graphical (bool): If True, returns graphical emojis. If False, returns unicode symbols.

    Returns:
        str: The corresponding emoji or unicode symbol, or None if the planet is not recognized.
    """

    # Dictionary mapping planet names to graphical emojis
    planet_emojis = {
        "sun": "🌞",
        "moon": "🌝",
        "mercury": "🐦‍⬛",
        "venus": "💖",
        "mars": "🗡️",
        "jupiter": "⚡️",
        "saturn": "⏳"
    }

    # Dictionary mapping planet names to unicode symbols
    planet_unicode = {
        "mercury": "☿️",
        "venus": "♀️",
        "mars": "♂️",
        "jupiter": "♃",
        "saturn": "♄"
    }

    # Check if graphical emojis should be used
    if use_graphical:
        # Get the graphical emoji for the given planet name
        emoji = planet_emojis.get(planet.lower(), None)
    else:
        # Get the unicode symbol for the given planet name
        emoji = planet_unicode.get(planet.lower(), None)

    return emoji