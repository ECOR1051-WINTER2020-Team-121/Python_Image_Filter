import Cimpl
import simple_Cimpl_filters
import T121_sepia
def test_sepia(outcome:Cimpl.Image,original_image:Cimpl.Image)-> bool:
    """the author: Ibrahim Kasim
    returns boolean statament, two image objects passed 
    as arguments, first one being outcome, second is the original image.

    """
    if type(outcome)!= type(original_image):
        print("images intended for comparison do not match in type:",False)
    
    
    expected = simple_Cimpl_filters.grayscale(original_image) 
    test_increase = 0 
    
    for x,y,var1 in expected:
       
        if var1[0] < 63:
            dark_gray = Cimpl.create_color(var1[0] * 1.1,var1[1],var1[2]* 0.9)
            pixel_expected = dark_gray
        elif var1[0] >= 63 and var1[0] <= 191:
            medium_gray = Cimpl.create_color(var1[0] * 1.15,var1[1],var1[2]* 0.85) 
            pixel_expected = medium_gray
        elif var1[0] > 191:
            light_gray = Cimpl.create_color(var1[0] * 1.08,var1[1],var1[2]* 0.93)       
            pixel_expected = light_gray
    
           
            pixel = Cimpl.get_color(outcome,x,y) 
        
            if pixel[0] != pixel_expected[0] or pixel[1] != pixel_expected[1] or pixel[2] != pixel_expected[2]:
                print("difference detected at the point ({},{}):".format(x,y))
                print("expected image's pixel:({},{},{}) vs. the outcome image's pixel ({},{},{})".format(pixel_expected[0],pixel_expected[1],pixel_expected[2],r,g,b))
                test_increase += 1 
    
    if test_increase > 0:
        print("The test is failed,your comparison returned:",False)
    else:
        print("The test is passed,your comparison returned:",True)
        

outcome_1 = T121_sepia.sepia_channel(Cimpl.load_image(Cimpl.choose_file()))
original_image_1 = Cimpl.load_image(Cimpl.choose_file())
test_sepia(outcome_1,original_image_1)

