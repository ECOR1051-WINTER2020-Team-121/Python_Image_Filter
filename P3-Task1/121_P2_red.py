import Cimpl

SAVE_FILE_AS = 'red_channelled.png'


def red_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS an ImageObject whose
    channels except for red, have
    been zeroed, after being
    PASSED an ImageObject
    """
    copy = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        Cimpl.set_color(copy, x, y, Cimpl.create_color(r, 0, 0))
    Cimpl.save_as(copy, SAVE_FILE_AS)
    return copy


def check_equal(expected: Cimpl.Image, outcome: Cimpl.Image) -> None:
    """
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


# First test
white_original = Cimpl.create_image(50, 50, Cimpl.create_color(255, 255, 255))  # original image: white image
red_expected = Cimpl.create_image(50, 50, Cimpl.create_color(255, 0, 0))   # ideal result: all red image - each pix at 255r

red_outcome = red_channel(white_original)
Cimpl.show(red_outcome)

check_equal(red_expected, red_outcome)

# Second test
expected = Cimpl.load_image('red_image.png')
outcome = red_channel(Cimpl.load_image('p2-original.png'))
Cimpl.show(outcome)
check_equal(expected, outcome)
