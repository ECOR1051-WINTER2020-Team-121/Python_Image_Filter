
from Cimpl import *
from test_grayscale import check_equal 
from T121_P5_filter_edge import detect_edges


def test_edge():
    """author: YANGLONG LIU 101141366
    #create a image with six pixels and keep x unchanged, change y's value 
    #because we should check a pixle below one. 
    """
    original = create_image(1, 6)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 0, 1,  create_color(0, 0, 1))
    set_color(original, 0, 2,  create_color(127, 127, 127))
    set_color(original, 0, 3,  create_color(125, 73, 224))
    set_color(original, 0, 4,  create_color(254, 255, 255))
    set_color(original, 0, 5,  create_color(255, 255, 255))
    

    expected = create_image(1, 6)
    set_color(expected, 0, 0,  create_color(255,255,255)) #contrast is lower, change to white 
    set_color(expected, 0, 1,  create_color(0, 0, 0)) #contrast is lower, change to black
    set_color(expected, 0, 2,  create_color(0, 0, 0)) #contrast is lower, change to black
    set_color(expected, 0, 3,  create_color(0, 0, 0)) #contrast is lower, change to black
    set_color(expected, 0, 4,  create_color(0, 0, 0)) #contrast is lower, change to black
    set_color(expected, 0, 5,  create_color(255, 255, 255)) #the bottom row, change to white
       
    
    edge_image = detect_edges_better(original,2)   
    for x, y, col in edge_image: 
                                 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

test_edge()
          
    