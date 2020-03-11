"""
1. Team Identifier: Team #121
2. Contributing Members: Zakaria Ismail - 101143497

P.S
I have two tests in my function; one using monochromatic
images (white, red, green, blue) and another one using
the supplied images (red dog, blue dog, green dog, normal dog).

I did this because I had issues involving the .jpg and .png formatting
and when I spoke to Professor Green, he told me that I had to use the
first testing method, which involved testing monochromatic images so that
I can prove, quantitatively, that my combine() function works.

There are lots of errors that are shown from my check_equal() function
while testing the given approved images (the dog pictures) due to the
.jpg/.png formatting issue.

"""

import Cimpl


def combine(r_img: Cimpl.Image, g_img: Cimpl.Image, b_img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject where
    three ImageObjects are PASSED.
    Combines the color channels
    of the three arguments.

    >> combine(red_img, green_img, blue_img)
    combined_img
    """
    base = Cimpl.copy(r_img)

    for x, y, (r, g, b) in base:
        g_r, g_g, g_b = Cimpl.get_color(g_img, x, y)
        b_r, b_g, b_b = Cimpl.get_color(b_img, x, y)
        color = Cimpl.create_color(compute_sum(r, g_r, b_r), compute_sum(g, g_g, b_g), compute_sum(b, g_b, b_b))
        Cimpl.set_color(base, x, y, color)
    Cimpl.save_as(base, 'combined_image.png')
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


def check_equal(expected: Cimpl.Image, outcome: Cimpl.Image) -> None:
    """
    Author: Zakaria Ismail

    RETURNS nothing. Checks if PARAMETERS expected and outcome,
    both Cimpl.Image objects are:
        1. Of the same type
        2. Have the same pixel at each location - Quantitatively the same
    """
    errors = 0
    if type(expected) == type(outcome):
        for x, y, exp_col in expected:
            out_col = Cimpl.get_color(outcome, x, y)
            if exp_col != out_col:
                print("ERROR: Color discrepancy detected at x:{} y:{}\n"
                      "Expected: {}\n"
                      "Outcome: {}".format(x, y, exp_col, out_col))
                errors += 1
        if errors == 0:
            print("SUCCESS: expected and outcome are of the same type and have identical pixels.")
        else:
            print("{} ERRORS detected.".format(errors))
    else:
        print("ERROR: Different types detected.\n"
              "Expected: Type {}\n"
              "Outcome: Type {}".format(type(expected), type(outcome)))


# First test - Involves Monochromatic Images
print("---FIRST SET OF TESTS: MONOCHROMATIC IMAGES---")
expected = Cimpl.create_image(50, 50)
red = Cimpl.create_image(50, 50, Cimpl.Color(255, 0, 0))
#Cimpl.show(red)
blue = Cimpl.create_image(50, 50, Cimpl.Color(0, 255, 0))
#Cimpl.show(blue)
green = Cimpl.create_image(50, 50, Cimpl.Color(0, 0, 255))
#Cimpl.show(green)

outcome = combine(red, green, blue)
check_equal(expected, outcome)

# Second Test - Involves Dog Images
print("---SECOND TEST: DOG IMAGES TESTS---")
expected = Cimpl.load_image('p2-original.jpg')
red = Cimpl.load_image('red_image.png')         # Given dog color images are loaded
blue = Cimpl.load_image('blue_image.png')
green = Cimpl.load_image('green_image.png')

print("EXPECTED IS DISPLAYED: ")
Cimpl.show(expected)
outcome = combine(red, green, blue)
print("OUTCOME IS DISPLAYED:")
Cimpl.show(outcome)
print("COMPARING OUTCOME AND EXPECTED: ")
check_equal(expected, outcome)

