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


def check_equal(expected: Cimpl.Image, outcome: Cimpl.Image) -> None:
    """
    Author: Zakaria Ismail

    Checks if PARAMETERS expected and outcome,
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


print("---TESTING FUNCTION red_channel()---")
expected = Cimpl.load_image(input("Select expected (A RED RESULT) image filename: "))
print("DISPLAYING EXPECTED IMAGE: ")
Cimpl.show(expected)

testfile = Cimpl.load_image(input("Input filename of image to be passed (AN UNCOLORED IMAGE) through FUNCTION red_channel: "))
print("DISPLAYING TEST IMAGE: ")
Cimpl.show(testfile)

print("PASSING TEST IMAGE INTO function red_channel: ")
outcome = red_channel(testfile)
print("DISPLAYING OUTCOME: ")
Cimpl.show(outcome)


print("---VISUAL TEST COMPLETE---")

# These are the test functions
print("---TESTING red_channel FUNCTION QUANTITATIVELY---")
white = Cimpl.create_image(50, 50)
print("DISPLAYING WHITE IMAGE: ")
Cimpl.show(white)

red = Cimpl.create_image(50, 50, Cimpl.create_color(255, 0, 0))
print("DISPLAYING EXPECTED RED IMAGE: ")
Cimpl.show(red)

print("PASSING WHITE IMAGE INTO red_channel")
filtered_white = red_channel(white)
print("DISPLAYING FILTERED WHITE IMAGE")
Cimpl.show(filtered_white)
print("COMPARING FILTERED WHITE IMAGE (outcome) AND RED IMAGE (expected)")
check_equal(red, filtered_white)
