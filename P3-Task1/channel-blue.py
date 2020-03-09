from Cimpl import *
# Assumption: There is an image stored in the same folder as
# this script with the given name
FILENAME = "p2-original,png.png"
original_image = load_image(FILENAME)

def blue_channel(orig_image):
    """yanglongliu
    returns a new image which cannels of pixel expect for blue have been set to 0
    """
    blue_channel_image = copy(orig_image)
    for pi in orig_image:
        x,y,(r,g,b)=pi
        new_image_color = create_color(0,0,b)
        set_color(blue_channel_image,x,y,new_image_color)
    return blue_channel_image

    
new_image = blue_channel(original_image)
show(new_image)
show( original_image )
