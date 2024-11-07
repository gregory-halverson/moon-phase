def get_planet_emoji(planet: str) -> str:
  """
  This function takes the name of a traditional visible planet as a string
  and returns the corresponding emoji.

  Args:
    planet: The name of the planet (e.g., "Mercury", "Venus", "Mars", etc.)

  Returns:
    The corresponding emoji, or None if the planet is not recognized.
  """

  planet = planet.lower()  # Convert input to lowercase for case-insensitive matching
  
  if planet == "mercury":
    return "☿️"
  elif planet == "venus":
    return "♀️"
  elif planet == "mars":
    return "♂️"
  elif planet == "jupiter":
    return "♃"
  elif planet == "saturn":
    return "♄"
  else:
    return None  # Return None for invalid planet names