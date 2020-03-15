
import Cimpl
from T121_P4_posterize import posterize


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


def test_posterize() -> None:
    """
    Tests function posterize

    >>> test_posterize()
    """
    # This test will involve a transformation from original -> Posterized (Decreased number of colours)

    # Quadrant definitions:
    #   I: 0-63
    #   II: 64-127
    #   III: 128-191
    #   IV: 192-255

    # ** Testing each combination would be too tiresome... Better to test if it transforms each RGB case at the same time.

    # This function will test if function posterize() correctly transforms:
    # 0. (0, 0, 0) -> (31, 31, 31)  # Q1 Lower Boundary channel values
    # 1. (1, 1, 1) -> (31, 31, 31)  # Q1 non-boundary channel values
    # 2. (63, 63, 63) -> (31, 31, 31)   # Q1 Upper Boundary channel values
    # 3. (64, 64, 64) -> (95, 95, 95)   # Q2 Lower Boundary channel values
    # 4. (65, 65, 65) -> (95, 95, 95)   # Q2 non-boundary channel values
    # 5. (127, 127, 127) -> (95, 95, 95)    # Q2 Upper Boundary channel values
    # 6. (128, 128, 128) -> (159, 159, 159) # Q3 Lower boundary channel values
    # 7. (129, 129, 129) -> (159, 159, 159) # Q3 non-boundary channel values
    # 8. (191, 191, 191) -> (159, 159, 159) # Q3 Upper boundary channel values
    # 9. (192, 192, 192) -> (223, 223, 223) # Q4 Lower Boundary channel values
    # 10. (193, 193, 193) -> (223, 223, 223)    # Q4 non-boundary channel values
    # 11. (255, 255, 255) -> (223, 223, 223)    # Q4 Upper boundary channel values

    # 12 test cases. Therefore, image with 12 pixels is created
    original = Cimpl.create_image(12, 1)

    Cimpl.set_color(original, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(original, 1, 0, Cimpl.create_color(1, 1, 1))
    Cimpl.set_color(original, 2, 0, Cimpl.create_color(63, 63, 63))
    Cimpl.set_color(original, 3, 0, Cimpl.create_color(64, 64, 64))
    Cimpl.set_color(original, 4, 0, Cimpl.create_color(65, 65, 65))
    Cimpl.set_color(original, 5, 0, Cimpl.create_color(127, 127, 127))
    Cimpl.set_color(original, 6, 0, Cimpl.create_color(128, 128, 128))
    Cimpl.set_color(original, 7, 0, Cimpl.create_color(129, 129, 129))
    Cimpl.set_color(original, 8, 0, Cimpl.create_color(191, 191, 191))
    Cimpl.set_color(original, 9, 0, Cimpl.create_color(192, 192, 192))
    Cimpl.set_color(original, 10, 0, Cimpl.create_color(193, 193, 193))
    Cimpl.set_color(original, 11, 0, Cimpl.create_color(255, 255, 255))

    # an ideal image with the corresponding expected results is created
    expected = Cimpl.create_image(12, 1)

    Cimpl.set_color(expected, 0, 0, Cimpl.create_color(31, 31, 31))
    Cimpl.set_color(expected, 1, 0, Cimpl.create_color(31, 31, 31))
    Cimpl.set_color(expected, 2, 0, Cimpl.create_color(31, 31, 31))
    Cimpl.set_color(expected, 3, 0, Cimpl.create_color(95, 95, 95))
    Cimpl.set_color(expected, 4, 0, Cimpl.create_color(95, 95, 95))
    Cimpl.set_color(expected, 5, 0, Cimpl.create_color(95, 95, 95))
    Cimpl.set_color(expected, 6, 0, Cimpl.create_color(159, 159, 159))
    Cimpl.set_color(expected, 7, 0, Cimpl.create_color(159, 159, 159))
    Cimpl.set_color(expected, 8, 0, Cimpl.create_color(159, 159, 159))
    Cimpl.set_color(expected, 9, 0, Cimpl.create_color(223, 223, 223))
    Cimpl.set_color(expected, 10, 0, Cimpl.create_color(223, 223, 223))
    Cimpl.set_color(expected, 11, 0, Cimpl.create_color(223, 223, 223))

    # Transforms the original image
    posterized = posterize(original)

    for x, y, col in posterized:
        check_equal('Checking pixel @({},{})'.format(x, y), col, Cimpl.get_color(expected, x, y))


test_posterize()
