import Cimpl


def detect_edges(img: Cimpl.Image, thres: int) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object
    whose pixels have been changed
    to black or white dependent on its
    contrast with the pixel below it after
    being passed img and thres

    img is a Cimpl.Image object
    thres is a integer

    >>> detect_edges(Cimpl.load_image(choose_file()), 4)
    """
    black = Cimpl.Color(0, 0, 0)
    white = Cimpl.Color(255, 255, 255)
    copy = Cimpl.copy(img)
    hgt = Cimpl.get_height(copy)

    for x, y, (r, g, b) in copy:
        if y+1 < hgt:   # checks if pixel below exists
            r2, g2, b2 = Cimpl.get_color(copy, x, y+1)
            contrast = abs((r + g + b)/3 - (r2 + g2 + b2)/3)
            if contrast > thres:
                col = black
            else:
                col = white
            Cimpl.set_color(copy, x, y, col)
        else:
            Cimpl.set_color(copy, x, y, white)
    return copy


