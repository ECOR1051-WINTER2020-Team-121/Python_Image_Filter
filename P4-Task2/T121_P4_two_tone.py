
"""
#Group: Himanshu Singh, Zakaria Ismail, Ibrahim Kasim, Yang Long Liu
group number: 121
author: himanshu singh
"""
import Cimpl


def _brightness(r: int, g: int, b: int) -> int:
    """
    Author: Himanshu Singh
    this returns the brightness of a pixel at a certain (x,y) coordinate.
    
    This is a helper function
    
    >>>_brightness(255,255,255)
    255
    """
    _brightness = (r + g + b) / 3

    return _brightness


def two_tone(img: Cimpl.Image, col1: str, col2: str) -> Cimpl.Image:
    """
    Author: Himanshu Singh
    Returns a two-toned Cimpl.Image object, based on the colors col1 and col2
    passed. 
    
    img is the original Cimpl.Image object passed
    
    col1 and col2 are the strings representing the image.
    
    >>>two_tone(Cimpl.load_image("image.jpg"), "col1", "col2")
    returns image with a two toned filter

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

    #image = load_image(FILENAME)
    newimage = Cimpl.copy(img)

    for x, y, (r, g, b) in img:
        bright = _brightness(r, g, b)
        
        
        if bright <= 127: 
        #if calculated brightness at said pixel is below 127 set color to col[1]        
            black = Cimpl.create_color(0, 0, 0)
            Cimpl.set_color(newimage, x, y, COLORS[col1])

        else:
        #else set color to col2 at said pixel
            Cimpl.set_color(newimage, x, y, COLORS[col2])


    return newimage


two_tone(Cimpl.load_image("miss_sullivan.jpg"), "black", "white")
