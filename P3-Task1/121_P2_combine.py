# ISSUE RESOLVED. SOLUTION: Make sure to create a
# copy of an image in each function.

# Idea for testing: compare value addition with
# actual result value?

import Cimpl


def combine(r_img: Cimpl.Image, g_img: Cimpl.Image, b_img: Cimpl.Image) -> Cimpl.Image:
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
    base = Cimpl.copy(r_img)

    for x, y, (r, g, b) in base:
        g_r, g_g, g_b = Cimpl.get_color(g_img, x, y)
        b_r, b_g, b_b = Cimpl.get_color(b_img, x, y)
        color = Cimpl.create_color(compute_sum(r, g_r, b_r), compute_sum(g, g_g, b_g), compute_sum(b, g_b, b_b))
        Cimpl.set_color(base, x, y, color)
    Cimpl.save_as(base, 'combined.png')
    return base


def compute_sum(r: int, g: int, b: int) -> int:
    """
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
    PASSED an ImageObject
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(r, 0, 0))
    Cimpl.save_as(copy, 'red_channelled.png')
    return copy


def blue_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject whose
    channels except for blue, have
    been zeroed, after being
    PASSED an ImageObject
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(0, 0, b))
    Cimpl.save_as(copy, 'blue_channelled.png')
    return copy


def green_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject whose
    channels except for green, have
    been zeroed, after being
    PASSED an ImageObject
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(0, g, 0))
    Cimpl.save_as(copy, 'green_channelled.png')
    return copy


def check_equal(expected: Cimpl.Image, outcome: Cimpl.Image) -> None:
    """
    Author: Zakaria Ismail

    Checks if PARAMETERS expected and outcome,
    both Cimpl.Image objects are:
        1. Of the same type
        2. Have the same pixel at each location - Quantitatively the same
    Assumes both PARAMETERS have the same dimensions <- should this be taken into account?
    """
    errors = 0
    if type(expected) == type(outcome):
        for x, y, exp_col in expected:
            out_col = Cimpl.get_color(outcome, x, y)
            if exp_col != out_col:
                print("ERROR: Color discrepancy detected at x:{} y:{}\n"
                      "Expected: {}\n"
                      "Outcome: {}".format(x, y, exp_col, out_col))
        if errors == 0:
            print("SUCCESS: expected and outcome are of the same type and have identical pixels.")
        else:
            print("{} ERRORS detected.".format(errors))
    else:
        print("ERROR: Different types detected.\n"
              "Expected: Type {}\n"
              "Outcome: Type {}".format(type(expected), type(outcome)))


expected = Cimpl.create_image(50, 50)
red = red_channel(expected)
Cimpl.show(red)
blue = blue_channel(expected)
Cimpl.show(blue)
green = green_channel(expected)
Cimpl.show(green)

outcome = combine(red, green, blue)
check_equal(expected, outcome)

