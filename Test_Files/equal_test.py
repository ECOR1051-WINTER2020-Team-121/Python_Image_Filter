import Cimpl


def test_equal(expected: Cimpl.Image, outcome: Cimpl.Image) -> None:
    if expected == outcome:
        print("These two images are equal.")
    else:
        print("these two images SHOULD be equal, but they are apparently not.\n"
              "Therefore, using an == statement would not work on Cimpl.Image objects")


exp = Cimpl.create_image(50, 50)
out = Cimpl.create_image(50, 50)

Cimpl.show(exp)
Cimpl.show(out)

test_equal(exp, out)