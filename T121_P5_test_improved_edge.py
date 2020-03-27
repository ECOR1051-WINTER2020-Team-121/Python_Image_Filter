import Cimpl


def detect_edges_better(img: Cimpl.Image, thres: int) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object.
    Is detect_edges, but better.
    """
    img = Cimpl.copy(img)
    hgt = Cimpl.get_height(img)
    wth = Cimpl.get_width(img)
    #avg_contrast = 0
    for x, y, (r, g, b) in img:
        if y == hgt - 1 or x == wth - 1:    # updated for new requirements
            Cimpl.set_color(img, x, y, Cimpl.create_color(255, 255, 255))
        elif y + 1 < hgt:
            if x + 1 < wth:
                #print("It got in")
                r2, g2, b2 = Cimpl.get_color(img, x, y + 1)
                r3, g3, b3 = Cimpl.get_color(img, x + 1, y)
                contrast_bot = abs((r + g + b) / 3 - (r2 + g2 + b2) / 3)
                contrast_right = abs((r + g + b) / 3 - (r3 + g3 + b3) / 3)

                #avg_contrast += (contrast_bot+contrast_right)/2
                if contrast_bot >= thres or contrast_right >= thres:
                # changed to greater or equal
                    col = Cimpl.create_color(0, 0, 0)
                else:
                    col = Cimpl.create_color(255, 255, 255)
        Cimpl.set_color(img, x, y, col)
    #avg_contrast /= wth * hgt
    # print(avg_contrast)
    return img


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


def test_imp_edge_better() -> bool:
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

    check_equal(expected, detect_edges_better(original_image, 4))


# The test function call:
test_imp_edge_better()
