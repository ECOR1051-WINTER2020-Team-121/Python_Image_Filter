# experiments with image parsing methods using the Cimpl library

import Cimpl


def red_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS an Cimpl.Image Object whose
    channels, except for red, have
    been zeroed, after being
    PASSED an ImageObject
    """
    copy = Cimpl.copy(img)

    for x, y, (r, g, b) in img:
        # print(x, y, r, g ,b)
        Cimpl.set_color(copy, x, y, Cimpl.create_color(r, 0, 0))
    return copy


def check_equal(expected: Cimpl.Image, outcome: Cimpl.Image) -> None:
    """
    Checks if PARAMETERS expected and outcome,
    both Cimpl.Image objects are:
        1. Of the same type
        2. Have the same pixel at each location - Quantitatively the same
    Assumes both PARAMETERS have the same dimensions <- should this be taken into account?
    """
    if type(expected) != type(outcome):
        for x, y, exp_col in expected:
            out_col = Cimpl.get_color(outcome, x, y)
            if exp_col != out_col:
                print("ERROR: Color discrepancy detected at x:{} y:{}\n"
                      "Expected: {}\n"
                      "Outcome: {}".format(x, y, exp_col, out_col))
        print("SUCCESS: expected and outcome are of the same type and have identical pixels.")
    else:
        print("ERROR: Different types detected.\n"
              "Expected: Type {}\n"
              "Outcome: Type {}".format(type(expected), type(outcome)))


imge = Cimpl.load_image('miss_sullivan.png')
red_img = red_channel(imge)
Cimpl.show(red_img)
