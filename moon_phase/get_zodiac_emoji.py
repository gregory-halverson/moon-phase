def get_zodiac_emoji(sign):
  """
  This function takes a zodiac sign name as a string and returns an emoji.

  Args:
    sign: The name of the zodiac sign.

  Returns:
    An emoji representing the zodiac sign, or None if the sign is not recognized.
  """

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

  zodiac_emoji = sign_emojis[sign]

  return zodiac_emoji
