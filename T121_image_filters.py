import Cimpl
"""
Team Identifier: 121
Contributing Members: Zakaria Ismail, Ibrahim Kasim, Himanshu Singh, Yanglong Liu
"""



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
            # r1, g1, b1 = Cimpl.get_color(img, x, y)
            # r2, g2, b2 = Cimpl.get_color(img, x, hgt-y)
            Cimpl.set_color(copy, x, y, Cimpl.get_color(img, wth - x - 1, y))
            Cimpl.set_color(copy, wth - x - 1, y, Cimpl.get_color(img, x, y))
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
    ranges = [63, 127, 191, 255]
    mid = [31, 95, 159, 223]
    for i in range(len(ranges)):
        if num <= ranges[i]:
            return mid[i]


def green_channel():
    """
    The Author: Ibrahim Kasim
    green_channel() -> Cimpl.Image:
    Returns green filtered image. It directs user to choose an image that 
    is desired for filtering.
    
    """

    image_file = Cimpl.choose_file()
    original_image = Cimpl.load_image(image_file)
    new_image = Cimpl.copy(original_image)
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        green_color = Cimpl.create_color(0, g, 0)
        Cimpl.set_color(new_image, x, y, green_color)

    return new_image


def extreme_contrast(original_image: Cimpl.Image) -> Cimpl.Image:
    """
    The author: Ibrahim Kasim
    returns image object with extreme contrast filter apllied.
    
        >>>test_image = Cimpl.load_image(Cimpl.choose_file())
           extreme_channel(test_image)
        ...(shows orginal image in extreme contrast filter)

    """
    new_image = Cimpl.copy(original_image)
    min_pixel = 0
    max_pixel = 255
    for x, y, colour_tuple in original_image:
        i = 0
        for component in colour_tuple:
            list_colour = list(colour_tuple)
            if component <= 127:
                list_colour[i] = min_pixel
                maximized_contrast = Cimpl.create_color(list_colour[0], list_colour[1], list_colour[2])
                Cimpl.set_color(new_image, x, y, maximized_contrast)
            elif component >= 128:
                list_colour[i] = max_pixel
                maximized_contrast = Cimpl.create_color(list_colour[0], list_colour[1], list_colour[2])
                Cimpl.set_color(new_image, x, y, maximized_contrast)
            i += 1
    return new_image


def detect_edges(original_image: Cimpl.Image, threshold: float) -> Cimpl.Image:
    """ The author: Ibrahim Kasim
    returns a copy of the original image with edge detection filter apllied to it."""
    new_image = Cimpl.copy(original_image)
    total_width = Cimpl.get_width(original_image)
    total_height = Cimpl.get_height(original_image)
    blacked = Cimpl.create_color(0, 0, 0)
    whited = Cimpl.create_color(255, 255, 255)

    for x, y, pixels in original_image:
        if x != total_width and y != total_height - 1:
            pixel_top = Cimpl.get_color(original_image, x, y)
            pixel_bottom = Cimpl.get_color(original_image, x, y + 1)

            average_top = (pixel_top[0] + pixel_top[1] + pixel_top[2]) / 3
            average_bottom = (pixel_bottom[0] + pixel_bottom[1] + pixel_bottom[2]) / 3
            difference = abs(average_bottom - average_top)
            if x == total_width:
                Cimpl.set_color(new_image, x, y, whited)

            elif difference > threshold:
                Cimpl.set_color(new_image, x, y, blacked)
            else:
                Cimpl.set_color(new_image, x, y, whited)
    return new_image

def sepia(image):
    """
    Author: YANGLONG LIU
    return a grayscaled Image object after being passed a Image object.
    """
    hgt = Cimpl.get_height(image)
    wth = Cimpl.get_width(image)
    for x in range(wth):
        for y in range(hgt):
            red, green, blue = Cimpl.get_color(image, x, y)
            if red < 63:
                blue = blue * 0.9
                red = red * 1.1
            elif 63 <= red and 193 >= red:
                blue = blue * 0.85
                red = red * 1.15
            elif red > 191:
                blue = blue * 0.93
                red = red * 1.08
            new_color = Cimpl.create_color(red, blue, green)
            Cimpl.set_color(image, x, y, new_color)
    return image


def detect_edges_better(image: Cimpl.Image, threshold: int) -> Cimpl.Image:
    """
    Author:YANGLONG LIU 101141366
    returns a Image with only black and white color depending on the comparsion 
    between contrast and threshold.
    >>>improved_detect_image = detect_edges_better(raw_image, 13)
    >>>show(improved_detect_image) which returned image looks like pencil skectches.
    """
    new_image = Cimpl.copy(image)
    wdt = Cimpl.get_width(new_image)
    hgt = Cimpl.get_height(new_image)
    for x in range(wdt):
        for y in range(hgt):
            if y < hgt - 1:  # make a confirmation for the bottom line is not in this range
                red, green, blue = Cimpl.get_color(image, x, y)
                red1, green1, blue1 = Cimpl.get_color(image, x, y + 1)  # the pixel below the pixel of raw image one
                red2, green2, blue2 = Cimpl.get_color(image, x - 1, y)  # the right one of the pixel

                brightness1 = (red + blue + green) / 3
                brightness2 = (red1 + blue1 + green1) / 3
                brightness3 = (red2 + blue2 + green2) / 3

                contrast1 = abs(brightness2 - brightness1)
                contrast2 = abs(brightness3 - brightness1)

                if contrast1 > threshold or contrast2 > threshold:  # make a comparsion the contrast with threshold
                    red, green, blue = 0, 0, 0  # if the contrast is higher, change color to black.
                    black = Cimpl.create_color(red, green, blue)
                    Cimpl.set_color(new_image, x, y, black)

                else:
                    red, green, blue = 255, 255, 255  # if the contrast is lower, change color to white.
                    white = Cimpl.create_color(red, green, blue)
                    Cimpl.set_color(new_image, x, y, white)

            elif y == hgt - 1:  # the bottom row of the image which the bottom line is in this range
                red, green, blue = 255, 255, 255  # change to white simply.
                white = Cimpl.create_color(red, green, blue)
                Cimpl.set_color(new_image, x, y, white)

    return new_image


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


