
from T121_image_filters import *

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

def check_equal_ibrahim(expected, outcome):
    """
    The Author: Ibrahim Kasim
    check_equal(expected:Cimpl.Image,outcome:Cimpl.Image) -> Bool:
    Returns boolean statement. It checks if two images match. 
    """
    var1 = expected
    var2 = outcome
    test_increase = 0
    for x, y, (r, g, b) in var1:
        colour_tuple = Cimpl.get_color(var2, x, y)
        if r != colour_tuple[0] or g != colour_tuple[1] or b != colour_tuple[2]:
            test_increase += 1
            print("difference detected on the point ({},{}):".format(x, y))
            print("The pixel of the expected image:({},{},{}) vs. pixel of the outcome image:({},{},{}))".format(r, g, b, colour_tuple[0], colour_tuple[1], colour_tuple[2]))

    if test_increase > 0:
        print("The result of your comparison:", False)

    else:
        print("The result of your comparison:", True)

def test_detect_edges_better() -> bool:
    """ The author: Ibrahim Kasim
    It returns true or false depending on whether the improved edge detection
    filter works. The threshold value
    will be 4 for in this function.
    """
    original_image = Cimpl.create_image(6, 2)  # original image has to have a height
    # of 6 and width of 2 in order to consider 5 cases.

    # The first boundary case:
    # if the difference in the brightness of the top pixel and the bottom pixel
    # is less than the threshold value.
    # The top pixel will be set to white pixel. (23,23,23) -> (255,255,255)
    # pixels: top (23,23,23), bottom (20,20,20), right (23,23,23)
    Cimpl.set_color(original_image, 0, 0, Cimpl.create_color(23, 23, 23))
    Cimpl.set_color(original_image, 1, 0, Cimpl.create_color(20, 20, 20))
    Cimpl.set_color(original_image, 0, 1, Cimpl.create_color(23, 23, 23))

    # The second boundary case:
    # if the difference in the brightness of the top pixel and the bottom pixel
    # is equal to the threshold value.
    # The top pixel will be set to black pixel. (20,20,20) -> (0,0,0)
    # pixels: top (20,20,20), bottom (16,16,16), right (20,20,20)

    Cimpl.set_color(original_image, 2, 0, Cimpl.create_color(16, 16, 16))
    Cimpl.set_color(original_image, 1, 1, Cimpl.create_color(20, 20, 20))

    # The third boundary case:
    # if the difference in the brightness of the top pixel and the bottom pixel
    # is greater than the threshold value.
    # The top pixel will be set to black pixel. (20,20,20) -> (0,0,0)
    # pixels: top (16,16,16), bottom (21,21,21), right (16,16,16)

    Cimpl.set_color(original_image, 3, 0, Cimpl.create_color(21, 21, 21))
    Cimpl.set_color(original_image, 2, 1, Cimpl.create_color(16, 16, 16))

    # The fourth boundary case:(the first case of right pixel)
    # if the difference in the brightness of the top pixel and the bottom pixel
    # is less than the threshold value.
    # if the difference in the brightness of the top and the right pixel is
    # equal to the threshold value.
    # The top pixel will be set to black pixel. (20,20,20) -> (0,0,0)
    # pixels: top (21,21,21), bottom (21,21,21), right (0,0,0)

    Cimpl.set_color(original_image, 4, 0, Cimpl.create_color(21, 21, 21))
    Cimpl.set_color(original_image, 3, 1, Cimpl.create_color(25, 25, 25))

    # The fifth boundary case:(the second case of right pixel)
    # if the difference in the brightness of the top pixel and the bottom pixel
    # is less than the threshold value.
    # if the difference in the brightness of the top and the right pixel is
    # greater than the threshold value.
    # The top pixel will be set to black pixel. (21,21,21) -> (0,0,0)
    # pixels: top (21,21,21), bottom (21,21,21), right (26,26,26)

    Cimpl.set_color(original_image, 5, 0, Cimpl.create_color(21, 21, 21))
    Cimpl.set_color(original_image, 4, 1, Cimpl.create_color(26, 26, 26))
    # the right of the last one
    Cimpl.set_color(original_image, 5, 1, Cimpl.create_color(255, 255, 255))

    expected = Cimpl.create_image(6, 2)
    # (23,23,23) -> (255,255,255)
    Cimpl.set_color(expected, 0, 0, Cimpl.create_color(255, 255, 255))
    # (20,20,20) -> (0,0,0)
    Cimpl.set_color(expected, 1, 0, Cimpl.create_color(0, 0, 0))
    # (20,20,20) -> (0,0,0)
    Cimpl.set_color(expected, 2, 0, Cimpl.create_color(0, 0, 0))
    # (20,20,20) -> (0,0,0)
    Cimpl.set_color(expected, 3, 0, Cimpl.create_color(0, 0, 0))
    # (21,21,21) -> (0,0,0)
    Cimpl.set_color(expected, 4, 0, Cimpl.create_color(0, 0, 0))
    # the last row has to be whited
    Cimpl.set_color(original_image, 5, 0, Cimpl.create_color(255, 255, 255))

    # right (23,23,23) -> (255,255,255)
    Cimpl.set_color(expected, 0, 1, Cimpl.create_color(255, 255, 255))
    # right (20,20,20) -> (0,0,0)
    Cimpl.set_color(expected, 1, 1, Cimpl.create_color(0, 0, 0))
    # right (16,16,16) -> (0,0,0)
    Cimpl.set_color(expected, 2, 1, Cimpl.create_color(0, 0, 0))
    # right (0,0,0) -> (0,0,0)
    Cimpl.set_color(expected, 3, 1, Cimpl.create_color(0, 0, 0))
    # right (26,26,26) -> (0,0,0)
    Cimpl.set_color(expected, 4, 1, Cimpl.create_color(0, 0, 0))
    # the last row has to be whited
    Cimpl.set_color(original_image, 5, 1, Cimpl.create_color(255, 255, 255))

    check_equal_ibrahim(expected, detect_edges_better(original_image, 4))


