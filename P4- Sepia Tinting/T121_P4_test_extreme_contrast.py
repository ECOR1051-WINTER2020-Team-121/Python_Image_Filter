
import Cimpl

from T121_extreme_contrast import extreme_contrast


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


def test_extreme_contrast() -> None:
    """
    Tests function extreme_contrast
    """

    # This test function will involve a transformation from original -> Extreme contrasted (reduced colours)

    # Range definitions:
    #   Low: 0-127
    #   High: 128-255

    # This function will test if extreme_contrast() correctly transforms:
    # 0. (0, 0, 0) -> (0, 0, 0) # Low lower boundary channel value
    # 1. (1, 1, 1) -> (0, 0, 0) # Low non-boundary channel value
    # 2. (127, 127) -> (0, 0, 0)    # Low upper boundary channel value
    # 3. (128, 128, 128) -> (255, 255, 255) # High lower boundary channel value
    # 4. (129, 129, 129) -> (255, 255, 255) # High non-boundary channel value
    # 5. (255, 255, 255) -> (255, 255, 255) # High upper boundary channel value

    # 6 test cases. Therefore, 6 pixels.
    original = Cimpl.create_image(6, 1)

    Cimpl.set_color(original, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(original, 1, 0, Cimpl.create_color(1, 1, 1))
    Cimpl.set_color(original, 2, 0, Cimpl.create_color(127, 127, 127))
    Cimpl.set_color(original, 3, 0, Cimpl.create_color(128, 128, 128))
    Cimpl.set_color(original, 4, 0, Cimpl.create_color(129, 129, 129))
    Cimpl.set_color(original, 5, 0, Cimpl.create_color(255, 255, 255))

    # an ideal image with the corresponding expected image values is created
    expected = Cimpl.create_image(6, 1)

    Cimpl.set_color(expected, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 1, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 2, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 3, 0, Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 4, 0, Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 5, 0, Cimpl.create_color(255, 255, 255))

    extreme_contrasted = extreme_contrast(original)

    for x, y, col in extreme_contrasted:
        check_equal('Checking pixel @({},{})'.format(x, y), col, Cimpl.get_color(expected, x, y))


test_extreme_contrast()