"""
1. Team Identifier: #121
2. Contributing Members: Zakaria Ismail - 101143497

"""

import Cimpl


def combine(img_1: Cimpl.Image, img_2: Cimpl.Image, img_3: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS a Cimpl.Image object
    where color channel values of
    img_1, img_2, and img_3 have been combined.

    img_1, img_2, and img_3 are Cimpl.Image objects PASSED to the function.

    >>> combine(Cimpl.create_image(1,1), Cimpl.create_image(1,1), Cimpl.create_image(1,1))
    """
    base = Cimpl.copy(img_1)

    for x, y, (r, g, b) in base:
        r3, g3, b3 = Cimpl.get_color(img_3, x, y)
        r2, g2, b2 = Cimpl.get_color(img_2, x, y)
        color = Cimpl.Color(r+r2+r3, g+g2+g3, b+b2+b3)
        Cimpl.set_color(base, x, y, color)

    return base



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

red = Cimpl.load_image(input("Input red image filename: "))  # choose_file does not work for me.
print("DISPLAYING RED IMAGE")
Cimpl.show(red)
green = Cimpl.load_image(input("Input green image filename: "))
print("DISPLAYING GREEN IMAGE")
Cimpl.show(green)
blue = Cimpl.load_image(input("Select blue image filename: "))
print("DISPLAYING BLUE IMAGE")
Cimpl.show(blue)

print("COMBINING IMAGES")
outcome = combine(red, green, blue)

print("DISPLAYING combine() function OUTCOME IMAGE:")
Cimpl.show(outcome)
#print("COMPARING OUTCOME AND EXPECTED: ")
#check_equal(expected, outcome)

# These are the tests
print("\n---TESTING function combine() QUANTITATIVELY---")
expected = Cimpl.create_image(50, 50)

red = Cimpl.create_image(50, 50, Cimpl.create_color(255, 0, 0))
green = Cimpl.create_image(50, 50, Cimpl.create_color(0, 255, 0))
blue = Cimpl.create_image(50, 50, Cimpl.create_color(0, 0, 255))

outcome = combine(red, green, blue)
print("DISPLAYING combine FUNCTION OUTCOME")
Cimpl.show(outcome)
print("COMPARING EXPECTED AND OUTCOME")
check_equal(expected, outcome)