def test_sepia() -> bool:
    """
    The author: Ibrahim Kasim
    It returns true or false.  
    """
    original_image = Cimpl.create_image(5, 1)  # expected image has to have a height of 5 to cover 5 different cases.
    Cimpl.set_color(original_image, 0, 0, Cimpl.create_color(1, 22, 22))  # grayscale filter applied: Color(red=15, green=15, blue=15), below 63
    Cimpl.set_color(original_image, 1, 0, Cimpl.create_color(100, 0, 89))  # grayscale filter applied: Color(red=63, green=63, blue=63) , it is equal to 63, the boundary
    Cimpl.set_color(original_image, 2, 0, Cimpl.create_color(100, 100, 25))  # grayscale filter applied: Color(red=75, green=75, blue=75), a value between 63 and 191
    Cimpl.set_color(original_image, 3, 0, Cimpl.create_color(200, 200, 173))  # grayscale filter applied: Color(red=191, green=191, blue=191), it is equal to 193, the boundary
    Cimpl.set_color(original_image, 4, 0, Cimpl.create_color(244, 177, 210))  # grayscale filter applied: Color(red=210, green=210, blue=210), above the boundary 191

    expected = Cimpl.create_image(5, 1)  # expected image has to have a height of 5 to cover 5 different cases after gray_scale filter apllied:
    Cimpl.set_color(expected, 0, 0, Cimpl.create_color(16, 15, 13))  # the red component multipled by 1.1, blue by 0.9 since it is filtered to dark gray.
    Cimpl.set_color(expected, 1, 0, Cimpl.create_color(72, 63, 63))  # the red component multipled by 1.15, blue by 0.85 since it is filtered to medium gray.
    Cimpl.set_color(expected, 2, 0, Cimpl.create_color(86, 75, 75))  # the red component multipled by 1.15, blue by 0.85 since it is filtered to medium gray.
    Cimpl.set_color(expected, 3, 0, Cimpl.create_color(219, 191, 191))  # the red component multipled by 1.15, blue by 0.85 since it is filtered to medium gray.
    Cimpl.set_color(expected, 4, 0, Cimpl.create_color(226, 210, 195))  # the red component multipled by 1.08, blue by 0.93 since it is filtered to light gray.

    check_equal_ibrahim(expected, sepia(original_image))

