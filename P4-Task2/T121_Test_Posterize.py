import Cimpl


def posterize(img: Cimpl.Image) -> Cimpl.Image:
    """
    RETURNS an image where
    img has its RGB channels
    set to the midpoint of quadrants:
        0..63, 64..127, 128..191, and 192..255
    depending on where the color channel value is situated between

    img is a Cimpl.Image object passed to the function

    (How do I write the examples?)
    """
    img = Cimpl.copy(img)
    for x, y, col in img:
        channels = []
        for ch in col:
            channels += [__adjust_component__(ch)]
        Cimpl.set_color(img, x, y, Cimpl.create_color(channels[0], channels[1], channels[1]))
    Cimpl.show(img)
    return img


def __adjust_component__(num: int) -> int:


    """
    RETURNS the midpoint of
    one of the following ranges,
    after being PASSED.
    """
    ranges = [63,127,191,255]
    mid = [31, 95, 159, 223]
    for i in range(len(ranges)):
        if num <= ranges[i]:
            return mid[i]
        
        



def test_posterize():
    
    #testing all three channels at the same time for each case as it would be 
    #easier and less tedious as opposed to replicating each combination which would
    #be unnessessary and a waste of time.
    normal = Cimpl.create_image(12, 1)
    
    Cimpl.set_color(normal, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(normal, 1, 0, Cimpl.create_color(1, 1, 1))
    Cimpl.set_color(normal, 2, 0, Cimpl.create_color(63, 63, 63))
    Cimpl.set_color(normal, 3, 0, Cimpl.create_color(64, 64, 64))
    Cimpl.set_color(normal, 4, 0, Cimpl.create_color(65, 65, 65))
    Cimpl.set_color(normal, 5, 0, Cimpl.create_color(127, 127, 127))
    Cimpl.set_color(normal, 6, 0, Cimpl.create_color(128, 128, 128))
    Cimpl.set_color(normal, 7, 0, Cimpl.create_color(129, 129, 129))
    Cimpl.set_color(normal, 8, 0, Cimpl.create_color(191, 191, 191))
    Cimpl.set_color(normal, 9, 0, Cimpl.create_color(192, 192, 192))
    Cimpl.set_color(normal, 10, 0, Cimpl.create_color(193, 193, 193))
    Cimpl.set_color(normal, 11, 0, Cimpl.create_color(255, 255, 255))
    
    
    expected = Cimpl.create_image(12, 1)
    
    Cimpl.set_color(expected, 0, 0, Cimpl.create_color(31, 31, 31))
    Cimpl.set_color(expected, 1, 0, Cimpl.create_color(31, 31, 31))
    Cimpl.set_color(expected, 2, 0, Cimpl.create_color(31, 31, 31))
    Cimpl.set_color(expected, 3, 0, Cimpl.create_color(95, 95, 95))
    Cimpl.set_color(expected, 4, 0, Cimpl.create_color(95, 95, 95))
    Cimpl.set_color(expected, 5, 0, Cimpl.create_color(95, 95, 95))
    Cimpl.set_color(expected, 6, 0, Cimpl.create_color(159, 159, 159))
    Cimpl.set_color(expected, 7, 0, Cimpl.create_color(159, 159, 159))
    Cimpl.set_color(expected, 8, 0, Cimpl.create_color(159, 159, 159))
    Cimpl.set_color(expected, 9, 0, Cimpl.create_color(223, 223, 223))
    Cimpl.set_color(expected, 10, 0, Cimpl.create_color(223, 223, 223))
    Cimpl.set_color(expected, 11, 0, Cimpl.create_color(223, 223, 223))
    
    posterized = posterize(normal)
    
    for x, y, col in posterized:
        check_equal(expected,posterized)
        check_equal(normal,posterized)

        


def check_equal(expected: Cimpl.Image, outcome: Cimpl.Image) -> Cimpl.Image:
    
    """
    AUTHOR: HIMANSHU SINGH
    check_equal(expected:Cimpl.Image,outcome:Cimpl.Image) -> Bool:
    It basically checks if the outcome image matches the pixel of the expected
    image.
    returns True if they have less than 1 error, otherwise it returns False.
    Before returning False, it prints the pixels
    and (x,y) coordinates of both images at which the images differ in pixel. 

    """
    ce_one = Cimpl.load_image(expected)
    ce_two = Cimpl.load_image(outcome)
    show(ce_one)
    show(ce_two  )


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
#print(check_equal("red_image.jpg","outcome.jpg"))

#this will print false as the orginal image is not the same as the outcome image
#as the outcome image has a red filter on it. 
#print(check_equal("p2-original.jpg","outcome.jpg"))

posterize(Cimpl.load_image("miss_sullivan.jpg"))
test_posterize()