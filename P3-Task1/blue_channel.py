
def blue_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject whose
    channels except for blue, have
    been zeroed, after being
    PASSED a Cimpl.Image object

    >>> blue_channel(Cimpl.load_image())
    -> An a green filtered image will be displayed
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(0, 0, b))
    return copy