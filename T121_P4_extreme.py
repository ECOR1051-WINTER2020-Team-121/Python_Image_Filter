import Cimpl


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
    Cimpl.save_as(new_image, "outcome_extreme.png")
    Cimpl.show(new_image)


test_image = Cimpl.load_image(Cimpl.choose_file())
extreme_channel(test_image)


