
"""
#Group: Himanshu Singh, Zakaria Ismail, Ibrahim Kasim, Yang Long Liu
group number: 121
author: himanshu singh
"""
import Cimpl


def _brightness(r: int, g: int, b:int ) -> int:
    """
    this returns the brightness of a pixel at a certain (x,y) coordinate.
    """
    _brightness = (r + g + b)/3
    

    return _brightness

def two_tone(img: Cimpl.Image) -> Cimpl.Image:
    
    """
    Returns a two-toned Cimpl.Image object, based on the colors col1 and col2
    passed. 
    
    img is the original Cimpl.Image object passed
    
    col1 and col2 are the strings representing the image.
    """
    
    COLORS = {
        
    "black": Cimpl.Color(0, 0, 0), #black
    "white": Cimpl.Color(255,255,255), #white
    "gray": Cimpl.Color(128,128,128), # gray
    "red": Cimpl.Color(255,0,0), #red
    "lime": Cimpl.Color(0,255,0), #lime
    "blue": Cimpl.Color(0,0,255), #blue
    "yellow": Cimpl.Color(255,255,0), #yellow
    "cyan": Cimpl.Color(0,255,255), #cyan
    "magenta": Cimpl.Color(255,0,255) #magenta
    
    }    
    
    col1 = COLORS['black']
    col2 = COLORS['white']
    col3 = COLORS['gray']
    col4 = COLORS['red']
    col5 = COLORS['lime']
    col6 = COLORS['blue']
    col7 = COLORS['yellow']
    col8 = COLORS['cyan']
    col9 = COLORS['magenta']
    

    #image = load_image(FILENAME)
    newimage = Cimpl.copy(img)    
    
    for x, y, (r, g, b) in img:
        bright = _brightness(r,g,b)
    
        if bright <=127:
            black = Cimpl.create_color(0,0,0)
            Cimpl.set_color(newimage, x, y, col1)
            
        
        else:
            Cimpl.set_color(newimage, x, y, col2)
            
    Cimpl.save_as(newimage,"2toneoutcome.jpg")
    Cimpl.show(newimage)
    Cimpl.show(img)
    return newimage


two_tone(Cimpl.load_image("miss_sullivan.jpg"))