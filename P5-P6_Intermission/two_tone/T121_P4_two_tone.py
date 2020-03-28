import Cimpl


def two_tone(img: Cimpl.Image, tone_a: str, tone_b: str) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object
    that was turned into a two toned image.
    Is PASSED a Cimpl.Image object,
    and two strings
    """
    COLOURS = {
        'black': Cimpl.Color(0, 0, 0),
        'white': Cimpl.Color(255, 255, 255),
        'red': Cimpl.Color(255, 0, 0),
        'lime': Cimpl.Color(0, 255, 0),
        'blue': Cimpl.Color(0, 0, 255),
        'yellow': Cimpl.Color(255, 255, 0),
        'cyan': Cimpl.Color(0, 255, 255),
        'magenta': Cimpl.Color(255, 0, 255),
        'gray': Cimpl.Color(128, 128, 128)
    }

    img = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        brightness = (r + g + b) / 3
        if brightness <= 127:
            Cimpl.set_color(img, x, y, COLOURS[tone_a])
        else:
            Cimpl.set_color(img, x, y, COLOURS[tone_b])
    return img
