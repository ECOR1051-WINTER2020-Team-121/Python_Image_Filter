"""
#Group: Himanshu Singh, Zakaria Ismail, Ibrahim Kasim, Yang Long Liu
group number: 121
author: himanshu singh
"""
import Cimpl


def _brightness(r: int, g: int, b: int) -> int:
    """
    author: Himanshu Singh
    this returns the brightness of a pixel at a certain (x,y) coordinate. 
    
    This is a helper function
    
    >>>_brightness(255,255,255)
    255
    """
    _brightness = (r + g + b) / 3

    return _brightness


def three_tone(img: Cimpl.Image, col1: str, col2: str, col3: str) -> Cimpl.Image:
    """
    Returns a three-toned Cimpl.Image object, based on the colors col1, col2
    and col3 passed. 
    
    img is the original Cimpl.Image object passed
    
    col1, col2 and col3 are the strings representing the image.
    
    >>>three_tone(Cimpl.load_image("image.jpg"), "col1", "col2", "col3")
    returns image with a three toned filter

    """
    COLORS = {

        "black": Cimpl.Color(0, 0, 0),  # black
        "white": Cimpl.Color(255, 255, 255),  # white
        "gray": Cimpl.Color(128, 128, 128),  # gray
        "red": Cimpl.Color(255, 0, 0),  # red
        "lime": Cimpl.Color(0, 255, 0),  # lime
        "blue": Cimpl.Color(0, 0, 255),  # blue
        "yellow": Cimpl.Color(255, 255, 0),  # yellow
        "cyan": Cimpl.Color(0, 255, 255),  # cyan
        "magenta": Cimpl.Color(255, 0, 255)  # magenta

    }

    newimage = Cimpl.copy(img)

    for x, y, (r, g, b) in img:
        bright = _brightness(r, g, b)

        if bright <= 84:
        #if brightness is below or equal to 84 change the color at said pixel to
        #col1
            Cimpl.set_color(newimage, x, y, COLORS[col1])

        elif 84 < bright <= 170:
        #if brightness is below or equal to 170 but higher than 84 change the   
        # color at said pixel to col2
            Cimpl.set_color(newimage, x, y, COLORS[col2])

        else:
        #else set color to col3
            Cimpl.set_color(newimage, x, y, COLORS[col3])

   
    return newimage


three_tone(Cimpl.load_image("miss_sullivan.jpg"), 'black', 'white', 'gray')
