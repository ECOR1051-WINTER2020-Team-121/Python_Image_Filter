
"""
#Group: Himanshu Singh, Zakaria Ismail, Ibrahim Kasim, Yang Long Liu
group number: 121
author: himanshu singh
"""
from Cimpl import *
COLORS = {
    
"black": Color(0, 0, 0), #black
"white": Color(255,255,255), #white
"gray": Color(128,128,128), # gray
"red": Color(255,0,0), #red
"lime": Color(0,255,0), #lime
"blue": Color(0,0,255), #blue
"yellow": Color(255,255,0), #yellow
"cyan": Color(0,255,255), #cyan
"magenta": Color(255,0,255) #magenta

}
FILENAME = input()

def brightness(r: int, g: int, b:int ) -> int:
    """
    this returns the brightness of a pixel at a certain (x,y) coordinate.
    """
    brightness = (r + g + b)/3
    

    return brightness

def twotone(img: Image, col1, col2) -> Image:
    
    
    """
    Returns an image object that is in two tone. It does this by using brightness
    to determine whether a pixel will be black or white. Black if brightness
    less than or equal to 127, else it is white. Takes in the RGB components 
    of the original image at coordinates (x,y). Col1 and Col2 are color() objects
    that represent black and white in rgb components.
    e.g twotone(FILENAME,col1,col2)
    FILENAME is the original image, col1 and col2 are the two colors that are
    dealt with.
    """
    image = load_image(FILENAME)
    newimage = copy(image)    
    
    for x, y, (r, g, b) in image:
        bright = brightness(r,g,b)
    
        if bright <=127:
            black = create_color(0,0,0)
            set_color(newimage, x, y, col1)
            
        
        else:
            set_color(newimage, x, y, col2)
            
    save_as(newimage,"2toneoutcome.jpg")
    show(newimage)
    show(image)
    return newimage

col1 = COLORS['black']
col2 = COLORS['white']
col3 = COLORS['gray']
col4 = COLORS['red']
col5 = COLORS['lime']
col6 = COLORS['blue']
col7 = COLORS['yellow']
col8 = COLORS['cyan']
col9 = COLORS['magenta']
twotone(FILENAME, col1, col2)
