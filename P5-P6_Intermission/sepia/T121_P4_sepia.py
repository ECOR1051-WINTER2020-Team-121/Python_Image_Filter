
import Cimpl


def grayscale(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a grayscaled
    Cimpl.Image object after
    being PASSEDD a Cimpl.Image object.
    """
    img = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        avg = (r + g + b) / 3
        Cimpl.set_color(img, x, y, Cimpl.create_color(avg, avg, avg))
    Cimpl.save_as(img, 'grayscaled.png')
    return img


def sepia(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a sepia filtered
    Cimpl.Image object after
    being PASSED a Cimpl.Image object
    """
    img = Cimpl.copy(img)
    img = grayscale(img)

    for x, y, (r, g, b) in img:
        if r < 63:
            b *= 0.9
            r *= 1.1
        elif 63 <= r <= 191:
            b *= 0.85
            r *= 1.15
        else:
            b *= 0.93
            r *= 1.08
        Cimpl.set_color(img, x, y, Cimpl.create_color(r, g, b))
    Cimpl.save_as(img, 'sepiafied.png')
    return img
