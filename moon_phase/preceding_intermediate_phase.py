def preceding_intermediate_phase(phase: str) -> str:
    """
    Determines the intermediate moon phase that precedes the given principal phase.

    Args:
        phase: The principal moon phase (New Moon, First Quarter, Full Moon, or Last Quarter).

    Returns:
        The preceding intermediate moon phase as a string.
    """

    if phase == "New":
        return "Waning Crescent"
    elif phase == "First Quarter":
        return "Waxing Crescent"
    elif phase == "Full":
        return "Waxing Gibbous"
    elif phase == "Last Quarter":
        return "Waning Gibbous"
    else:
        raise ValueError(f"invalid moon phase: {phase}")
