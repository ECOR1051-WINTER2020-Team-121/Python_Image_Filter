"""
1. Team Identifier: #121
2. Contributing Members: Zakaria Ismail - 101143497


There are lots of errors that are shown from my check_equal() function
while testing the given approved images (the dog pictures) due to the
.jpg/.png formatting issue.

"""

import Cimpl


def combine(r_img: str, g_img: str, b_img: str) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject where
    three image filenames are passed.
    Combines the color channels
    of the three arguments.

    >>> Cimpl.show(combine('red_image.png', 'green_image.png', 'blue_image.png'))
    -> An a combination of the filtered images will be displayed. Hence, the original image.
    """
    r_img = Cimpl.load_image(r_img)
    g_img = Cimpl.load_image(g_img)
    b_img = Cimpl.load_image(b_img)
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

    >>> check_equal(Cimpl.load_image('p2-original.jpg'), Cimpl.load_image('combined_image.png'))
    -> Test results and error messages are printed.
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


expected = Cimpl.load_image(input('Input EXPECTED image filename: '))
print("DISPLAYING EXPECTED IMAGE")
Cimpl.show(expected)

red = input("Input red image filename: ")  # choose_file does not work for me.
print("DISPLAYING RED IMAGE")
Cimpl.show(Cimpl.load_image(red))
green = input("Input green image filename: ")
print("DISPLAYING GREEN IMAGE")
Cimpl.show(Cimpl.load_image(green))
blue = input("Select blue image filename: ")
print("DISPLAYING BLUE IMAGE")
Cimpl.show(Cimpl.load_image(blue))

print("COMBINING IMAGES")
outcome = combine(red, green, blue)

print("DISPLAYING combine() function OUTCOME IMAGE:")
Cimpl.show(outcome)
print("COMPARING OUTCOME AND EXPECTED: ")
check_equal(expected, outcome)

