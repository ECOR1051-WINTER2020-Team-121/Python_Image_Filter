
import Cimpl


def extreme_contrast(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object
    with pixels of extreme contrast,
    after being PASSED a Cimpl.Image object.
    """
    copy = Cimpl.copy(img)
    for x, y, col in img:
        channels = []
        for ch in col:
            if ch < 128:
                channels += [0]
            else:
                channels += [255]
        Cimpl.set_color(copy, x, y, Cimpl.create_color(channels[0], channels[1], channels[2]))
    return copy

