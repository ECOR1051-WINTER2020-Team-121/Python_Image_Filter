import Cimpl

SAVE_FILE_AS = 'blue_channelled.png'


def blue_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS an ImageObject whose
    channels except for blue, have
    been zeroed, after being
    PASSED an ImageObject
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(0, 0, b))
    Cimpl.save_as(copy, SAVE_FILE_AS)
    return copy


def check_equal(expected: Cimpl.Image, outcome: Cimpl.Image) -> None:
    """
    Checks if PARAMETERS expected and outcome,
    both Cimpl.Image objects are:
        1. Of the same type
        2. Have the same pixel at each location - Quantitatively the same
    PRINTS the location
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


white_original = Cimpl.create_image(50, 50, Cimpl.create_color(255, 255, 255))  # original image: white image
blue_expected = Cimpl.create_image(50, 50, Cimpl.create_color(0, 0, 255))   # ideal result: all blue image - each pix at 255r

blue_outcome = blue_channel(white_original)
Cimpl.show(blue_outcome)

check_equal(blue_outcome, blue_expected)







