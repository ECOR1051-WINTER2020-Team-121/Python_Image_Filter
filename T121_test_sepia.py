import Cimpl
import simple_Cimpl_filters
def test_sepia(outcome:Cimpl.Image,original_image:Cimpl.Image)-> bool:
    
    expected = simple_Cimpl_filters.grayscale(original_image) 
    var1 = Cimpl.get_color(expected,1,1)
    if var1[0] < 63:
        dark_gray = Cimpl.create_color(var1[0] * 1.1,var1[1],var1[2]* 0.9)
        pixel_expected = dark_gray
    elif var1[0] >= 63 and var1[0] <= 191:
        medium_gray = Cimpl.create_color(var1[0] * 1.15,var1[1],var1[2]* 0.85) 
        pixel_expected = medium_gray
    elif var1[0] > 191:
        light_gray = Cimpl.create_color(var1[0] * 1.08,var1[1],var1[2]* 0.93)       
        pixel_expected = light_gray
    
    test_increase = 0    
    for x,y,(r,g,b) in outcome:
        
        if r != pixel_expected[0] and g != pixel_expected[1] and b != pixel_expected[2]:
            print("difference detected at the point ({},{}):".format(x,y))
            print("expected image's pixel:({},{},{}) vs. the outcome image's pixel ({},{},{})".format(pixel_expected[0],pixel_expected[1],pixel_expected[2],r,g,b))

            test_increase += 1 
    if test_increase > 0:
        print("The test is failed,your comparison returned:")
        return False
    else:
        print("The test is passed,your comparison returned:")
        return True


outcome = Cimpl.load_image(Cimpl.choose_file())
original_image = Cimpl.load_image(Cimpl.choose_file())
print(test_sepia(outcome,original_image)) 
            