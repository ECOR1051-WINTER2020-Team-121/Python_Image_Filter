import Cimpl


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
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(0, 0, b))
    return copy


def blue_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject whose
    channels except for green, have
    been zeroed, after being
    PASSED a Cimpl.Image object

    >>> Cimpl.show(blue_channel(Cimpl.load_image(('p2-original.png')))
    -> An a green filtered image will be displayed
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(0, 0, b))
    return copy


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


def detect_edges(img: Cimpl.Image, thres: int) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object
    whose pixels have been changed
    to black or white dependent on its
    contrast with the pixel below it after
    being passed img and thres

    img is a Cimpl.Image object
    thres is a integer

    >>> detect_edges(Cimpl.load_image(choose_file()), 4)
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
    RETURNS a Cimpl.Image object
    whose pixels have been changed
    to black or white dependent on its
    contrast with the pixel below or to the
    right of it, after
    being passed img and thres

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


def flip_horizontal(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image
    that was flipped, after
    being PASSED a Cimpl.Image object
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
    return img


def three_tone(img: Cimpl.Image, tone_a: str, tone_b: str, tone_c: str) -> Cimpl.Image:
    """
        RETURNS a Cimpl.Image object
        that was turned into a two toned image.
        Is PASSED a Cimpl.Image object,
        and two strings
        """
    COLOURS = {
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
            Cimpl.set_color(img, x, y, COLOURS[tone_a])
        elif 84 < brightness <= 170:
            Cimpl.set_color(img, x, y, COLOURS[tone_b])
        else:
            Cimpl.set_color(img, x, y, COLOURS[tone_c])
    return img


def two_tone(img: Cimpl.Image, tone_a: str, tone_b: str) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object
    that was turned into a two toned image.
    Is PASSED a Cimpl.Image object,
    and two strings
    """
    COLOURS = {
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
            Cimpl.set_color(img, x, y, COLOURS[tone_a])
        else:
            Cimpl.set_color(img, x, y, COLOURS[tone_b])
    return img


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