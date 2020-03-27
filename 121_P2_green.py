import Cimpl
def green_channel():
    """
    The Author: Ibrahim Kasim
    green_channel() -> Cimpl.Image:
    Returns green filtered image. It directs user to choose an image that 
    is desired for filtering.
    
    """
    
    image_file = Cimpl.choose_file()
    original_image = Cimpl.load_image(image_file)
    new_image = Cimpl.copy(original_image)
    for pixel in original_image:
        x,y,(r,g,b) = pixel
        green_color = Cimpl.create_color(0,g,0)
        Cimpl.set_color(new_image, x,y, green_color)
    
    return new_image
    
def check_equal(expected, outcome):
    
    var1 = Cimpl.load_image(expected)
    var2 = Cimpl.load_image(outcome)
    """
    The Author: Ibrahim Kasim
    check_equal(expected:Cimpl.Image,outcome:Cimpl.Image) -> Bool:
    Returns boolean statement. It checks if two images match. 
    """
    test_increase = 0
    for x,y,(r,g,b) in var1:
        colour_tuple = Cimpl.get_color(var2,x,y)
        if r != colour_tuple[0] or g != colour_tuple[1] or b != colour_tuple[2]:
            test_increase += 1 
            print("difference detected on the point ({},{}):".format(x,y))
            print("The pixel of the expected image:({},{},{}) vs. pixel of the outcome image:({},{},{}))".format(r,g,b,colour_tuple[0],colour_tuple[1],colour_tuple[2]))


    if test_increase > 0:        
        print("The result of your comparison:")
        return False
    else:
        print("The result of your comparison:")
        return True

#Testing:        
green_channel()
print(check_equal(Cimpl.choose_file(),Cimpl.choose_file()))



