
from Cimpl import *
raw_image=load_image('p2-original,png.png')

def detect_edges_better(image:Image, threshold:int)->Image:
    """
    Author:YANGLONG LIU 101141366
    returns a Image with only black and white color depending on the comparsion 
    between contrast and threshold.
    >>>improved_detect_image = detect_edges_better(raw_image, 13)
    >>>show(improved_detect_image) which returned image looks like pencil skectches.
    """
    new_image=copy(image)
    wdt=get_width(raw_image)
    hgt=get_height(raw_image)
    for x in range(wdt):
        for y in range(hgt):
            if y<hgt-1: #make a confirmation for the bottom line is not in this range
                red,green,blue=get_color(image,x,y)
                red1,green1,blue1=get_color(image,x,y+1) #the pixel below the pixel of raw image one
                red2,green2,blue2=get_color(image,x-1,y) #the right one of the pixel 
                
                brightness1=(red+blue+green)/3
                brightness2=(red1+blue1+green1)/3
                brightness3=(red2+blue2+green2)/3
                
                contrast1=abs(brightness2-brightness1)
                contrast2=abs(brightness3-brightness1) 
                
                
                if contrast1>threshold or contrast2>threshold: #make a comparsion the contrast with threshold
                    red,green,blue=0,0,0 #if the contrast is higher, change color to black.
                    black=create_color(red,green,blue)
                    set_color(new_image,x,y,black)
                
                else:
                    red,green,blue=255,255,255 #if the contrast is lower, change color to white.
                    white=create_color(red,green,blue)
                    set_color(new_image,x,y,white)
            
            
            
            elif y==hgt-1: #the bottom row of the image which the bottom line is in this range
                red,green,blue=255,255,255 #change to white simply.
                white=create_color(red,green,blue)
                set_color(new_image,x,y,white)
                
   
    return new_image





improved_detect_image=detect_edges_better(raw_image,13)

show(improved_detect_image)