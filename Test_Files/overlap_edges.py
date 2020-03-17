
import Cimpl
from simple_Cimpl_filters import detect_edges_better
import math


def blackboard(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object with
    the dots from an image returned by FUNCTION
    detect_edges_better superimposed over
    img

    img is a Cimpl.Image object passed to the function

    >>> blackboard(img)
    ** How do I write these examples???
    """
    BLACK = Cimpl.create_color(0, 0, 0)
    WHITE = Cimpl.create_color(255, 255, 255)
    AVG_CONTRAST = 5.77
    img = Cimpl.copy(img)
    dotted_img = detect_edges_better(img, AVG_CONTRAST * math.pi)

    for x, y, (r, g, b) in img:
        if Cimpl.get_color(dotted_img, x, y) == BLACK:
            Cimpl.set_color(img, x, y, WHITE)
        else:
            Cimpl.set_color(img, x, y, BLACK)
    return img


def superimpose_two(img_1: Cimpl.Image, img_2: Cimpl.Image, c1: int, c2: int, multiple: int) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object with
    img_1 and img_2 superimposed (or blended?)
    by adding a pixel of each one at a time.
    Also allows brightness adjustment, using FUNCTION adjust_brightness.
    Now takes a positive integer multiple that determines the frequency
    that the second image's pixels are placed onto the image

    >>> superimpose_two(img1, img2, 10, -10)
    """
    img_1 = adjust_brightness(img_1, c1)
    img_2 = adjust_brightness(img_2, c2)
    canvas = Cimpl.copy(img_1)
    count = 0

    for x, y, (r, g, b) in canvas:
        if count % multiple == 0:
            Cimpl.set_color(canvas, x, y, Cimpl.get_color(img_2, x, y))
        count += 1
    return canvas


def adjust_brightness(img: Cimpl.Image, constant: int) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object whose
    brightness has been adjusted after being
    PASSED constant.

    constant is the value by which the brightness will increase or decrease

    >>> adjust_brightness(img, 10)
    """
    img = Cimpl.copy(img)

    for x, y, (r, g, b) in img:
        Cimpl.set_color(img, x, y, Cimpl.create_color(r+constant, g+constant, b+constant))
    return img


def smooth(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object
    that is smoothed by identifying the edges
    using FUNCTION blackboard() and averaging
    them out depending on the surrounding pixels

    Add a function that deletes the white dots from
    the dot_plan after passing through each matrix?

    >>> smooth(img)
    """
    WHITE = Cimpl.Color(255, 255, 255)
    img = Cimpl.copy(img)
    dot_plan = blackboard(img)

    for x, y, (r, g, b) in img:
        radius = 0
        out_of_range = False
        edge_detected = Cimpl.get_color(dot_plan, x, y) == WHITE
        if edge_detected:
            while edge_detected:
                radius += 1
                edge_detected = __analyze_matrix_edges__(img, dot_plan, x, y, radius)
                if edge_detected == 0:
                    out_of_range = True
                    # print("index out of range")
                # else:
                    # print("index NOT out of range")
            # print('left edge_detection')
            # print(edge_detected)
            # if edge_detected != 0:
            if edge_detected == False and type(edge_detected) == bool:
                # print(edge_detected)
                # print('inside smoothening')
                # smoothen matrix
                if out_of_range == False:
                    img, dot_plan = __smooth_matrix__(img, dot_plan, x, y, radius)
                    # print("matrix smoothened")
                # dot_plan = __clear_dot_plan__(dot_plan)
    return img


def __analyze_matrix_edges__(img: Cimpl.Image, dot_plan: Cimpl.Image, x: int, y: int, radius: int):
    """
    RETURNS whether there are
    edge pixels detected on the edges of the matrix.
    Returns True or False
    If 0 is returned, this is to tell that the matrix
    is on the edge and that you should not attempt to smooth it
    due to complications
    """
    wth = Cimpl.get_width(img)
    hgt = Cimpl.get_height(img)
    WHITE = Cimpl.create_color(255, 255, 255)
    if x - radius >= 0:
        start_x = x - radius
    else:
        return 0
    if x + radius < wth:
        end_x = x + radius
    else:
        return 0
    if y - radius >= 0:
        start_y = x - radius
    else:
        return 0
    if y + radius < hgt:
        end_y = y + radius
    else:
        return 0

    for j in range(start_y, end_y+1):
        for i in range(start_x, end_x+1):
            if (j == start_y or j == end_y) or (i == start_x or i == end_x):
                if Cimpl.get_color(dot_plan, i, j) == WHITE:
                    return True
    return False


def __smooth_matrix__(img: Cimpl.Image, dot_plan: Cimpl.Image, x: int, y: int, radius: int) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object
    where a certain set of pixels
    have been blended

    Blending technique: setting all of the
    pixels in the matrix to the average of
    each component.

    Also deletes the white dots in the dot plan
    """
    # get averages for each channel
    avg_r = 0
    avg_g = 0
    avg_b = 0
    pixels = 0
    start_x = x - radius
    end_x = x + radius
    start_y = x - radius
    end_y = x + radius

    for j in range(start_y, end_y+1):
        for i in range(start_x, end_x+1):
            r, g, b = Cimpl.get_color(img, i, j)
            avg_r += r
            avg_g += g
            avg_b += b
            pixels += 1
    avg_r /= pixels
    avg_g /= pixels
    avg_b /= pixels

    # set each pixel to the average
    for j in range(start_y, end_y+1):
        for i in range(start_x, end_x+1):
            Cimpl.set_color(img, i, j, Cimpl.Color(avg_r, avg_g, avg_b))
            Cimpl.set_color(dot_plan, i, j, Cimpl.Color(0, 0, 0))
    images = (img, dot_plan)
    return images


starter = Cimpl.load_image('miss_sullivan.jpg')
second = Cimpl.load_image('p2-original.jpg')
#dotted_img = blackboard(starter)
#Cimpl.show(dotted_img)




#blended = superimpose_two(starter, second, 0, 0, -5)
#Cimpl.show(blended)

#smoothened = smooth(starter)
#Cimpl.show(smoothened)
#Cimpl.save_as(smoothened, 'smoothened_sully.png')




