import Cimpl


def combine(r_img, g_img, b_img):
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject where
    three ImageObjects are PASSED.

    FUNCTION combines the three images'
    corresponding colour channels in
    each pixel.

    Note: Passed ImageObjects must have
    the same width and height
    """
    img = Cimpl.copy(r_img)    # set red image as the base
    hgt = Cimpl.get_height(img)
    wth = Cimpl.get_width(img)

    for y in range(hgt):
        for x in range(wth):
            r_red, g_red, b_red = Cimpl.get_color(r_img, x, y)
            r_green, g_green, b_green = Cimpl.get_color(g_img, x, y)
            r_blue, g_blue, b_blue = Cimpl.get_color(b_img, x, y)
            Cimpl.set_color(img, x, y, Cimpl.create_color(r_red+r_green+r_blue, g_red+g_green+g_blue, b_red+b_green+b_blue))
    return img


def red_channel(img):
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject where
    every pixel's channels except for
    red have been set to 0.
    """
    hgt = Cimpl.get_height(img)
    wth = Cimpl.get_width(img)

    for y in range(hgt):
        for x in range(wth):
            r, g, b = Cimpl.get_color(img, x, y)
            Cimpl.set_color(img, x, y, Cimpl.create_color(r, 0, 0))
    return img


def blue_channel(img):
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject where
    every pixel's channels except for
    red have been set to 0.
    """
    hgt = Cimpl.get_height(img)
    wth = Cimpl.get_width(img)

    for y in range(hgt):
        for x in range(wth):
            r, g, b = Cimpl.get_color(img, x, y)
            Cimpl.set_color(img, x, y, Cimpl.create_color(0, 0, b))
    return img


def green_channel(img):
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject where
    every pixel's channels except for
    red have been set to 0.
    """
    hgt = Cimpl.get_height(img)
    wth = Cimpl.get_width(img)

    for y in range(hgt):
        for x in range(wth):
            r, g, b = Cimpl.get_color(img, x, y)
            Cimpl.set_color(img, x, y, Cimpl.create_color(0, g, 0))
    return img

img = Cimpl.load_image('p2-original.jpg')

Cimpl.show(img)

combined = combine(red_channel(img), green_channel(img), blue_channel(img))

Cimpl.show(combined)
