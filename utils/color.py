def get_color_based_on_force(force, max_force):
    normalized_force = force / max_force
    
    if normalized_force < 0.33:
        # Low force: Blue color
        r = 0
        g = int(255 * (normalized_force / 0.33))
        b = 255
    elif normalized_force < 0.66:
        # Medium force: Green color
        r = 0
        g = 255
        b = int(255 * (1 - (normalized_force - 0.33) / 0.33))
    else:
        # High force: Red color
        r = 255
        g = int(255 * (1 - (normalized_force - 0.66) / 0.34))
        b = 0

    # Ensure RGB values are within the valid range
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    
    return (r, g, b)