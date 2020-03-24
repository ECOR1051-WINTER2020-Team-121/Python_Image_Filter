
import Cimpl


def flip_horizontal(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image
    that was flipped, after
    being PASSED a Cimpl.Image object

    >>> flip_horizontal(Cimpl.load_image('filename'))
    """
    hgt = Cimpl.get_height(img)
    wth = Cimpl.get_width(img)
    mid_x = wth // 2
    copy = Cimpl.copy(img)
    for y in range(hgt):
        for x in range(mid_x):
            #r1, g1, b1 = Cimpl.get_color(img, x, y)
            #r2, g2, b2 = Cimpl.get_color(img, x, hgt-y)
            Cimpl.set_color(copy, x, y, Cimpl.get_color(img, wth-x-1, y))
            Cimpl.set_color(copy, wth-x-1, y, Cimpl.get_color(img, x, y))
    return copy
