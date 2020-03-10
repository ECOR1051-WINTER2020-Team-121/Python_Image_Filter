from Cimpl import *




"""
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

def redchannel(FILENAME):
    image = load_image(FILENAME)
    newimage = copy(image)
    for x, y, (r, g, b) in image:
        red = create_color(r, 0, 0)
        set_color (newimage, x, y, red)
    show(newimage)
    return newimage

FILENAME = "riveter.jpg"

original = load_image(FILENAME)
redchannel(FILENAME)
show(original)