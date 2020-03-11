import Cimpl

#SAVE_FILE_AS = 'red_channelled.png'


def red_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject whose
    channels except for red, have
    been zeroed, after being
    PASSED an image filename
    """
    img = Cimpl.load_image(img)
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(r, 0, 0))
    #Cimpl.save_as(copy, SAVE_FILE_AS)
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

print("---TESTING FUNCTION red_channel()---")
expected = Cimpl.load_image(input("Select expected image filename: "))
print("DISPLAYING EXPECTED IMAGE: ")
Cimpl.show(expected)

testfile = input("Input filename of image to be passed through FUNCTION red_channel: ")
print("DISPLAYING TEST IMAGE: ")
Cimpl.show(Cimpl.load_image(testfile))

print("PASSING TEST IMAGE INTO function red_channel: ")
outcome = red_channel(testfile)
print("DISPLAYING OUTCOME: ")
Cimpl.show(outcome)
print("COMPARING EXPECTED AND OUTCOME")
check_equal(expected, outcome)