import Cimpl
import simple_Cimpl_filters
import sepia_code


def check_equal(expected, outcome):
    """
    The Author: Ibrahim Kasim
    check_equal(expected:Cimpl.Image,outcome:Cimpl.Image) -> Bool:
    Returns boolean statement. It checks if two images match. 
    """
    var1 = expected 
    var2 = outcome
    test_increase = 0
    for x,y,(r,g,b) in var1:
        colour_tuple = Cimpl.get_color(var2,x,y)
        if r != colour_tuple[0] or g != colour_tuple[1] or b != colour_tuple[2]:
            test_increase += 1 
            print("difference detected on the point ({},{}):".format(x,y))
            print("The pixel of the expected image:({},{},{}) vs. pixel of the outcome image:({},{},{}))".format(r,g,b,colour_tuple[0],colour_tuple[1],colour_tuple[2]))


    if test_increase > 0:        
        print("The result of your comparison:",False)
        
    else:
        print("The result of your comparison:",True)
        
       
def testing_sepia(original_image:Cimpl.Image,expected:Cimpl.Image)-> bool:
    """
    The author: Ibrahim Kasim
    It returns a true or false, as two object images(manually written) passed as arguments.  
    """
    check_equal(expected,sepia_code.sepia_channel(original_image))


#calling 
print("The first calling:")
expected= Cimpl.create_image(6,1)
Cimpl.set_color(expected,0,0,Cimpl.create_color(0,0,0))
Cimpl.set_color(expected,1,0,Cimpl.create_color(16,15,13))
Cimpl.set_color(expected,2,0,Cimpl.create_color(68,62,55))
Cimpl.set_color(expected,3,0,Cimpl.create_color(226,210,195))
Cimpl.set_color(expected,4,0,Cimpl.create_color(105,92,92))
Cimpl.set_color(expected,5,0,Cimpl.create_color(186,162,162))


original_image = Cimpl.create_image(6,1)
Cimpl.set_color(original_image,0,0,Cimpl.create_color(0,0,0))
Cimpl.set_color(original_image,1,0,Cimpl.create_color(1,22,22))
Cimpl.set_color(original_image,2,0,Cimpl.create_color(120,34,34))
Cimpl.set_color(original_image,3,0,Cimpl.create_color(244,177,210))
Cimpl.set_color(original_image,4,0,Cimpl.create_color(32,230,14)) 
Cimpl.set_color(original_image,5,0,Cimpl.create_color(144,144,200))

testing_sepia(original_image,expected)

print("The second calling:")

expected = Cimpl.create_image(6,1)
Cimpl.set_color(expected,0,0,Cimpl.create_color(1,1,1))
Cimpl.set_color(expected,1,0,Cimpl.create_color(1,22,22))
Cimpl.set_color(expected,2,0,Cimpl.create_color(54,43,43))
Cimpl.set_color(expected,3,0,Cimpl.create_color(13,13,13))
Cimpl.set_color(expected,4,0,Cimpl.create_color(32,230,14))
Cimpl.set_color(expected,5,0,Cimpl.create_color(144,144,200))

original_image = Cimpl.create_image(6,1)
Cimpl.set_color(original_image,0,0,Cimpl.create_color(1,1,1))
Cimpl.set_color(original_image,1,0,Cimpl.create_color(1,22,22))
Cimpl.set_color(original_image,2,0,Cimpl.create_color(4,43,43))
Cimpl.set_color(original_image,3,0,Cimpl.create_color(13,13,13))
Cimpl.set_color(original_image,4,0,Cimpl.create_color(32,230,14)) 
Cimpl.set_color(original_image,5,0,Cimpl.create_color(144,144,200))

testing_sepia(original_image,expected)
