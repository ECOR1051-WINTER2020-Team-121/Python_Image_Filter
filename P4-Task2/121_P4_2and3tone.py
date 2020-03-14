#twotone and threetone

"""
#Group: Himanshu Singh, Zakaria Ismail, Ibrahim Kasim, Yang Long Liu
group number: 121
author: himanshu singh
"""
from Cimpl import *
color1 = create_color(0, 0, 0) #black

color2 = create_color(255,255,255) #white
                     
color3 = create_color(128,128,128) # gray

FILENAME = input()

def brightness(r,g,b):
    """
    author: himanshu singh
    this returns the brightness of a pixel at a certain (x,y) coordinate.
    
    """
    brightness = (r + g + b)/3
    return brightness

def twotone(str, color1, color2):
    
    """
    author: himanshu singh
    this replaces the original color of a pixel with either black or white
    depending on the calculated brightness of the pixel
    
    
    """
    image = load_image(FILENAME)
    newimage = copy(image)    
    
    for x, y, (r, g, b) in image:
        bright = brightness(r,g,b)
    
        if bright <=127:
            black = create_color(0,0,0)
            set_color(newimage, x, y, color1)
            
        
        else:
            set_color(newimage, x, y, color2)
            
    save_as(newimage,"2toneoutcome.jpg")
    show(newimage)
    show(image)
    return newimage

def threetone(str, color1, color2, color3):
    """
    
    author: himanshu singh
    this replaces the original color of a pixel with either black, grey or white
    depending on the calculated brightness of the pixel
    
    
    """
    image = load_image(FILENAME)
    newimage = copy(image)    
    
    for x, y, (r, g, b) in image:
        bright = brightness(r,g,b)
    
        if bright <= 84:
            set_color(newimage, x, y, color1)
        
        elif 84 < bright <= 170:
            set_color(newimage, x , y, color2)
        
        else:
            set_color(newimage, x, y, color3)
            
    save_as(newimage,"3toneoutcome.jpg")
    show(newimage)
    show(image)
    return newimage

twotone(FILENAME, color1, color2)
threetone(FILENAME, color1, color2, color3)

        