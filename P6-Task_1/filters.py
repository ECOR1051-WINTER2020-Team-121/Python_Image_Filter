
def sepia(image):
    """
    Author: YANGLONG LIU
    return a grayscaled Image object after being passed a Image object.
    """
    hgt = Cimpl.get_height(image)
    wth = Cimpl.get_width(image)
    for x in range(wth):
        for y in range(hgt):
            red, green, blue = Cimpl.get_color(new_image, x, y)
            if red < 63:
                blue = blue * 0.9
                red = red * 1.1
            elif 63 <= red and 193 >= red:
                blue = blue * 0.85
                red = red * 1.15
            elif red > 191:
                blue = blue * 0.93
                red = red * 1.08
            new_color = Cimpl.create_color(red, blue, green)
            Cimpl.set_color(new_image, x, y, new_color)
    return new_image


def detect_edges_better(image: Image, threshold: int) -> Image:
    """
    Author:YANGLONG LIU 101141366
    returns a Image with only black and white color depending on the comparsion 
    between contrast and threshold.
    >>>improved_detect_image = detect_edges_better(raw_image, 13)
    >>>show(improved_detect_image) which returned image looks like pencil skectches.
    """
    new_image = Cimpl.copy(image)
    wdt = Cimpl.get_width(raw_image)
    hgt = Cimpl.get_height(raw_image)
    for x in range(wdt):
        for y in range(hgt):
            if y < hgt - 1:  # make a confirmation for the bottom line is not in this range
                red, green, blue = Cimpl.get_color(image, x, y)
                red1, green1, blue1 = Cimpl.get_color(image, x, y + 1)  # the pixel below the pixel of raw image one
                red2, green2, blue2 = Cimpl.get_color(image, x - 1, y)  # the right one of the pixel

                brightness1 = (red + blue + green) / 3
                brightness2 = (red1 + blue1 + green1) / 3
                brightness3 = (red2 + blue2 + green2) / 3

                contrast1 = abs(brightness2 - brightness1)
                contrast2 = abs(brightness3 - brightness1)

                if contrast1 > threshold or contrast2 > threshold:  # make a comparsion the contrast with threshold
                    red, green, blue = 0, 0, 0  # if the contrast is higher, change color to black.
                    black = Cimpl.create_color(red, green, blue)
                    Cimpl.set_color(Cimpl.new_image, x, y, black)

                else:
                    red, green, blue = 255, 255, 255  # if the contrast is lower, change color to white.
                    white = Cimpl.create_color(red, green, blue)
                    Cimpl.set_color(Cimpl.new_image, x, y, white)

            elif y == hgt - 1:  # the bottom row of the image which the bottom line is in this range
                red, green, blue = 255, 255, 255  # change to white simply.
                white = Cimpl.create_color(red, green, blue)
                Cimpl.set_color(Cimpl.new_image, x, y, white)

    return new_image
