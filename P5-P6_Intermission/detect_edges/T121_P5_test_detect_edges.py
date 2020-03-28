import Cimpl
from T121_P5_detect_edges import detect_edges


def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a
    "fail" message.

    Parameter description should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.

    Parameters outcome and expected are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal.
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:

        # The format method is explained on pages 119-122 of
        # 'Practical Programming', 3rd ed.

        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '),
                     outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")


def test_detect_edges() -> None:
    """
    Tests function detect_edges

    >>> test_detect_edges()
    """
    # This test will involve a transformation from original to black and white.
    # The threshold value will be 10.

    # This function is contrast and position dependent
    # It depends on the difference of the brightness of pixels and threshold

    # List of cases:
    #   - Pixel w/ Lighter pixel below becomes black b/c contrast > thres
    #   - Pixel w/ Lighter pixel below becomes white b/c contrast = thres
    #   - Pixel w/ Lighter pixel below becomes white b/c contrast < thres
    #   - Pixel w/ Darker pixel below becomes black b/c contrast > thres
    #   - Pixel w/ Darker pixel below becomes white b/c contrast = thres
    #   - Pixel w/ Darker pixel below becomes white b/c contrast < thres
    #   - Pixel at bottom row becomes white

    # The testing of pixels when lighter and darker is done to test whether it works for both cases (difference calc)

    # This will be tested by setting up a 2x4 image.
    # The first column will get darker in brightness as you go down (-11, -10, -9) and will test the "Darker" cases
    # The second column will get lighter in brightness as you go down (+11, +10, +9) and will test the "lighter" cases
    # The "bottom row" cases will be tested twice on each column

    # FIRST COLUMN:
    # 0,0. (255, 255, 255) -> (0, 0, 0)
    # 1,0. (244, 244, 244) -> (255, 255, 255)
    # 2,0. (234, 234, 234) -> (255, 255, 255)
    # 3,0. (225, 225, 225) -> (255, 255, 255)

    # SECOND COLUMN:
    # 0,1. (0, 0, 0) -> (0, 0, 0)
    # 1,1. (11, 11, 11) -> (255, 255, 255)
    # 2,1. (21, 21, 21) -> (255, 255, 255)
    # 3,1. (30, 30, 30) -> (255, 255, 255)

    original = Cimpl.create_image(2, 4)
    # FIRST COLUMN
    Cimpl.set_color(original, 0, 0, Cimpl.Color(255, 255, 255))
    Cimpl.set_color(original, 0, 1, Cimpl.Color(244, 244, 244))
    Cimpl.set_color(original, 0, 2, Cimpl.Color(234, 234, 234))
    Cimpl.set_color(original, 0, 3, Cimpl.Color(225, 225, 225))
    # SECOND COLUMN
    Cimpl.set_color(original, 1, 0, Cimpl.Color(0, 0, 0))
    Cimpl.set_color(original, 1, 1, Cimpl.Color(11, 11, 11))
    Cimpl.set_color(original, 1, 2, Cimpl.Color(21, 21, 21))
    Cimpl.set_color(original, 1, 3, Cimpl.Color(30, 30, 30))

    expected = Cimpl.create_image(2, 4)
    # FIRST COLUMN
    Cimpl.set_color(expected, 0, 0, Cimpl.Color(0, 0, 0))
    Cimpl.set_color(expected, 0, 1, Cimpl.Color(255, 255, 255))
    Cimpl.set_color(expected, 0, 2, Cimpl.Color(255, 255, 255))
    Cimpl.set_color(expected, 0, 3, Cimpl.Color(255, 255, 255))
    # SECOND COLUMN
    Cimpl.set_color(expected, 1, 0, Cimpl.Color(0, 0, 0))
    Cimpl.set_color(expected, 1, 1, Cimpl.Color(255, 255, 255))
    Cimpl.set_color(expected, 1, 2, Cimpl.Color(255, 255, 255))
    Cimpl.set_color(expected, 1, 3, Cimpl.Color(255, 255, 255))

    outcome = detect_edges(original, 10)

    for x, y, col in outcome:
        check_equal("Testing pixel @(Row:{},Col:{})".format(y, x), col, Cimpl.get_color(expected, x, y))


test_detect_edges()

