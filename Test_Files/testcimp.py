import Cimpl

def mystery(image, a):
    new_image = Cimpl.copy(image)
    for x, y, (r, g, b) in image:
        new_color = Cimpl.create_color(r%a, g%a, b%a)
        Cimpl.set_color(new_image, x, y, new_color)
    return new_image


Cimpl.show(mystery(Cimpl.load_image('miss_sullivan.jpg'), 200))