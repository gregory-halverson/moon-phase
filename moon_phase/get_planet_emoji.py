def get_planet_emoji(planet: str) -> str:
    """
    This function takes the name of a traditional visible planet as a string
    and returns the corresponding emoji.

    Args:
        planet: The name of the planet (e.g., "Mercury", "Venus", "Mars", etc.)

    Returns:
        The corresponding emoji, or None if the planet is not recognized.
    """

    planet_emojis = {
        "mercury": "☿️",
        "venus": "♀️",
        "mars": "♂️",
        "jupiter": "♃",
        "saturn": "♄"
    }

    return planet_emojis.get(planet.lower(), None)