import Cimpl

def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a
    "fail" message.

    Parameter description should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.

    Parameters outcome and expected are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal.
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:

        # The format method is explained on pages 119-122 of
        # 'Practical Programming', 3rd ed.

        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '),
                     outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")
    
def test_flip_horizontal():
    '''
    A test function for flip_horizontal.
    Author: Himanshu Singh
    
    >>> test_flip_horizontal()
    Checking pixel @(0, 0) PASSED
    
    checks if flip_horizontal correctly transforms:
    # (50, 100, 200) to (3, 2, 1)  # center pixels flipped
    #(0, 0, 0) to (255, 255, 255) # top pixel flipped to lower pixel
    # (255, 255, 255)to (0, 0, 0)  # lower pixel flipped to top pixel
    # (3, 2, 1) to (50, 100, 200)  # center pixels flipped 

    '''
  
    #create image with 4 vertical pixels
    original = Cimpl.create_image(1, 4)
    Cimpl.set_color(original, 0, 0,  Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(original, 0, 1,  Cimpl.create_color(3, 2, 1))
    Cimpl.set_color(original, 0, 2,  Cimpl.create_color(50, 100, 200))
    Cimpl.set_color(original, 0, 3,  Cimpl.create_color(255, 255, 255))
    
    #create image identical image to the return image of an actual 
    #horizontal flip function.
    
    expected = Cimpl.create_image(1, 4)
    Cimpl.set_color(expected, 0, 0,  Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 0, 1,  Cimpl.create_color(50, 100, 200))
    Cimpl.set_color(expected, 0, 2,  Cimpl.create_color(3, 2, 1))
    Cimpl.set_color(expected, 0, 3,  Cimpl.create_color(0, 0, 0))
       
    #now compare the two images.
    
    flip_horizontal_image = flip_horizontal(original)   
    for x, y, col in flip_horizontal_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, Cimpl.get_color(expected, x, y))    
        
def flip_horizontal(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail
    RETURNS a Cimpl.Image
    that was flipped, after
    being PASSED a Cimpl.Image object

    >>> flip_horizontal(Cimpl.load_image('filename'))
    returns horizontally flipped image
    """
    hgt = Cimpl.get_height(img)
    
    wth = Cimpl.get_width(img)
    
    mid_x = wth // 2
    
    copy = Cimpl.copy(img)
    
    for y in range(hgt):
        
        for x in range(mid_x):
            
            r1, g1, b1 = Cimpl.get_color(img, x, y)
            r2, g2, b2 = Cimpl.get_color(img, x, hgt-y)
            
            change = wth-x-1
            
            Cimpl.set_color(copy, x, y, Cimpl.get_color(img, change, y))
            Cimpl.set_color(copy, change, y, Cimpl.get_color(img, x, y))
            
    return copy    


def posterize(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Zakaria Ismail
    RETURNS an image where
    img has its RGB channels
    set to the midpoint of quadrants:
        0..63, 64..127, 128..191, and 192..255
    depending on where the color channel value is situated between

    img is a Cimpl.Image object passed to the function

    >>>posterize(Cimpl.load_image("image.jpg"))
    returns image with posterize filter
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
    ranges = [63, 127, 191, 255]
    mid = [31, 95, 159, 223]
    for i in range(len(ranges)):
        if num <= ranges[i]:
            return mid[i]


def test_posterize():
    """
    This test_function tests the posterize() function.
    
    >>>test_posterize()
    checking pixel @(x,y) FAILED/PASSED
    
    """
    # testing all three channels at the same time for each case as it would be
    # easier and less tedious as opposed to replicating each combination which would
    # be unnessessary and a waste of time.
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
        check_equal(Cimpl.get_color(expected, x, y), Cimpl.get_color(posterized, x, y))
        check_equal(Cimpl.get_color(normal, x, y), Cimpl.get_color(posterized, x, y))
        

posterize(Cimpl.load_image("miss_sullivan.jpg"))
test_posterize()
test_flip_horizontal()
flip_horizontal(Cimpl.load_image("miss_sullivan.jpg"))