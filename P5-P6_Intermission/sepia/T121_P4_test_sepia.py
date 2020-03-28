
import Cimpl
from T121_P4_sepia import sepia


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


def test_sepia() -> None:
    """
    Tests function sepia
    """

    # This test will involve a transformation from original -> sepiafied (grayscale + tint of yellow)

    # Range definitions and multipliers:
    #   Low: 0-62       (R: 1.1, G: 1, B: 0.9)
    #   Mid: 63-191     (R: 1.15, G: 1, B: 0.85)
    #   High: 192-255   (R: 1.08, G: 1, B: 0.93)

    # Question: Can RGB values have decimal places on them?
    # Observation: Cimpl.Color objects can only have integer values.
    # As such, inputting a float value will cause it to be floored to the nearest integer.

    # This function will test if sepia() correctly transforms:
    # 0. (0, 0, 0) -> (0, 0, 0) # Low lower boundary channel values
    # 1. (1, 1, 1) -> (1.1, 1, 0.9) # Low non-boundary channel values
    # 2. (62, 62, 62) -> (68.2, 62, 55.8)   # Low upper boundary channel values
    # 3. (63, 63, 63) -> (72.45, 63, 53.55) # Mid lower boundary channel values
    # 4. (64, 64, 64) -> (73.6, 64, 54.4)   # Mid non-boundary channel values
    # 5. (191, 191, 191) -> (219.65, 191, 162.35)   # Mid upper boundary channel values
    # 6. (192, 192, 192) -> (207.36, 192, 178.56)   # High lower boundary channel values
    # 7. (193, 193, 193) -> (208.44, 193, 179.49)   # High non-boundary channel values
    # 8. (255, 255, 255) -> (255 (not 275.4), 255, 237.15)   # High upper boundary channel values

    # 9 test cases. Therefore, 9 pixels
    original = Cimpl.create_image(9, 1)

    Cimpl.set_color(original, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(original, 1, 0, Cimpl.create_color(1, 1, 1))
    Cimpl.set_color(original, 2, 0, Cimpl.create_color(62, 62, 62))
    Cimpl.set_color(original, 3, 0, Cimpl.create_color(63, 63, 63))
    Cimpl.set_color(original, 4, 0, Cimpl.create_color(64, 64, 64))
    Cimpl.set_color(original, 5, 0, Cimpl.create_color(191, 191, 191))
    Cimpl.set_color(original, 6, 0, Cimpl.create_color(192, 192, 192))
    Cimpl.set_color(original, 7, 0, Cimpl.create_color(193, 193, 193))
    Cimpl.set_color(original, 8, 0, Cimpl.create_color(255, 255, 255))

    # an image with the corresponding expected image values is created
    expected = Cimpl.create_image(9, 1)

    Cimpl.set_color(expected, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 1, 0, Cimpl.create_color(1.1, 1, 0.9))
    Cimpl.set_color(expected, 2, 0, Cimpl.create_color(68.2, 62, 55.8))
    Cimpl.set_color(expected, 3, 0, Cimpl.create_color(72.45, 63, 53.55))
    Cimpl.set_color(expected, 4, 0, Cimpl.create_color(73.6, 64, 54.4))
    Cimpl.set_color(expected, 5, 0, Cimpl.create_color(219.65, 191, 162.35))
    Cimpl.set_color(expected, 6, 0, Cimpl.create_color(207.36, 192, 178.56))
    Cimpl.set_color(expected, 7, 0, Cimpl.create_color(208.44, 193, 179.49))
    Cimpl.set_color(expected, 8, 0, Cimpl.create_color(255, 255, 237.15))

    sepiafied = sepia(original)

    for x, y, col in sepiafied:
        check_equal('Checking pixel @({},{})'.format(x, y), col, Cimpl.get_color(expected, x, y))


test_sepia()
