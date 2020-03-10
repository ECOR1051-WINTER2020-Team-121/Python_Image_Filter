from Cimpl import *

FILENAME = "p2-original,png.png"
raw_image = load_image(FILENAME)

def blue_channel(raw_image):
    """yanglongliu
    returns a blue channel only copy image, which each pixel only have blue item
    """
    blue_channel_image = copy(raw_image)
    for pi in raw_image:
        x,y,(r,g,b)=pi
        new_image_color = create_color(0,0,b)
        set_color(blue_channel_image,x,y,new_image_color)
    return blue_channel_image

    
new_image = blue_channel(raw_image)
show(new_image)
show( raw_image )

def equal_text_blue()->str:
    """return pass of fail if all of the pixel expect for blue is 0
    """
    image =load_image(FILENAME)
    blue1=blue_channel(raw_image)
    check = 0
    for pi in blue1:
        x,y,(r,g,b) = pi
        if g and r !=0:
            check+=1
    else:
        check=check
    if check ==0:
        print('passed')
    else:
        print('failed')
    return blue1
print(equal_text_blue())
    


