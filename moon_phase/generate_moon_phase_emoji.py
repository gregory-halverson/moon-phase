from .determine_moon_phase import determine_moon_phase

def generate_moon_phase_emoji(phase: str = None, use_face_emojis: bool = False) -> str:
    """
    Generate an emoji representing the current moon phase.

    Args:
        phase (str, optional): The moon phase as a string. If None, the current phase will be fetched.
        use_face_emojis (bool, optional): Whether to use face emojis for 'New' and 'Full' moon phases.

    Returns:
        str: The emoji representing the moon phase.

    Raises:
        ValueError: If an invalid moon phase is provided.
    """
    if phase is None:
        # Fetch the current moon phase if not provided
        phase = determine_moon_phase()

    # Determine the appropriate emoji based on the moon phase
    if phase == "New":
        emoji = "🌑" if not use_face_emojis else "🌚"
    elif phase == "Waxing Crescent":
        emoji = "🌒"
    elif phase == "First Quarter":
        emoji = "🌓"
    elif phase == "Waxing Gibbous":
        emoji = "🌔"
    elif phase == "Full":
        emoji = "🌕" if not use_face_emojis else "🌝"
    elif phase == "Waning Gibbous":
        emoji = "🌖"
    elif phase == "Last Quarter":
        emoji = "🌗"
    elif phase == "Waning Crescent":
        emoji = "🌘"
    else:
        # Raise an error if the moon phase is invalid
        raise ValueError(f"Invalid moon phase: {phase}")

    return emoji