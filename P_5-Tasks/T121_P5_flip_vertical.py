
import Cimpl


def flip_vertical(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image
    that was flipped, after
    being PASSED a Cimpl.Image object
    """
    hgt = Cimpl.get_height(img)
    mid_y = hgt // 2
    wth = Cimpl.get_width(img)
    copy = Cimpl.copy(img)
    for y in range(mid_y):
        for x in range(wth):
            #r1, g1, b1 = Cimpl.get_color(img, x, y)
            #r2, g2, b2 = Cimpl.get_color(img, x, hgt-y)
            Cimpl.set_color(copy, x, y, Cimpl.get_color(img, x, hgt-y-1))
            Cimpl.set_color(copy, x, hgt-y-1, Cimpl.get_color(img, x, y))
    return copy