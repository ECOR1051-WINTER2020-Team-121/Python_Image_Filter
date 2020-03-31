"""
Milestone 3
Team Identifier: 121
Contributing Members: Zakaria Ismail, Ibrahim Kasim, Himanshu Singh, Yanglong Liu
"""

import Cimpl


def red_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Himanshu Singh

    RETURNS an ImageObject whose
    channels except for red, have
    been zeroed, after being
    PASSED img

    img is a Cimpl.Image object

    >>> red_channel(Cimpl.load_image(Cimpl.choose_file()))
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(r, 0, 0))
    return copy


def green_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Ibrahim Kasim

    RETURNS an ImageObject whose
    channels except for green, have
    been zeroed, after being
    PASSED img

    img is a Cimpl.Image object

    >>> green_channel(Cimpl.load_image(Cimpl.choose_file()))
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(0, g, 0))
    return copy


def blue_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Yanglong Liu

    RETURNS an ImageObject whose
    channels except for green, have
    been zeroed, after being
    PASSED img

    img is a Cimpl.Image object

    >>> blue_channel(Cimpl.load_image(Cimpl.choose_file()))
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(0, 0, b))
    return copy


def combine(img_1: Cimpl.Image, img_2: Cimpl.Image, img_3: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS a Cimpl.Image object
    where color channel values of
    img_1, img_2, and img_3 have been combined.

    img_1, img_2, and img_3 are Cimpl.Image objects PASSED to the function.

    >>> combine(Cimpl.load_image(Cimpl.choose_file()), Cimpl.load_image(Cimpl.choose_file()), Cimpl.load_image(Cimpl.choose_file()))
    """
    base = Cimpl.copy(img_1)

    for x, y, (r, g, b) in base:
        r3, g3, b3 = Cimpl.get_color(img_3, x, y)
        r2, g2, b2 = Cimpl.get_color(img_2, x, y)
        color = Cimpl.Color(r+r2+r3, g+g2+g3, b+b2+b3)
        Cimpl.set_color(base, x, y, color)

    return base


def detect_edges(img: Cimpl.Image, thres: int) -> Cimpl.Image:
    """
    Author: Ibrahim Kasim

    RETURNS a Cimpl.Image object
    whose pixels have been changed
    to black or white depending on its
    contrast with the pixel below it after
    being PASSED img and thres

    img is a Cimpl.Image object

    thres is a integer

    >>> detect_edges(Cimpl.load_image(choose_file()), 10)
    """
    black = Cimpl.Color(0, 0, 0)
    white = Cimpl.Color(255, 255, 255)
    copy = Cimpl.copy(img)
    hgt = Cimpl.get_height(copy)

    for x, y, (r, g, b) in copy:
        if y+1 < hgt:   # checks if pixel below exists
            r2, g2, b2 = Cimpl.get_color(copy, x, y+1)
            contrast = abs((r + g + b)/3 - (r2 + g2 + b2)/3)
            if contrast > thres:
                col = black
            else:
                col = white
            Cimpl.set_color(copy, x, y, col)
        else:
            Cimpl.set_color(copy, x, y, white)
    return copy


def detect_edges_better(img: Cimpl.Image, thres: int) -> Cimpl.Image:
    """
    Author: Yanglong Liu

    RETURNS a Cimpl.Image object
    whose pixels have been changed
    to black or white depending on its
    contrast with the pixel below or to the
    right of it, after
    being PASSED img and thres

    img is a Cimpl.Image object

    thres is a integer

    >>> detect_edges_better(Cimpl.load_image(choose_file()), 4)
    """
    black = Cimpl.Color(0, 0, 0)
    white = Cimpl.Color(255, 255, 255)
    copy = Cimpl.copy(img)
    hgt = Cimpl.get_height(copy)
    wth = Cimpl.get_width(copy)

    for x, y, (r, g, b) in copy:
        is_bottom_row = not y+1 < hgt
        is_right_column = not x+1 < wth
        # if y+1 < hgt and x+1 < wth:   # checks if pixel below and to the right exist
        if not is_bottom_row:
            if not is_right_column:
                r2, g2, b2 = Cimpl.get_color(copy, x, y+1)
                r3, g3, b3 = Cimpl.get_color(copy, x+1, y)
                r_contrast = abs((r + g + b)/3 - (r3 + g3 + b3)/3)
                b_contrast = abs((r + g + b)/3 - (r2 + g2 + b2)/3)
                if r_contrast > thres or b_contrast > thres:
                    col = black
                else:
                    col = white
                Cimpl.set_color(copy, x, y, col)
        else:
            Cimpl.set_color(copy, x, y, white)
    return copy


def extreme_contrast(original_image: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Ibrahim Kasim

    RETURNS a Cimpl.Image object where
    the pixel channels in original_image have
    been set to 0 or 255.

    original_image is a Cimpl.Image object

    >>> extreme_contrast(Cimpl.load_image(choose_file()))
    """
    new_image = Cimpl.copy(original_image)
    min_pixel = 0
    max_pixel = 255
    for x, y, colour_tuple in original_image:
        list_colour = []

        for component in colour_tuple:
            if component <= 127:
                list_colour += [min_pixel]
            else:
                list_colour += [max_pixel]

        maximized_contrast = Cimpl.create_color(list_colour[0], list_colour[1], list_colour[2])
        Cimpl.set_color(new_image, x, y, maximized_contrast)
    return new_image


def flip_horizontal(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS a Cimpl.Image object
    where img is flipped horizontally

    img is a Cimpl.Image object

    >>> flip_horizontal(Cimpl.load_image(Cimpl.choose_file()))
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


def posterize(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS a Cimpl.Image where
    img has its RGB channels
    set to the midpoint of quadrants:
        0..63, 64..127, 128..191, and 192..255
    depending on where the color channel value is situated between

    img is a Cimpl.Image object passed to the function

    >>> posterize(Cimpl.load_image(Cimpl.choose_file()))
    """
    img = Cimpl.copy(img)
    for x, y, col in img:
        channels = []
        for ch in col:
            channels += [_adjust_component(ch)]
        Cimpl.set_color(img, x, y, Cimpl.create_color(channels[0], channels[1], channels[1]))
    return img


def _adjust_component(num: int) -> int:
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


def grayscale(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a grayscaled
    Cimpl.Image object after
    being PASSED img

    img is a Cimpl.Image object

    >>> grayscale(Cimpl.load_image(Cimpl.choose_file()))
    """
    img = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        avg = (r + g + b) / 3
        Cimpl.set_color(img, x, y, Cimpl.create_color(avg, avg, avg))
    return img


def sepia(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Yanglong Liu

    RETURNS a sepia filtered
    Cimpl.Image object after
    being PASSED img

    img is a Cimpl.Image object

    >>> sepia(Cimpl.load_image(Cimpl.choose_file()))
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
    return img


def three_tone(img: Cimpl.Image, tone_a: str, tone_b: str, tone_c: str) -> Cimpl.Image:
    """
    Author: Himanshu Singh

    RETURNS a Cimpl.Image object
    that was turned into a two toned image after
    being PASSED img, tone_a, tone_b, and tone_c

    img is a Cimpl.Image object

    tone_a, tone_b, and tone_c are strings representing colours

    >>> three_tone(Cimpl.load_image(Cimpl.choose_file()), 'black', 'white', 'gray')
    """
    colours = {
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
        if brightness <= 84:
            Cimpl.set_color(img, x, y, colours[tone_a])
        elif 84 < brightness <= 170:
            Cimpl.set_color(img, x, y, colours[tone_b])
        else:
            Cimpl.set_color(img, x, y, colours[tone_c])
    return img


def two_tone(img: Cimpl.Image, tone_a: str, tone_b: str) -> Cimpl.Image:
    """
    Author: Himanshu Singh

    RETURNS a Cimpl.Image object
    that was turned into a two toned image
    after being PASSED img, tone_a, and tone_b

    img is a Cimpl.Image object

    tone_a and tone_b are strings representing colours

    >>> two_tone(Cimpl.load_image(Cimpl.choose_file()), 'white', 'gray')
    """
    colours = {
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
            Cimpl.set_color(img, x, y, colours[tone_a])
        else:
            Cimpl.set_color(img, x, y, colours[tone_b])
    return img


def flip_vertical(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Himanshu Singh

    RETURNS a Cimpl.Image
    that was flipped, after
    being PASSED a img

    img is a Cimpl.Image object

    >>> flip_vertical(Cimpl.load_image(Cimpl.choose_file()))
    """
    hgt = Cimpl.get_height(img)
    mid_y = hgt // 2
    wth = Cimpl.get_width(img)
    copy = Cimpl.copy(img)
    for y in range(mid_y):
        for x in range(wth):
            Cimpl.set_color(copy, x, y, Cimpl.get_color(img, x, hgt-y-1))
            Cimpl.set_color(copy, x, hgt-y-1, Cimpl.get_color(img, x, y))
    return copy

