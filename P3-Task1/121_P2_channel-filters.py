"""
Team Identifier: #121
Contributing Members: Zakaria Ismail, Ibrahim Kasim, Yanglong Liu, Himanshu Singh
"""

import Cimpl


def combine(r_img: Cimpl.Image, g_img: Cimpl.Image, b_img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject where
    three Cimpl.Image objects are passed.
    Combines the color channels
    of the three arguments.

    >>> Cimpl.show(combine(Cimpl.load_image('red_image.png'), Cimpl.load_image('green_image.png'), Cimpl.load_image('blue_image.png'))
    -> An a combination of the filtered images will be displayed.
    """
    base = Cimpl.copy(r_img)

    for x, y, (r, g, b) in base:
        g_r, g_g, g_b = Cimpl.get_color(g_img, x, y)
        b_r, b_g, b_b = Cimpl.get_color(b_img, x, y)
        color = Cimpl.create_color(compute_sum(r, g_r, b_r), compute_sum(g, g_g, b_g), compute_sum(b, g_b, b_b))
        Cimpl.set_color(base, x, y, color)
    Cimpl.save_as(base, 'combined_image.png')
    return base


def red_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Himanshu Singh

    RETURNS an Cimpl.Image object whose
    channels except for red, have
    been zeroed, after being
    PASSED an Cimpl.Image object

    >>> Cimpl.show(red_channel(Cimpl.load_image('p2-original.png')))
    -> An a red filtered image will be displayed
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(r, 0, 0))
    return copy


def green_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Ibrahim Kasim

    RETURNS an Cimpl.Image object whose
    channels except for green, have
    been zeroed, after being
    PASSED a Cimpl.Image object

    >>> Cimpl.show(green_channel(Cimpl.load_image(('p2-original.png')))
    -> An a green filtered image will be displayed
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(0, g, 0))
    return copy


def blue_channel(raw_image):
    """Author: Yanglong liu
    RETURNS a Cimpl.Image object
    whose red and green channels
    have been set to 0
    """
    blue_channel_image = Cimpl.copy(raw_image)
    for pi in raw_image:
        x,y,(r,g,b)=pi
        new_image_color = Cimpl.create_color(0,0,b)
        Cimpl.set_color(blue_channel_image,x,y,new_image_color)
    return blue_channel_image


def compute_sum(r: int, g: int, b: int) -> int:
    """
    Author: Zakaria Ismail

    RETURNS the sum of three numbers
    PASSED. If sum exceeds 255, then
    the sum is 255.

    >>> compute_sum(5,6,7)
    18
    """
    if r + g + b <= 255:
        return r + g + b
    else:
        return 255


original = Cimpl.load_image(input("Input image filename: "))
print("DISPLAYING IMAGE: ")
Cimpl.show(original)

print("COMPUTING RED FILTERED IMAGE")
red = red_channel(original)
print("DISPLAYING RED FILTERED IMAGE: ")
Cimpl.show(red)

print("COMPUTING GREEN FILTERED IMAGE")
green = green_channel(original)
print("DISPLAYING GREEN FILTERED IMAGE: ")
Cimpl.show(green)

print("COMPUTING BLUE FILTERED IMAGE")
blue = blue_channel(original)
print("DISPLAYING BLUE FILTERED IMAGE: ")
Cimpl.show(blue)

print("COMPUTING COMBINED RGB IMAGE")
combined = combine(red, green, blue)
print("DISPLAYING COMBINED RGB FILTERED IMAGE: ")
Cimpl.show(combined)

print("\n"
      "Program has finished. Have a good day.\n")

