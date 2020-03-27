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
  
    #create image
    original = Cimpl.create_image(1, 4)
    Cimpl.set_color(original, 0, 0,  Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(original, 0, 1,  Cimpl.create_color(3, 2, 1))
    Cimpl.set_color(original, 0, 2,  Cimpl.create_color(50, 100, 200))
    Cimpl.set_color(original, 0, 3,  Cimpl.create_color(255, 255, 255))
    
    
    expected = Cimpl.create_image(1, 4)
    Cimpl.set_color(expected, 0, 0,  Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 0, 1,  Cimpl.create_color(50, 100, 200))
    Cimpl.set_color(expected, 0, 2,  Cimpl.create_color(3, 2, 1))
    Cimpl.set_color(expected, 0, 3,  Cimpl.create_color(0, 0, 0))
       
    
    flip_horizontal_image = flip_horizontal(original)   
    for x, y, col in flip_horizontal_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, Cimpl.get_color(expected, x, y))    
        
def flip_horizontal(img: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Himanshu Singh
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
        
#Main 
test_flip_horizontal()
