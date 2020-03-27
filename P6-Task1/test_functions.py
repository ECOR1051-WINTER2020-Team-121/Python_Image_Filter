import Cimpl


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


