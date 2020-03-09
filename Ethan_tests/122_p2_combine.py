import Cimpl


class person:
    def __init__(self):
        pass

    def asian(self):
        pass

    def glasses(self):
        pass


def combine(r_img, g_img, b_img):
    """ (Cimple.Image, Cimple.Image, Cimple.Image) -> Cimple.Image
    Returns a combination of 3 images.
    """
    combined_image = Cimpl.Image(Cimpl.get_width(r_img), Cimpl.get_height(r_img))
    for r_pixel, g_pixel, b_pixel in zip(r_img, g_img, b_img):
        Cimpl.set_color(combined_image, Cimpl.r_pixel[0], Cimpl.r_pixel[1],
                        Cimpl.create_color(Cimpl.r_pixel[2][0], Cimpl.g_pixel[2][1], Cimpl.b_pixel[2][2]))
    return combined_image


def check_equal(expected, actual) -> None:
    whatever = True
    for e_pixel, a_pixel in zip(expected, actual):
        if e_pixel != a_pixel:
            whatever = False
    print(whatever)


blue_img = Cimpl.load_image('blue_image.png')
green_img = Cimpl.load_image('green_image.png')
red_img = Cimpl.load_image('red_image.png')
expected = Cimpl.load_image('p2-original.jpg')

outcome = combine(red_img, green_img, blue_img)
Cimpl.show(outcome)

check_equal(expected, outcome)

