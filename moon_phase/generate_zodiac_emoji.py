def generate_zodiac_emoji(sign, use_animal_emojis=True):
  """
  This function takes a zodiac sign name as a string and returns an emoji.

  Args:
    sign (str): The name of the zodiac sign.
    use_animal_emojis (bool): If True, use animal emojis; otherwise, use sign emojis. Default is True.

  Returns:
    str: An emoji representing the zodiac sign, or None if the sign is not recognized.
  """

  # Dictionary mapping zodiac signs to their corresponding animal emojis
  animal_emojis = {
      "Aries": "🐏",
      "Taurus": "🐂",
      "Gemini": "👯",
      "Cancer": "🦀",
      "Leo": "🦁",
      "Virgo": "👰",
      "Libra": "⚖️",
      "Scorpio": "🦂",
      "Sagittarius": "🏹",
      "Capricorn": "🐐",
      "Aquarius": "🏺",
      "Pisces": "🐟"
  }

  # Dictionary mapping zodiac signs to their corresponding sign emojis
  sign_emojis = {
      "Aries": "♈️",
      "Taurus": "♉️",
      "Gemini": "♊️",
      "Cancer": "♋️",
      "Leo": "♌️",
      "Virgo": "♍️",
      "Libra": "♎️",
      "Scorpio": "♏️",
      "Sagittarius": "♐️",
      "Capricorn": "♑️",
      "Aquarius": "♒️",
      "Pisces": "♓️"
  }

  # Select the appropriate emoji based on the use_animal_emojis flag
  if use_animal_emojis:
    zodiac_emoji = animal_emojis.get(sign)
  else:
    zodiac_emoji = sign_emojis.get(sign)

  return zodiac_emoji