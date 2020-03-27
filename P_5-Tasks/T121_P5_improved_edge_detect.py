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
        if y == hgt - 1:    # updated for new requirements
            Cimpl.set_color(img, x, y, Cimpl.create_color(255, 255, 255))
        elif y + 1 < hgt:
            if x + 1 < wth:
                #print("It got in")
                r2, g2, b2 = Cimpl.get_color(img, x, y + 1)
                r3, g3, b3 = Cimpl.get_color(img, x + 1, y)
                contrast_bot = abs((r + g + b) / 3 - (r2 + g2 + b2) / 3)
                contrast_right = abs((r + g + b) / 3 - (r3 + g3 + b3) / 3)

                #avg_contrast += (contrast_bot+contrast_right)/2
                if contrast_bot >= thres or contrast_right >= thres:    # changed to greater or equal
                    col = Cimpl.create_color(0, 0, 0)
                else:
                    col = Cimpl.create_color(255, 255, 255)
        Cimpl.set_color(img, x, y, col)
    #avg_contrast /= wth * hgt
    #print(avg_contrast)
    return img


Cimpl.show(detect_edges_better(Cimpl.load_image('miss_sullivan.png'), 10))