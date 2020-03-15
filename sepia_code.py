import Cimpl
import simple_Cimpl_filters
def sepia_channel(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS a sepia filtered
    Cimpl.Image object after
    being PASSED a Cimpl.Image object
    """
    img = Cimpl.copy(img)
    img = simple_Cimpl_filters.grayscale(img)
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
    Cimpl.show(img)
    return img
