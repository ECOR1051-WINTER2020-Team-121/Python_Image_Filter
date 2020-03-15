import Cimpl


def posterize(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS an image where
    img has its RGB channels
    set to the midpoint of quadrants:
        0..63, 64..127, 128..191, and 192..255
    depending on where the color channel value is situated between

    img is a Cimpl.Image object passed to the function

    (How do I write the examples?)
    """