def _brightness(r: int, g: int, b: int) -> int:
    """
    author: Himanshu Singh
    this returns the brightness of a pixel at a certain (x,y) coordinate. 
    
    This is a helper function
    
    >>>_brightness(255,255,255)
    255
    """
    _brightness = (r + g + b) / 3

    return _brightness


def three_tone(img: Cimpl.Image, col1: str, col2: str, col3: str) -> Cimpl.Image:
    """
    Returns a three-toned Cimpl.Image object, based on the colors col1, col2
    and col3 passed. 
    
    img is the original Cimpl.Image object passed
    
    col1, col2 and col3 are the strings representing the image.
    
    >>>three_tone(Cimpl.load_image("image.jpg"), "col1", "col2", "col3")
    returns image with a three toned filter

    """
    COLORS = {

        "black": Cimpl.Color(0, 0, 0),  # black
        "white": Cimpl.Color(255, 255, 255),  # white
        "gray": Cimpl.Color(128, 128, 128),  # gray
        "red": Cimpl.Color(255, 0, 0),  # red
        "lime": Cimpl.Color(0, 255, 0),  # lime
        "blue": Cimpl.Color(0, 0, 255),  # blue
        "yellow": Cimpl.Color(255, 255, 0),  # yellow
        "cyan": Cimpl.Color(0, 255, 255),  # cyan
        "magenta": Cimpl.Color(255, 0, 255)  # magenta

    }

    newimage = Cimpl.copy(img)

    for x, y, (r, g, b) in img:
        bright = _brightness(r, g, b)

        if bright <= 84:
            # if brightness is below or equal to 84 change the color at said pixel to
            # col1
            Cimpl.set_color(newimage, x, y, COLORS[col1])

        elif 84 < bright <= 170:
            # if brightness is below or equal to 170 but higher than 84 change the   
            # color at said pixel to col2
            Cimpl.set_color(newimage, x, y, COLORS[col2])

        else:
            # else set color to col3
            Cimpl.set_color(newimage, x, y, COLORS[col3])

    return newimage


def two_tone(img: Cimpl.Image, col1: str, col2: str) -> Cimpl.Image:
    """
    Author: Himanshu Singh
    Returns a two-toned Cimpl.Image object, based on the colors col1 and col2
    passed. 
    
    img is the original Cimpl.Image object passed
    
    col1 and col2 are the strings representing the image.
    
    >>>two_tone(Cimpl.load_image("image.jpg"), "col1", "col2")
    returns image with a two toned filter

    """

    COLORS = {

        "black": Cimpl.Color(0, 0, 0),  # black
        "white": Cimpl.Color(255, 255, 255),  # white
        "gray": Cimpl.Color(128, 128, 128),  # gray
        "red": Cimpl.Color(255, 0, 0),  # red
        "lime": Cimpl.Color(0, 255, 0),  # lime
        "blue": Cimpl.Color(0, 0, 255),  # blue
        "yellow": Cimpl.Color(255, 255, 0),  # yellow
        "cyan": Cimpl.Color(0, 255, 255),  # cyan
        "magenta": Cimpl.Color(255, 0, 255)  # magenta

    }

    # image = load_image(FILENAME)
    newimage = Cimpl.copy(img)

    for x, y, (r, g, b) in img:
        bright = _brightness(r, g, b)

        if bright <= 127:
            # if calculated brightness at said pixel is below 127 set color to col[1]        
            black = Cimpl.create_color(0, 0, 0)
            Cimpl.set_color(newimage, x, y, COLORS[col1])

        else:
            # else set color to col2 at said pixel
            Cimpl.set_color(newimage, x, y, COLORS[col2])

    return newimage


def flip_vertical(img: Cimpl.Image) -> Cimpl.Image:
    """
    author: himanshu singh
    flips the image vertically (Cimpl.Image object) and returns it when called.
    
    >>> flip_vertical(Cimpl.load_image("image.jpg"))
    returns a vertically flipped image

    """
    newimage = Cimpl.copy(img)

    height1 = Cimpl.get_height(img)  # get image height

    width1 = Cimpl.get_width(img)  # get image width

    for y in range(height1):

        for x in range(width1):
            change = height1 - y - 1
            # editing height to flip vertically (change)
            # change implemented below to make changes to the actual image passed 
            # in below 
            Cimpl.set_color(newimage, x, y, Cimpl.get_color(img, x, change))
            Cimpl.set_color(newimage, x, change, Cimpl.get_color(img, x, y))

    return newimage
