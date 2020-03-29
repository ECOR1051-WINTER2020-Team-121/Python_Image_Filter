import Cimpl


def flip_horizontal(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object
    where img is flipped horizontally

    >>> flip_horizontal(Cimpl.create_image(1,1))
    """
    hgt = Cimpl.get_height(img)
    wth = Cimpl.get_width(img)
    mid_x = wth // 2
    copy = Cimpl.copy(img)
    for y in range(hgt):
        for x in range(mid_x):
            Cimpl.set_color(copy, x, y, Cimpl.get_color(img, wth-x-1, y))
            Cimpl.set_color(copy, wth-x-1, y, Cimpl.get_color(img, x, y))

    return copy

