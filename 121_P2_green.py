import Cimpl
def green_channel():
    """
    The Author: Ibrahim Kasim
    green_channel() -> Cimpl.Image:
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
    
def check_equal(expected, outcome):
    
    var1 = Cimpl.load_image(expected)
    var2 = Cimpl.load_image(outcome)
    Cimpl.show(var1)
    Cimpl.show(var2)
    """
    The Author: Ibrahim Kasim
    check_equal(expected:Cimpl.Image,outcome:Cimpl.Image) -> Bool:
    It checks if the pixel of the outcome image matches the pixel of expected image at each coordinate. It 
    returns True if they are identical, otherwise it returns False. Before returning False, it prints the pixels
    and (x,y) coordinates of both images at which the images differ in pixel. 

    """
    test_increase = 0
    for x,y,(r,g,b) in var1:
        colour_tuple = Cimpl.get_color(var2,x,y)
        if r != colour_tuple[0] or g != colour_tuple[1] or b != colour_tuple[2]:
            test_increase += 1 
            print("difference detected on the point ({},{}):".format(x,y))
            print("The pixel of the expected image:({},{},{} vs. pixel of the outcome image:({},{},{}))".format(r,g,b,colour_tuple[0],colour_tuple[1],colour_tuple[2]))


    if test_increase > 0:        
        print("The result of your comparison:")
        return False
    else:
        print("The result of your comparison:")
        return True

#Testing        
green_channel()

# It will return True as the two images match.
print(check_equal('greenfiltered_.png','outcome.png'))


# This example check will return False, since the expected image is original image while the outcome is filtered.
# this was done to demonstrate how the test function works and it will print each points and the 
# respective pixels that are every time the pixels are different. 
print(check_equal('great_big_c.jpg','outcome.png'))


