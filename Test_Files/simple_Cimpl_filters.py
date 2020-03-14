import Cimpl


def grayscale(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a grayscaled
    Cimpl.Image object after
    being PASSEDD a Cimpl.Image object.
    """
    img = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        avg = (r + g + b) / 3
        Cimpl.set_color(img, x, y, Cimpl.create_color(avg, avg, avg))
    Cimpl.save_as(img, 'grayscaled.png')
    return img


def sepia(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a sepia filtered
    Cimpl.Image object after
    being PASSED a Cimpl.Image object
    """
    img = Cimpl.copy(img)
    img = grayscale(img)

    for x, y, (r, g, b) in img:
        if r < 63:
            b *= 0.9
            r *= 1.1
        elif 63 <= r <= 191:
            b += 0.85
            r *= 1.15
        else:
            b *= 0.93
            r *= 1.08
        Cimpl.set_color(img, x, y, Cimpl.create_color(r, g, b))
    Cimpl.save_as(img, 'sepiafied.png')
    return img


def posterize(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object
    whose RGB components have been rounded
    to the midpoint of the following quadrants:
        0 to 63, 64 to 127, 128 to 191, and 192 to 255
    Is PASSED a Cimpl.Image object
    """
    img = Cimpl.copy(img)
    for x, y, col in img:
        channels = []
        for ch in col:
            channels += [__adjust_component__(ch)]
        Cimpl.set_color(img, x, y, Cimpl.create_color(channels[0], channels[1], channels[1]))
    return img


def __adjust_component__(num: int) -> int:
    """
    RETURNS the midpoint of
    one of the following ranges,
    after being PASSED.
    """
    ranges = [63,127,191,255]
    mid = [31, 95, 159, 223]
    for i in range(len(ranges)):
        if num <= ranges[i]:
            return mid[i]


def woodcut(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image pbject with a
    woodcut effect, after being
    PASSED a Cimpl.Image object
    """
    img = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        avg = (r+g+b) / 3
        if avg <= 127:
            col = Cimpl.create_color(0, 0, 0)
        else:
            col = Cimpl.create_color(255, 255, 255)
        Cimpl.set_color(img, x, y, col)
    return img


def extreme_contrast(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object
    with pixels of extreme contrast,
    after being PASSED a Cimpl.Image object.
    """
    copy = Cimpl.copy(img)
    for x, y, col in img:
        channels = []
        for ch in col:
            if ch < 128:
                channels += [0]
            else:
                channels += [255]
        Cimpl.set_color(copy, x, y, Cimpl.create_color(channels[0], channels[1], channels[2]))
    return copy


def detect_edges(img: Cimpl.Image, thres) -> Cimpl.Image:
    """
    RETURNS...
    """
    copy = Cimpl.copy(img)
    hgt = Cimpl.get_height(img)
    for x, y, (r, g, b) in img:
        if y+1 < hgt:
            r2, g2, b2 = Cimpl.get_color(copy, x, y+1)
            contrast = abs((r + g + b)/3 - (r2 + g2 + b2)/3)
            #print(contrast)
            if contrast > thres:
                col = Cimpl.create_color(0, 0, 0)
                #print("HIGH")
            else:
                col = Cimpl.create_color(255, 255, 255)
                #print("LOW")
            Cimpl.set_color(copy, x, y, col)
    return copy


def detect_edges_better(img: Cimpl.Image, thres) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object.
    Is detect_edges, but better.
    """
    img = Cimpl.copy(img)
    hgt = Cimpl.get_height(img)
    wth = Cimpl.get_width(img)
    for x, y, (r, g, b) in img:
        if y + 1 < hgt:
            if x + 1 < wth:
                #print("It got in")
                r2, g2, b2 = Cimpl.get_color(img, x, y + 1)
                r3, g3, b3 = Cimpl.get_color(img, x + 1, y)
                contrast_bot = abs((r + g + b) / 3 - (r2 + g2 + b2) / 3)
                contrast_right = abs((r + g + b) / 3 - (r3 + g3 + b3) / 3)
                if contrast_bot > thres or contrast_right > thres:
                    col = Cimpl.create_color(0, 0, 0)
                else:
                    col = Cimpl.create_color(255, 255, 255)
        Cimpl.set_color(img, x, y, col)
    return img


def flip_vertical(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image
    that was flipped, after
    being PASSED a Cimpl.Image object
    """
    hgt = Cimpl.get_height(img)
    mid_y = hgt // 2
    wth = Cimpl.get_width(img)
    copy = Cimpl.copy(img)
    for y in range(mid_y):
        for x in range(wth):
            #r1, g1, b1 = Cimpl.get_color(img, x, y)
            #r2, g2, b2 = Cimpl.get_color(img, x, hgt-y)
            Cimpl.set_color(copy, x, y, Cimpl.get_color(img, x, hgt-y-1))
            Cimpl.set_color(copy, x, hgt-y-1, Cimpl.get_color(img, x, y))
    return copy


def flip_horizontal(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image
    that was flipped, after
    being PASSED a Cimpl.Image object
    """
    hgt = Cimpl.get_height(img)
    wth = Cimpl.get_width(img)
    mid_x = wth // 2
    copy = Cimpl.copy(img)
    for y in range(hgt):
        for x in range(mid_x):
            #r1, g1, b1 = Cimpl.get_color(img, x, y)
            #r2, g2, b2 = Cimpl.get_color(img, x, hgt-y)
            Cimpl.set_color(copy, x, y, Cimpl.get_color(img, wth-x-1, y))
            Cimpl.set_color(copy, wth-x-1, y, Cimpl.get_color(img, x, y))
    return copy


def two_tone(img: Cimpl.Image, tone_a: str, tone_b: str) -> Cimpl.Image:
    """
    RETURNS a Cimpl.Image object
    that was turned into a two toned image.
    Is PASSED a Cimpl.Image object,
    and two strings
    """
    COLOURS = {
        'black': Cimpl.Color(0, 0, 0),
        'white': Cimpl.Color(255, 255, 255),
        'red': Cimpl.Color(255, 0, 0),
        'lime': Cimpl.Color(0, 255, 0),
        'blue': Cimpl.Color(0, 0, 255),
        'yellow': Cimpl.Color(255, 255, 0),
        'cyan': Cimpl.Color(0, 255, 255),
        'magenta': Cimpl.Color(255, 0, 255),
        'gray': Cimpl.Color(128, 128, 128)
    }

    img = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        brightness = (r + g + b) / 3
        if brightness <= 127:
            Cimpl.set_color(img, x, y, COLOURS[tone_a])
        else:
            Cimpl.set_color(img, x, y, COLOURS[tone_b])
    return img


def three_tone(img: Cimpl.Image, tone_a: str, tone_b: str, tone_c: str) -> Cimpl.Image:
    """
        RETURNS a Cimpl.Image object
        that was turned into a two toned image.
        Is PASSED a Cimpl.Image object,
        and two strings
        """
    COLOURS = {
        'black': Cimpl.Color(0, 0, 0),
        'white': Cimpl.Color(255, 255, 255),
        'red': Cimpl.Color(255, 0, 0),
        'lime': Cimpl.Color(0, 255, 0),
        'blue': Cimpl.Color(0, 0, 255),
        'yellow': Cimpl.Color(255, 255, 0),
        'cyan': Cimpl.Color(0, 255, 255),
        'magenta': Cimpl.Color(255, 0, 255),
        'gray': Cimpl.Color(128, 128, 128)
    }

    img = Cimpl.copy(img)
    for x, y, (r, g, b) in img:
        brightness = (r + g + b) / 3
        if brightness <= 84:
            Cimpl.set_color(img, x, y, COLOURS[tone_a])
        elif 84 < brightness < 170:
            Cimpl.set_color(img, x, y, COLOURS[tone_b])
        else:
            Cimpl.set_color(img, x, y, COLOURS[tone_c])
    return img

"""
FUNCTION TEST CALLS:
"""
starter = Cimpl.load_image('miss_sullivan.png')
Cimpl.show(starter)
"""
grey = grayscale(Cimpl.load_image('miss_sullivan.png'))
Cimpl.show(grey)

sepia_img = sepia(Cimpl.load_image('miss_sullivan.png'))
Cimpl.show(sepia_img)

poste_img = posterize(Cimpl.load_image('miss_sullivan.png'))
Cimpl.show(poste_img)

wood_img = woodcut(Cimpl.load_image('miss_sullivan.png'))
Cimpl.show(wood_img)

extrem_img = extreme_contrast(Cimpl.load_image('miss_sullivan.png'))
Cimpl.show(extrem_img)

detec_img = detect_edges(Cimpl.load_image('miss_sullivan.png'), 5)
Cimpl.show(detec_img)

detec_better_img = detect_edges_better(Cimpl.load_image('miss_sullivan.png'), 5)
Cimpl.show(detec_better_img)

vert_img = flip_vertical(Cimpl.load_image('miss_sullivan.png'))
Cimpl.show(vert_img)

hori_img = flip_horizontal(Cimpl.load_image('miss_sullivan.png'))
Cimpl.show(hori_img)
"""
two_toned = two_tone(starter, input('Pick tone_1: '), input('Pick tone_2'))
Cimpl.show(two_toned)

three_toned = three_tone(starter, input('Pick tone_1'), input('Pick tone_2'), input('Pick tone_3'))
Cimpl.show(three_toned)

