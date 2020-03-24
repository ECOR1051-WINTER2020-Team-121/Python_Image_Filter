
import Cimpl


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


def test_flip_vertical() -> None:
    """
    Tests function flip_vertical

    >>> test_flip_vertical()
    """

    # This test will involve a transformation from an original image to a vertically flipped image

    # Whether pixels will be flipped is independent of the pixels' colour
    # However, there are three zones that must be tested.
    #   1. Border pixels    (2 pixels)
    #   2. Non-border pixels    (2 pixels)
    #   3. Center pixels when height is ODD (1 pixel)
    #   4. Center pixels when height is EVEN (2 pixels)

    # However, case #3 and #4 cannot allow testing for an odd and an even width image, so there will be TWO images tested
    #   Image 1: Tests border, non-border, and ODD heighted center pixel    (5 pixels)  1x5
    #   Image 2: Tests border, non-border, and EVEN heighted center pixel   (6 pixels)  1x6

    # IMAGE 1:
    #   Border: (255, 255, 255), (0, 0, 0) -> (0, 0, 0), (255, 255, 255)
    #   Non-border: (

    # 0. Border pixel test: