

def test_extreme_contrast() -> None:
    """
    Author:YANGLONG LIU
    extreme_contrast test function
    
    """
   
    raw = Cimpl.create_image(6, 1)

    Cimpl.set_color(raw, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(raw, 1, 0, Cimpl.create_color(1, 1, 1))
    Cimpl.set_color(raw, 2, 0, Cimpl.create_color(123, 123, 123))
    Cimpl.set_color(raw, 3, 0, Cimpl.create_color(128, 128, 128))
    Cimpl.set_color(raw, 4, 0, Cimpl.create_color(129, 129, 129))
    Cimpl.set_color(raw, 5, 0, Cimpl.create_color(255, 255, 255))

   
    expected = Cimpl.create_image(6, 1)

    Cimpl.set_color(expected, 0, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 1, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 2, 0, Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(expected, 3, 0, Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 4, 0, Cimpl.create_color(255, 255, 255))
    Cimpl.set_color(expected, 5, 0, Cimpl.create_color(255, 255, 255))

    extreme_contrasted = extreme_contrast(raw)

    for x, y, col in extreme_contrasted:
        
        check_equal('Checking pixel @({},{})'.format(x, y), col, get_color(expected, x, y))


test_extreme_contrast()






def test_edge():
    """author: YANGLONG LIU 101141366
    #create a image with six pixels and keep x unchanged, change y's value 
    #because we should check a pixle below one. 
    """
    original = Cimpl.create_image(1, 6)
    Cimpl.set_color(original, 0, 0,  Cimpl.create_color(0, 0, 0))
    Cimpl.set_color(original, 0, 1,  Cimpl.create_color(0, 0, 1))
    Cimpl.set_color(original, 0, 2,  Cimpl.create_color(127, 127, 127))
    Cimpl.set_color(original, 0, 3,  Cimpl.create_color(125, 73, 224))
    Cimpl.set_color(original, 0, 4,  Cimpl.create_color(254, 255, 255))
    Cimpl.set_color(original, 0, 5,  Cimpl.create_color(255, 255, 255))
    

    expected = create_image(1, 6)
    Cimpl.set_color(expected, 0, 0,  Cimpl.create_color(255,255,255)) #contrast is lower, change to white 
    Cimpl.set_color(expected, 0, 1,  Cimpl.create_color(0, 0, 0)) #contrast is lower, change to black
    Cimpl.set_color(expected, 0, 2,  Cimpl.create_color(0, 0, 0)) #contrast is lower, change to black
    Cimpl.set_color(expected, 0, 3,  Cimpl.create_color(0, 0, 0)) #contrast is lower, change to black
    Cimpl.set_color(expected, 0, 4,  Cimpl.create_color(0, 0, 0)) #contrast is lower, change to black
    Cimpl.set_color(expected, 0, 5,  Cimpl.create_color(255, 255, 255)) #the bottom row, change to white
       
    
    edge_image = detect_edges_better(original,2)   
    for x, y, col in edge_image: 
                                 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

test_edge()
          
