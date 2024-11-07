from .get_phase import get_phase


def get_moon_phase_emoji(phase: str = None, use_face_emojis: bool = False) -> str:
    if phase is None:
        phase = get_phase()

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
        raise ValueError(f"Invalid moon phase: {phase}")

    return emoji
