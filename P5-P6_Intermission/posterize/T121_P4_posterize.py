"""
Team Identifier: #121
Contributing Members: Zakaria Ismail - 101143497

"""

import Cimpl


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


#filename = input("Input image filename: ")  # used for mac
print("SELECT AN IMAGE FILE: ")
filename = Cimpl.choose_file()

original = Cimpl.load_image(filename)
print("--DISPLAYING ORIGINAL IMAGE--")
Cimpl.show(original)

print("--PROCESSING POSTERIZED IMAGE--")
posterized = posterize(original)
print("--DISPLAYING POSTERIZED IMAGE--")
Cimpl.show(posterized)