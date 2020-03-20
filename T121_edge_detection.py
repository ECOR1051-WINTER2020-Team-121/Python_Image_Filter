import Cimpl

def detect_edges(original_image:Cimpl.Image,threshold:float)-> Cimpl.Image:
    """ The author: Ibrahim Kasim
    returns a copy of the original image with edge detection filter apllied to it."""
    new_image = Cimpl.copy(original_image)
    total_width = Cimpl.get_width(original_image)
    total_height = Cimpl.get_height(original_image)
    blacked = Cimpl.create_color(0,0,0)
    whited = Cimpl.create_color(255,255,255)

    for x,y, pixels in original_image:
        if x != total_width and y != total_height - 1:
            pixel_top = Cimpl.get_color(original_image,x,y)
            pixel_bottom = Cimpl.get_color(original_image,x,y+1)
            
            average_top = (pixel_top[0] + pixel_top[1] + pixel_top[2]) / 3 
            average_bottom = (pixel_bottom[0] + pixel_bottom[1] + pixel_bottom[2]) / 3 
            difference = abs(average_bottom - average_top)
            
            if difference > threshold:
                Cimpl.set_color(new_image,x,y,blacked) 
            else:
                Cimpl.set_color(new_image,x,y,whited)
        elif x == total_width:
            Cimpl.set_color(new_image,x,y,whited) 
    Cimpl.show(new_image)


var1 = Cimpl.choose_file()
original_image = Cimpl.load_image(var1)
detect_edges(original_image,4)