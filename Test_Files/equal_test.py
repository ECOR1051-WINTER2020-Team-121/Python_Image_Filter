import Cimpl


def test_equal(expected: Cimpl.Image, outcome: Cimpl.Image) -> None:
    if expected == outcome:
        print("These two images are equal.")
    else:
        print("these two images SHOULD be equal, but they are apparently not.\n"
              "Therefore, using an == statement would not work on Cimpl.Image objects")


exp = Cimpl.create_image(50, 50)
out = Cimpl.create_image(50, 50)

var = 0

while var:
    print("in loop")

print(bool(var))
print(bool(var) == False)
print(var == False)

print((var == 0) == (var == False))

print(False != 0)

boor = False
print("--last one--")
#print(boor == 0)
print(boor == False and type(boor) == bool)
print(var == False and type(var) == bool)

#Cimpl.show(exp)
#Cimpl.show(out)

#test_equal(exp, out)