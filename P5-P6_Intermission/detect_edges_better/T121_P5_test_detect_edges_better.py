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


def test_detect_edges_better() -> None:
    """
    Tests function detect_edges_beter

    >>> test_detect_edges_better()
    """
    # This test will involve a transformation from original to black and white.
    # The threshold value will be 10.

    # This function is contrast and position dependent
    # It depends on the difference of the brightness of pixels and threshold

    # There are 4 combinations of the rightmost and bottom pixel being lighter or darker
    #   - B: Darker, R: Darker
    #   - B: Darker, R: Lighter
    #   - B: Lighter, R: Darker
    #   - B: Lighter, R: Lighter

    # And there are three contrast states where:
    #   - contrast > thres
    #   - contrast = thres
    #   - contrast < thres
    #   - (contrast = 0?)

    # List of cases:
    #   - Pixel w/ Lighter pixel below becomes black b/c contrast > thres
    #   - Pixel w/ Lighter pixel below becomes white b/c contrast = thres
    #   - Pixel w/ Lighter pixel below becomes white b/c contrast < thres
    #   - Pixel w/ Darker pixel below becomes black b/c contrast > thres
    #   - Pixel w/ Darker pixel below becomes white b/c contrast = thres
    #   - Pixel w/ Darker pixel below becomes white b/c contrast < thres
    #   - Pixel at bottom row becomes white
    #   - Pixel at rightmost column becomes white

    # List of cases:
    #   - Pixel

    # The testing of pixels when lighter and darker is done to test whether it works for both cases (difference calc)


    for x, y, col in outcome:
        check_equal("Testing pixel @({},{})".format(x, y), col, Cimpl.get_color(expected, x, y))


test_detect_edges()

