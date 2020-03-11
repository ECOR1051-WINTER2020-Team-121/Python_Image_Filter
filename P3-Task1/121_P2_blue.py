import Cimpl


def blue_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject whose
    channels except for blue, have
    been zeroed, after being
    PASSED an Cimpl.Image object

    >>> Cimpl.show(blue_channel('p2-original.png'))
    -> An a blue filtered image will be displayed
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(0, 0, b))
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
                errors += 1
        if errors == 0:
            print("SUCCESS: expected and outcome are of the same type and have identical pixels.")
        else:
            print("{} ERRORS detected.".format(errors))
    else:
        print("ERROR: Different types detected.\n"
              "Expected: Type {}\n"
              "Outcome: Type {}".format(type(expected), type(outcome)))


print("---TESTING FUNCTION blue_channel()---")
expected = Cimpl.load_image(input("Select expected image filename: "))
print("DISPLAYING EXPECTED IMAGE: ")
Cimpl.show(expected)

testfile = Cimpl.load_image(input("Input filename of image to be passed through FUNCTION blue_channel: "))
print("DISPLAYING TEST IMAGE: ")
Cimpl.show(testfile)

print("PASSING TEST IMAGE INTO function blue_channel: ")
outcome = blue_channel(testfile)
print("DISPLAYING OUTCOME: ")
Cimpl.show(outcome)
print("COMPARING EXPECTED AND OUTCOME")
#check_equal(expected, outcome)

# These are the test functions
print("---TESTING blue_channel FUNCTION QUANTITATIVELY---")
white = Cimpl.create_image(50, 50)
print("DISPLAYING WHITE IMAGE: ")
Cimpl.show(white)

blue = Cimpl.create_image(50, 50, Cimpl.create_color(0, 0, 255))
print("DISPLAYING EXPECTED BLUE IMAGE: ")
Cimpl.show(blue)

print("PASSING WHITE IMAGE INTO red_channel")
filtered_white = blue_channel(white)
print("DISPLAYING FILTERED WHITE IMAGE")
Cimpl.show(filtered_white)
print("COMPARING FILTERED WHITE IMAGE (outcome) AND BLUE IMAGE (expected)")
check_equal(blue, filtered_white)








