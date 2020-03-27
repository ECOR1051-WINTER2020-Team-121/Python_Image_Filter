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
    
    >>> flip_vertical(Cimpl.load_image("image.jpg"))
    returns a vertically flipped image

    """
    newimage = Cimpl.copy(img)

    height1 = Cimpl.get_height(img) #get image height

    width1 = Cimpl.get_width(img) #get image width

    for y in range(height1):
        
        for x in range(width1):

            change = height1 - y - 1
            #editing height to flip vertically (change)
            #change implemented below to make changes to the actual image passed 
            #in below 
            Cimpl.set_color(newimage, x, y, Cimpl.get_color(img, x, change))
            Cimpl.set_color(newimage, x, change, Cimpl.get_color(img, x, y))

    return newimage

flip_vertical(Cimpl.load_image("miss_sullivan.jpg"))
