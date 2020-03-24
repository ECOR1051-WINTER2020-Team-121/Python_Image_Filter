"""
#Group: Himanshu Singh, Zakaria Ismail, Ibrahim Kasim, Yang Long Liu
group number: 121
author: himanshu singh
"""
import Cimpl


def flip_vertical(img: Cimpl.Image) -> Cimpl.Image:
    """
    author: himanshu singh
    flips the image vertically (Cimpl.Image object) and returns it when called.
    """
    newimage = Cimpl.copy(img)
    
    height1 = Cimpl.get_height(img)
    
    width1 = Cimpl.get_width(img)
    
    for y in range(height1):
        for x in range(width1):
            
            change = height1-y-1
            Cimpl.set_color(newimage, x, y, Cimpl.get_color(img, x, change))
            Cimpl.set_color(newimage, x, change, Cimpl.get_color(img, x, y)) 
            
    Cimpl.save_as(newimage,"flipped.jpg")
    Cimpl.show(newimage)
    Cimpl.show(img)
    return newimage    

flip_vertical(Cimpl.load_image("miss_sullivan.jpg"))