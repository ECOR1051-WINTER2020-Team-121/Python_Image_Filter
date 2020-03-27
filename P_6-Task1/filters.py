
def combine(r_img: Cimpl.Image, g_img: Cimpl.Image, b_img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject where
    three Cimpl.Image objects are passed.
    Combines the color channels
    of the three arguments.

    >>> Cimpl.show(combine(Cimpl.load_image('red_image.png'), Cimpl.load_image('green_image.png'), Cimpl.load_image('blue_image.png'))
    -> a combination of the filtered images will be displayed.
    """
    base = Cimpl.copy(r_img)

    for x, y, (r, g, b) in base:
        g_r, g_g, g_b = Cimpl.get_color(g_img, x, y)
        b_r, b_g, b_b = Cimpl.get_color(b_img, x, y)
        color = Cimpl.create_color(compute_sum(r, g_r, b_r), compute_sum(g, g_g, b_g), compute_sum(b, g_b, b_b))
        Cimpl.set_color(base, x, y, color)

    return base


def compute_sum(r: int, g: int, b: int) -> int:
    """
    Author: Zakaria Ismail

    RETURNS the sum of three numbers
    PASSED. If sum exceeds 255, then
    the sum is 255.

    >> compute_sum(5,6,7)
    18
    """
    if r + g + b <= 255:
        return r + g + b
    else:
        return 255


def red_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject whose
    channels except for red, have
    been zeroed, after being
    PASSED a Cimpl.Image object

    >>> Cimpl.show(red_channel('p2-original.png'))
    -> An a red filtered image will be displayed
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(r, 0, 0))
    return copy


def flip_horizontal(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS a Cimpl.Image
    that was flipped, after
    being PASSED img

    img is a Cimpl.Image object

    >>> flip_horizontal(Cimpl.load_image(Cimpl.choose_file()))
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


def posterize(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an image where
    img has its RGB channels
    set to the midpoint of quadrants:
        0..63, 64..127, 128..191, and 192..255
    depending on where the color channel value is situated between

    img is a Cimpl.Image object passed to the function

    >>> posterize(Cimpl.load_image(Cimpl.choose_file()))
    -> A posterized image is returned
    """
    img = Cimpl.copy(img)
    for x, y, col in img:
        channels = []
        for ch in col:
            channels += [__adjust_component__(ch)]
        Cimpl.set_color(img, x, y, Cimpl.create_color(channels[0], channels[1], channels[1]))
    return img


def __adjust_component__(num: int) -> int:
    """
    Author: Zakaria Ismail

    RETURNS the midpoint of
    one of the following ranges,
        0-63, 64-127, 128-191, 192-255
    after being PASSED num.

    num is an integer between 0-255.

    >>> __adjust_component__(5)
    31
    """
    ranges = [63,127,191,255]
    mid = [31, 95, 159, 223]
    for i in range(len(ranges)):
        if num <= ranges[i]:
            return mid[i]
