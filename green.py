import Cimpl
def green_channel():
    """
    The Author: Ibrahim Kasim
    green_channel(image:Cimpl.Image) -> Cimpl.Image:
    directs the user to choose an image that should be png, and 
    changes the green colour of the every individual pixels to the highest limit
    possible. It saves the new image created under the name of 'outcome.png'. 
    
    """
    
    image_file = Cimpl.choose_file()
    original_image = Cimpl.load_image(image_file)
    new_image = Cimpl.copy(original_image)
    for pixel in original_image:
        x,y,(r,g,b) = pixel
        green_color = Cimpl.create_color(0,g,0)
        Cimpl.set_color(new_image, x,y, green_color)

    Cimpl.save_as(new_image, 'outcome.png')    
    Cimpl.show(new_image) 
    return new_image
    
def test_green_channel(expected, outcome):
    
    var1 = Cimpl.load_image(expected)
    var2 = Cimpl.load_image(outcome)
    Cimpl.show(var1)
    Cimpl.show(var2)
    """
    The Author: Ibrahim Kasim
    test_green_channel(expected:Cimpl.Image,outcome:Cimpl.Image) -> Bool:
    It checks if the pixel of the outcome image matches the pixel of expected image at each coordinate. It 
    returns True if they are identical, otherwise it returns False.

    """
    
    for x,y,(r,g,b) in var1:
        colour_tuple = Cimpl.get_color(var2,x,y)
        if r != colour_tuple[0] and g != colour_tuple[1] and b != colour_tuple[2]:
            print("The result of your comparison:")
            return False
    print("The result of your comparison:")
    return True
                
green_channel()
print(test_green_channel('green_image.png','riveter.jpg'))

#test
