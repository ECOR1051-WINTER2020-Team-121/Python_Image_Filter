import Cimpl

from T121_P4_two_tone import two_tone


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


# Naming is to be determined (Correct format uncertain)
def test_two_tone() -> None:
    """
    Author: Zakaria Ismail

    Tests FUNCTION two_tone.

    >>> test_two_tone()
    """
    # This test will involve a transformation from original -> Black and White two toned

    # Brightness definitions:
    #   Low brightness: Less than 128
    #   High brightness: Greater than or equal to 128

    # This test function tests if two_tone correctly transforms:
    # (0, 0, 0) -> (0, 0, 0)    # Low zero brightness pixel
    # (0, 0, 1) -> (0, 0, 0)    # Low non-zero brightness pixel
    # (127, 127, 127) -> (0, 0, 0)  # Low mid brightness pixel
    # (128, 128, 128) -> (255, 255, 255)    # High mid brightness pixel
    # (254, 255, 255) -> (255, 255, 255)    # High non-255 brightness pixel
    # (255, 255, 255) -> (255, 255, 255)    # High 255 brightness pixel
    # Do I include non-gray pixels? I will not, because brightness is the dependent factor here.

    # 6 test cases. Therefore image with six pixels is created
    original = Cimpl.create_image(6, 1)

    Cimpl.set_color(original, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(original, 1, 0, Cimpl.create_color(0, 0, 1))
    Cimpl.set_color(original, 2, 0, Cimpl.create_color(127, 127, 127))
    Cimpl.set_color(original, 3, 0, Cimpl.create_color(128, 128, 128))
    Cimpl.set_color(original, 4, 0, Cimpl.create_color(254, 255, 255))
    Cimpl.set_color(original, 5, 0, Cimpl.create_color(255, 255, 255))

    # An ideal image with the corresponding expected results is created
    expected = Cimpl.create_image(6, 1)

    Cimpl.set_color(expected, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 1, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 2, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 3, 0, Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 4, 0, Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 5, 0, Cimpl.create_color(255, 255, 255))

    # Transforms the original image.
    two_toned_image = two_tone(original, 'black', 'white')

    for x, y, col in two_toned_image:
        check_equal('Checking pixel @({},{})'.format(x, y), col, Cimpl.get_color(expected, x, y))


test_two_tone()


