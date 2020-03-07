import Cimpl


def red_channel(img):
    """
    Author: Zakaria Ismail

    RETURNS an ImageObject where
    every pixel's channels except for
    red have been set to 0.
    """
    hgt = Cimpl.get_height(img)
    wth = Cimpl.get_width(img)

    for y in range(hgt):
        for x in range(wth):
            r, g, b = Cimpl.get_color(img, x, y)
            Cimpl.set_color(img, x, y, Cimpl.create_color(r, 0, 0))
    Cimpl.save_as(img, 'redFiltered.png')
    return img


def test_red_channel(filtered_img, ideal_img) -> str:
    """
    Author: Zakaria Ismail

    Compares each pixel in the filtered
    original image and in the ideal result.
    """
    hgt = Cimpl.get_height(filtered_img)
    wth = Cimpl.get_width(filtered_img)

    for y in range(hgt):
        for x in range(wth):
            if Cimpl.get_color(filtered_img, x, y) != Cimpl.get_color(ideal_img, x, y):
                return "ERROR: UNIDENTICAL PIXELS AT x:{} y:{} {} {} ".format(x, y,Cimpl.get_color(filtered_img, x, y), Cimpl.get_color(ideal_img, x, y))
    return "SUCCESS: NO DISCREPANCY DETECTED"


og_img = Cimpl.create_image(50, 50, Cimpl.create_color(255, 255, 255))  # original image: white image
ideal_img = Cimpl.create_image(50, 50, Cimpl.create_color(255, 0, 0))   # ideal result: all red image - each pix at 255r

filtered_og = red_channel(og_img)
print(test_red_channel(filtered_og, ideal_img))


Cimpl.show(filtered_og)

