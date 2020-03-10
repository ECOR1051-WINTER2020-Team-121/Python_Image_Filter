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
        green_color = Cimpl.create_color(0,g,0)
        Cimpl.set_color(new_image, x,y, green_color)
        
    Cimpl.show(new_image) 
<<<<<<< Updated upstream
    
=======
    
def test_green_channel(original_image,new_image):
    """ 
    test_green_channel(original_image:Cimpl.Image, new_image:Cimpl.Image )-> Bool :
   
    Tests to see if the pixels colour green of the original
    image is the same with the new image's green color pixel, whilst 
    the other colors set to zero. It has two arguments, first one is the original
    image, the second one is the new image with green filter applied.
    
    """
    for pixel in original_image:
        x,y,(r,g,b) = pixel
        if r != 0 and b != 0:
            return False
    
    return True
        
                
        
        
>>>>>>> Stashed changes