def check_equal_channel_colours(expected: Cimpl.Image, outcome: Cimpl.Image) -> None:
    """
    Author: Zakaria Ismail

    NOTE: THIS WAS DONE BEFORE WE WERE INFORMED TO USE THE check_equal
    SUPPLIED BY THE PROFESSORS

    Checks if PARAMETERS expected and outcome,
    both Cimpl.Image objects are:
        1. Of the same type
        2. Have the same pixel at each location - Quantitatively the same
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

def test_extreme_contrast() -> None:
    """
    Author:YANGLONG LIU
    extreme_contrast test function
    
    """

    raw = Cimpl.create_image(6, 1)

    Cimpl.set_color(raw, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(raw, 1, 0, Cimpl.create_color(1, 1, 1))
    Cimpl.set_color(raw, 2, 0, Cimpl.create_color(123, 123, 123))
    Cimpl.set_color(raw, 3, 0, Cimpl.create_color(128, 128, 128))
    Cimpl.set_color(raw, 4, 0, Cimpl.create_color(129, 129, 129))
    Cimpl.set_color(raw, 5, 0, Cimpl.create_color(255, 255, 255))

    expected = Cimpl.create_image(6, 1)

    Cimpl.set_color(expected, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 1, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 2, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 3, 0, Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 4, 0, Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 5, 0, Cimpl.create_color(255, 255, 255))

    extreme_contrasted = extreme_contrast(raw)

    for x, y, col in extreme_contrasted:
        check_equal('Checking pixel @({},{})'.format(x, y), col, get_color(expected, x, y))


def test_detect_edges():
    """author: YANGLONG LIU 101141366
    #create a image with six pixels and keep x unchanged, change y's value 
    #because we should check a pixle below one. 
    """
    original = Cimpl.create_image(1, 6)
    Cimpl.set_color(original, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(original, 0, 1, Cimpl.create_color(0, 0, 1))
    Cimpl.set_color(original, 0, 2, Cimpl.create_color(127, 127, 127))
    Cimpl.set_color(original, 0, 3, Cimpl.create_color(125, 73, 224))
    Cimpl.set_color(original, 0, 4, Cimpl.create_color(254, 255, 255))
    Cimpl.set_color(original, 0, 5, Cimpl.create_color(255, 255, 255))

    expected = Cimpl.create_image(1, 6)
    Cimpl.set_color(expected, 0, 0, Cimpl.create_color(255, 255, 255))  # contrast is lower, change to white
    Cimpl.set_color(expected, 0, 1, Cimpl.create_color(0, 0, 0))  # contrast is lower, change to black
    Cimpl.set_color(expected, 0, 2, Cimpl.create_color(0, 0, 0))  # contrast is lower, change to black
    Cimpl.set_color(expected, 0, 3, Cimpl.create_color(0, 0, 0))  # contrast is lower, change to black
    Cimpl.set_color(expected, 0, 4, Cimpl.create_color(0, 0, 0))  # contrast is lower, change to black
    Cimpl.set_color(expected, 0, 5, Cimpl.create_color(255, 255, 255))  # the bottom row, change to white

    edge_image = detect_edges(original, 2)
    for x, y, col in edge_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, Cimpl.get_color(expected, x, y))

def test_flip_horizontal():
    '''
    A test function for flip_horizontal.
    Author: Himanshu Singh
    
    >>> test_flip_horizontal()
    Checking pixel @(0, 0) PASSED
    
    checks if flip_horizontal correctly transforms:
    # (50, 100, 200) to (3, 2, 1)  # center pixels flipped
    #(0, 0, 0) to (255, 255, 255) # top pixel flipped to lower pixel
    # (255, 255, 255)to (0, 0, 0)  # lower pixel flipped to top pixel
    # (3, 2, 1) to (50, 100, 200)  # center pixels flipped 

    '''

    # create image with 4 vertical pixels
    original = Cimpl.create_image(1, 4)
    Cimpl.set_color(original, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(original, 0, 1, Cimpl.create_color(3, 2, 1))
    Cimpl.set_color(original, 0, 2, Cimpl.create_color(50, 100, 200))
    Cimpl.set_color(original, 0, 3, Cimpl.create_color(255, 255, 255))

    # create image identical image to the return image of an actual
    # horizontal flip function.

    expected = Cimpl.create_image(1, 4)
    Cimpl.set_color(expected, 0, 0, Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 0, 1, Cimpl.create_color(50, 100, 200))
    Cimpl.set_color(expected, 0, 2, Cimpl.create_color(3, 2, 1))
    Cimpl.set_color(expected, 0, 3, Cimpl.create_color(0, 0, 0))

    # now compare the two images.

    flip_horizontal_image = flip_horizontal(original)
    for x, y, col in flip_horizontal_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, Cimpl.get_color(expected, x, y))


def test_posterize():
    """
    This test_function tests the posterize() function.
    
    >>>test_posterize()
    checking pixel @(x,y) FAILED/PASSED
    
    """
    # testing all three channels at the same time for each case as it would be
    # easier and less tedious as opposed to replicating each combination which would
    # be unnessessary and a waste of time.
    normal = Cimpl.create_image(12, 1)

    Cimpl.set_color(normal, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(normal, 1, 0, Cimpl.create_color(1, 1, 1))
    Cimpl.set_color(normal, 2, 0, Cimpl.create_color(63, 63, 63))
    Cimpl.set_color(normal, 3, 0, Cimpl.create_color(64, 64, 64))
    Cimpl.set_color(normal, 4, 0, Cimpl.create_color(65, 65, 65))
    Cimpl.set_color(normal, 5, 0, Cimpl.create_color(127, 127, 127))
    Cimpl.set_color(normal, 6, 0, Cimpl.create_color(128, 128, 128))
    Cimpl.set_color(normal, 7, 0, Cimpl.create_color(129, 129, 129))
    Cimpl.set_color(normal, 8, 0, Cimpl.create_color(191, 191, 191))
    Cimpl.set_color(normal, 9, 0, Cimpl.create_color(192, 192, 192))
    Cimpl.set_color(normal, 10, 0, Cimpl.create_color(193, 193, 193))
    Cimpl.set_color(normal, 11, 0, Cimpl.create_color(255, 255, 255))

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

    posterized = posterize(normal)

    for x, y, col in posterized:
        check_equal(Cimpl.get_color(expected, x, y), Cimpl.get_color(posterized, x, y))
        check_equal(Cimpl.get_color(normal, x, y), Cimpl.get_color(posterized, x, y))

test_two_tone()
test_flip_vertical()
test_three_tone()
test_detect_edges_better()
test_sepia()
# NOTE: this is the test function for red_channel, green_channel, blue_channel, and combine
# check_equal_channel_colours()   
test_extreme_contrast()
test_detect_edges_better()
test_flip_horizontal()
test_posterize()

