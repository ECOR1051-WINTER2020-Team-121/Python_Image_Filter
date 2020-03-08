import Cimpl
def green_channel():
    """
    The Author: Ibrahim Kasim
    green_channel(image:Cimpl.Image) -> Cimpl.Image:
    directs the user to choose an image that should be png, and 
    changes the green colour of the every individual pixels to the highest limit
    possible. 
    
    """
    
    image_file = Cimpl.choose_file()
    original_image = Cimpl.load_image(image_file)
    new_image = Cimpl.copy(original_image)
    for pixel in original_image:
        x,y,(r,g,b) = pixel
        green_color = Cimpl.create_color(r,255,b)
        Cimpl.set_color(new_image, x,y, green_color)
        
    Cimpl.show(new_image) 
    