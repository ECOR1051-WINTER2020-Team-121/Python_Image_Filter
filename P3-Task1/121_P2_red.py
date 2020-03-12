from Cimpl import *

#Group: Himanshu Singh, Zakaria Ismail, Ibrahim Kasim, Yang Long Liu


"""
This is the old code
for pixel in original:
    x, y, (r, g, b) = pixel
    print (x,y,":", r,g,b)
 
newimage = copy(orginal)
def redchan(image: Cimpl.image):
    red = Cimpl.color(255,0,0)
    for newpixel in image:
        newpixel = x, y , (r, 0, 0)
        #print(x,y,":", r,g,b)
        set_color(newimage, x, y, red)
    show(newimage)
se = redchan(original)
print(se)
"""
#FILENAME = "p2-original.jpg"
FILENAME = input() #Im using input because choose_file() makes my macbook hang
#the name of the file is p2-original.jpg

def redchannel(FILENAME):
    
    """
    "Author: Himanshu Singh
    Takes in FileName as str (hardcoded) and outputs a filtered image 
    (red) using Cimpl library.j
    
    """
    image = load_image(FILENAME)
    newimage = copy(image)
    for x, y, (r, g, b) in image:
        red = create_color(r, 0, 0)
        set_color (newimage, x, y, red)
    show(newimage)
    save_as(newimage, 'outcome.jpg')                
    return newimage    
    #return newimage



def check_equal(expected, outcome):
    
    """
AUTHOR: HIMANSHU SINGH
    check_equal(expected:Cimpl.Image,outcome:Cimpl.Image) -> Bool:
    It basically checks if the outcome image matches the pixel of the expected
    image.
    returns True if they have less than 1 error, otherwise it returns False.
    Before returning False, it prints the pixels
    and (x,y) coordinates of both images at which the images differ in pixel. 

    """
    ce_one = load_image(expected)
    ce_two = load_image(outcome)
    show(ce_one)
    show(ce_two)


    errorinc = 0
    for x,y,(r,g,b) in ce_one:
        ct = get_color(ce_two,x,y)
        if r != ct[0] or g != ct[1] or b != ct[2]:
            errorinc = errorinc + 1
            print("difference dectected on point", x, "and", y)
            print("pixel on expected", r, g, b, "vs. the pixel on outcome", ct[0],
              ct[1], ct[2])
    
        if errorinc > 0:        
            print("The result:")
            return False
        else:
            print("The result:")
            return True
#this will print true because both the red variant of the original image and the
#outcome of the redchannel function will be the same picture.
print(check_equal("red_image.jpg","outcome.jpg"))

#this will print false as the orginal image is not the same as the outcome image
#as the outcome image has a red filter on it. 
print(check_equal("p2-original.jpg","outcome.jpg"))


original = load_image(FILENAME)
redchannel(FILENAME)
show(original)