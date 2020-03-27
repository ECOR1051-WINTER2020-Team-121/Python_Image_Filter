from Cimpl import *
from simple_Cimpl_filters import grayscale


original_image =  load_image('p2-original,png.png')
raw_image=copy(original_image)
new_image=grayscale(raw_image)
show(new_image)
def sepia(image):
    """
    Author: YANGLONG LIU
    return a grayscaled Image object after being passed a Image object.
    """    
    hgt=get_height(image)
    wth=get_width(image)
    for x in range(wth):
        for y in range(hgt):
            red, green, blue = get_color(new_image,x,y)
            if red<63 :
                blue=blue*0.9
                red=red*1.1
            elif 63<=red and 193>=red:
                blue=blue*0.85
                red= red*1.15
            elif red>191:
                blue=blue*0.93
                red=red*1.08
            new_color=create_color(red,blue,green)
            set_color(new_image,x,y,new_color)
    return new_image
sepia(new_image)
show(new_image)
    



            
           
            


    
