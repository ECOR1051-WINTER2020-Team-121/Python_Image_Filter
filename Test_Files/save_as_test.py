import Cimpl

img = Cimpl.load_image('miss_sullivan.png')
if None:
    print("None is true")
else:
    print("None is false")
Cimpl.save_as(img)