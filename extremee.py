import Cimpl


def extreme_contrast(original_image: Cimpl.Image) -> Cimpl.Image:
    """
    Author: Ibrahim Kasim
    RETURNS a Cimpl.Imagee object where
    the pixel channels in original_image have
    been set to 0 or 255.

    >>> extreme_contrast(Cimpl.load_image(choose_file()))
    """
    new_image = Cimpl.copy(original_image)
    min_pixel = 0
    max_pixel = 255
    for x, y, colour_tuple in original_image:

        list_colour = []

        for component in colour_tuple:
            if component <= 127:
                list_colour += [min_pixel]
            elif component >= 128:
                list_colour += [max_pixel]

        maximized_contrast = Cimpl.create_color(list_colour[0], list_colour[1], list_colour[2])
        Cimpl.set_color(new_image, x, y, maximized_contrast)
    
    return new_image


Cimpl.show(extreme_contrast(Cimpl.load_image('miss_sullivan.png')))
    
   