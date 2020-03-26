import Cimpl
import simple_Cimpl_filters
import T121_sepia


def check_equal(expected, outcome):
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

    check_equal(expected, T121_sepia.sepia_channel(original_image))


test_sepia()

