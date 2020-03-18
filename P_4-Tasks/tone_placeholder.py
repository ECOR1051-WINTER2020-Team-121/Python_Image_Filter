# This file is a placeholder for the two_tone function

import Cimpl


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


"""
#Group: Himanshu Singh, Zakaria Ismail, Ibrahim Kasim, Yang Long Liu
group number: 121
author: himanshu singh
"""
import Cimpl


def _brightness(r: int, g: int, b: int) -> int:
    """
    this returns the brightness of a pixel at a certain (x,y) coordinate.
    """
    _brightness = (r + g + b) / 3
    print("in brightness")
    return _brightness


def two_tone(img: Cimpl.Image, col1: str, col2: str) -> Cimpl.Image:
    """
    Returns a two-toned Cimpl.Image object, based on the colors col1 and col2
    passed.

    img is the original Cimpl.Image object passed

    col1 and col2 are the strings representing the image.
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
            black = Cimpl.create_color(0, 0, 0)
            Cimpl.set_color(newimage, x, y, COLORS[col1])


        else:
            Cimpl.set_color(newimage, x, y, COLORS[col2])

    #Cimpl.save_as(newimage, "2toneoutcome.jpg")
    #Cimpl.show(newimage)
    #Cimpl.show(img)
    return newimage


def three_tone(img: Cimpl.Image, col1: str, col2: str, col3: str) -> Cimpl.Image:
    """
    Returns a three-toned Cimpl.Image object, based on the colors col1, col2
    and col3 passed.

    img is the original Cimpl.Image object passed

    col1, col2 and col3 are the strings representing the image.
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

        if bright <= 84:
            Cimpl.set_color(newimage, x, y, COLORS[col1])

        elif 84 < bright <= 170:
            Cimpl.set_color(newimage, x, y, COLORS[col2])

        else:
            Cimpl.set_color(newimage, x, y, COLORS[col3])

    #Cimpl.save_as(newimage, "3toneoutcome.jpg")
    #Cimpl.show(newimage)
    #Cimpl.show(img)
    return newimage

