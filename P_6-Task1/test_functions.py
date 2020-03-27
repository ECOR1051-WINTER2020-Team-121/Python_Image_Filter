

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


def test_flip_vertical() -> None:
    """
    Author: Zakaria Ismail

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

    # However, case #3 and #4 cannot allow testing for an odd and an even width image,
    # so there will be TWO images tested

    #   Image 1: Tests border, non-border, and ODD heighted center pixel    (5 pixels)  1x5
    #   Image 2: Tests border, non-border, and EVEN heighted center pixel   (6 pixels)  1x6

    # NOTE: Listed pixels are ordered from top to bottom
    # (i.e the first border pixel is the top, while second border is bottom)

    # IMAGE 1 (5 pixels):
    #   Border: (0, 0, 0), (4, 4, 4) -> (4, 4, 4), (0, 0, 0)
    #   Non-border: (1, 1, 1), (3, 3, 3) -> (3, 3, 3), (1, 1, 1)
    #   Center: (2, 2, 2) -> (2, 2, 2)

    # IMAGE 2 (6 pixels):
    #   Border: (0, 0, 0), (5, 5, 5) -> (5, 5, 5), (0, 0, 0)
    #   Non-border: (1, 1, 1), (4, 4, 4) -> (4, 4, 4), (1, 1, 1)
    #   Center: (2, 2, 2), (3, 3, 3) -> (3, 3, 3), (2, 2, 2)

    # ORIGINAL IMAGE 1
    original_1 = Cimpl.create_image(1, 5)
    Cimpl.set_color(original_1, 0, 0, Cimpl.Color(0, 0, 0))
    Cimpl.set_color(original_1, 0, 1, Cimpl.Color(1, 1, 1))
    Cimpl.set_color(original_1, 0, 2, Cimpl.Color(2, 2, 2))
    Cimpl.set_color(original_1, 0, 3, Cimpl.Color(3, 3, 3))
    Cimpl.set_color(original_1, 0, 4, Cimpl.Color(4, 4, 4))

    # OUTCOME IMAGE 1
    outcome_1 = flip_vertical(original_1)

    # EXPECTED IMAGE 1
    expected_1 = Cimpl.create_image(1, 5)
    Cimpl.set_color(expected_1, 0, 0, Cimpl.Color(4, 4, 4))
    Cimpl.set_color(expected_1, 0, 1, Cimpl.Color(3, 3, 3))
    Cimpl.set_color(expected_1, 0, 2, Cimpl.Color(2, 2, 2))
    Cimpl.set_color(expected_1, 0, 3, Cimpl.Color(1, 1, 1))
    Cimpl.set_color(expected_1, 0, 4, Cimpl.Color(0, 0, 0))

    # ORIGINAL IMAGE 2
    original_2 = Cimpl.create_image(1, 6)
    Cimpl.set_color(original_2, 0, 0, Cimpl.Color(0, 0, 0))
    Cimpl.set_color(original_2, 0, 1, Cimpl.Color(1, 1, 1))
    Cimpl.set_color(original_2, 0, 2, Cimpl.Color(2, 2, 2))
    Cimpl.set_color(original_2, 0, 3, Cimpl.Color(3, 3, 3))
    Cimpl.set_color(original_2, 0, 4, Cimpl.Color(4, 4, 4))
    Cimpl.set_color(original_2, 0, 5, Cimpl.Color(5, 5, 5))

    # OUTCOME IMAGE 2
    outcome_2 = flip_vertical(original_2)

    # EXPECTED IMAGE 2
    expected_2 = Cimpl.create_image(1, 6)
    Cimpl.set_color(expected_2, 0, 0, Cimpl.Color(5, 5, 5))
    Cimpl.set_color(expected_2, 0, 1, Cimpl.Color(4, 4, 4))
    Cimpl.set_color(expected_2, 0, 2, Cimpl.Color(3, 3, 3))
    Cimpl.set_color(expected_2, 0, 3, Cimpl.Color(2, 2, 2))
    Cimpl.set_color(expected_2, 0, 4, Cimpl.Color(1, 1, 1))
    Cimpl.set_color(expected_2, 0, 5, Cimpl.Color(0, 0, 0))

    # IMAGE 1 TESTS
    print("\n---TESTING IMAGE 1---\n")
    for x, y, col in outcome_1:
        check_equal("Checking pixel @({},{})".format(x, y), col, Cimpl.get_color(expected_1, x, y))

    # IMAGE 2 TESTS
    print("\n---TESTING IMAGE 2---\n")
    for x, y, col in outcome_2:
        check_equal("Checking pixel @({},{})".format(x, y), col, Cimpl.get_color(expected_2, x, y))


def test_three_tone() -> None:
    """
    Author: Zakaria Ismail

    Tests FUNCTION three_tone.

    >>> test_three_tone()
    """
    # This test will involve a transformation from original -> Black, Gray, and White three toned

    # Brightness ranges: 0-84, 85-170, 171-255 (Low, Mid, High)

    # 0. (0, 0, 0) -> (0, 0, 0)    # Low zero (lower boundary) brightness pixel
    # 1. (0, 0, 1) -> (0, 0, 0)    # Low non-zero (non-boundary) brightness pixel
    # 2. (84, 84, 84) -> (0, 0, 0) # Low upper boundary brightness pixel
    # 3. (85, 85, 85) -> (128, 128, 128)   # Mid lower boundary brightness pixel
    # 4. (86, 85, 85) -> (128, 128, 128)   # Mid non-boundary brightness pixel
    # 5. (170, 170, 170) -> (128, 128, 128)    # Mid upper boundary brightness pixel
    # 6. (171, 171, 171) -> (255, 255, 255)    # High lower boundary brightness pixel
    # 7. (171, 171, 172) -> (255, 255, 255)    # High non-boundary brightness pixel
    # 8. (255, 255, 255) -> (255, 255, 255)    # High 255 (upper boundary) brightness pixel
    # Do I include non-gray pixels? I will not, because brightness is the dependent factor here.

    # 9 test cases. Therefore image with 9 pixels is created
    original = Cimpl.create_image(9, 1)

    Cimpl.set_color(original, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(original, 1, 0, Cimpl.create_color(0, 0, 1))
    Cimpl.set_color(original, 2, 0, Cimpl.create_color(84, 84, 84))
    Cimpl.set_color(original, 3, 0, Cimpl.create_color(85, 85, 85))
    Cimpl.set_color(original, 4, 0, Cimpl.create_color(86, 85, 85))
    Cimpl.set_color(original, 5, 0, Cimpl.create_color(170, 170, 170))
    Cimpl.set_color(original, 6, 0, Cimpl.create_color(171, 171, 171))
    Cimpl.set_color(original, 7, 0, Cimpl.create_color(171, 171, 172))
    Cimpl.set_color(original, 8, 0, Cimpl.create_color(255, 255, 255))

    # An ideal image with the corresponding expected results is created
    expected = Cimpl.create_image(9, 1)

    Cimpl.set_color(expected, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 1, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 2, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 3, 0, Cimpl.create_color(128, 128, 128))
    Cimpl.set_color(expected, 4, 0, Cimpl.create_color(128, 128, 128))
    Cimpl.set_color(expected, 5, 0, Cimpl.create_color(128, 128, 128))
    Cimpl.set_color(expected, 6, 0, Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 7, 0, Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 8, 0, Cimpl.create_color(255, 255, 255))

    # Transforms the original image.
    two_toned_image = three_tone(original, 'black', 'gray', 'white')

    for x, y, col in two_toned_image:
        check_equal('Checking pixel @({},{})'.format(x, y), col, Cimpl.get_color(expected, x, y))
