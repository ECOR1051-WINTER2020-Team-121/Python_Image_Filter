import Cimpl


def green_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject whose
    channels except for green, have
    been zeroed, after being
    PASSED a Cimpl.Image object

    >>> Cimpl.show(green_channel(Cimpl.load_image(('p2-original.png')))
    -> An a green filtered image will be displayed
    """
    #img = Cimpl.load_image(img)
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(0, g, 0))
    #Cimpl.save_as(copy, SAVE_FILE_AS)
    return copy



