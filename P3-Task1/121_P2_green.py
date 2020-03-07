import Cimpl


def green_channel(img):
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject where
    every pixel's channels except for
    green have been set to 0.
    """
    hgt = Cimpl.get_height(img)
    wth = Cimpl.get_width(img)

    for y in range(hgt):
        for x in range(wth):
            r, g, b = Cimpl.get_color(img, x, y)
            Cimpl.set_color(img, x, y, Cimpl.create_color(0, g, 0))
    return img


def test_green_channel(filtered_img, ideal_img) -> str:
    """
    Author: Zakaria Ismail

    Compares each pixel in the filtered
    original image and in the ideal result.
    """
    hgt = Cimpl.get_height(filtered_img)
    wth = Cimpl.get_width(filtered_img)

    for y in range(hgt):
        for x in range(wth):
            r_f, g_f, b_f = Cimpl.get_color(filtered_img, x, y)
            r_i, g_i, b_i = Cimpl.get_color(ideal_img, x, y)
            #if Cimpl.get_color(filtered_img, x, y) != Cimpl.get_color(ideal_img, x, y):
                #return "ERROR: UNIDENTICAL PIXELS AT x:{} y:{}".format(Cimpl.get_color(filtered_img, x, y), Cimpl.get_color(ideal_img, x, y))
            for i in range(3):
                if abs(Cimpl.get_color(filtered_img, x, y)[i] - Cimpl.get_color(ideal_img, x, y)[i]) > 40:
                    return "ERROR: DIFFERENCE BETWEEN {} AND {} TOO GREAT AT x:{} and y:{}".format(Cimpl.get_color(filtered_img, x, y), Cimpl.get_color(ideal_img, x, y), x, y)

    return "SUCCESS: NO DISCREPANCY DETECTED"


og_img = Cimpl.create_image(50, 50, Cimpl.create_color(255, 255, 255))  # original image: white image
ideal_img = Cimpl.create_image(50, 50, Cimpl.create_color(0, 255, 0))   # ideal result: all red image - each pix at 255r

filtered_og = green_channel(og_img)
print(test_green_channel(filtered_og, ideal_img))

Cimpl.show(filtered_og)




