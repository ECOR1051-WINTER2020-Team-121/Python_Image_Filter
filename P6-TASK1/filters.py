def green_channel():
    """
    The Author: Ibrahim Kasim
    green_channel() -> Cimpl.Image:
    Returns green filtered image. It directs user to choose an image that 
    is desired for filtering.
    
    """
    
    image_file = Cimpl.choose_file()
    original_image = Cimpl.load_image(image_file)
    new_image = Cimpl.copy(original_image)
    for pixel in original_image:
        x,y,(r,g,b) = pixel
        green_color = Cimpl.create_color(0,g,0)
        Cimpl.set_color(new_image, x,y, green_color)
    
    return new_image
    
def extreme_channel(original_image: Cimpl.Image) -> Cimpl.Image:
    """
    The author: Ibrahim Kasim
    returns image object with extreme contrast filter apllied.
    
        >>>test_image = Cimpl.load_image(Cimpl.choose_file())
           extreme_channel(test_image)
        ...(shows orginal image in extreme contrast filter)

    """
    new_image = Cimpl.copy(original_image)
    min_pixel = 0
    max_pixel = 255
    for x, y, colour_tuple in original_image:
        i = 0
        for component in colour_tuple:
            list_colour = list(colour_tuple)
            if component <= 127:
                list_colour[i] = min_pixel
                maximized_contrast = Cimpl.create_color(list_colour[0], list_colour[1], list_colour[2])
                Cimpl.set_color(new_image, x, y, maximized_contrast)
            elif component >= 128:
                list_colour[i] = max_pixel
                maximized_contrast = Cimpl.create_color(list_colour[0], list_colour[1], list_colour[2])
                Cimpl.set_color(new_image, x, y, maximized_contrast)
            i += 1

def detect_edges(original_image: Cimpl.Image, threshold: float) -> Cimpl.Image:
    """ The author: Ibrahim Kasim
    returns a copy of the original image with edge detection filter apllied to it."""
    new_image = Cimpl.copy(original_image)
    total_width = Cimpl.get_width(original_image)
    total_height = Cimpl.get_height(original_image)
    blacked = Cimpl.create_color(0, 0, 0)
    whited = Cimpl.create_color(255, 255, 255)

    for x, y, pixels in original_image:
        if x != total_width and y != total_height - 1:
            pixel_top = Cimpl.get_color(original_image, x, y)
            pixel_bottom = Cimpl.get_color(original_image, x, y + 1)

            average_top = (pixel_top[0] + pixel_top[1] + pixel_top[2]) / 3
            average_bottom = (pixel_bottom[0] + pixel_bottom[1] + pixel_bottom[2]) / 3
            difference = abs(average_bottom - average_top)
            if x == total_width:
                Cimpl.set_color(new_image, x, y, whited)

            elif difference > threshold:
                Cimpl.set_color(new_image, x, y, blacked)
            else:
                Cimpl.set_color(new_image, x, y, whited)
