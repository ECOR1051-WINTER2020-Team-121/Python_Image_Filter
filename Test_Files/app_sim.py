
from simple_Cimpl_filters import *
import Cimpl

CHOICES = ['L', 'G', 'S', 'P', 'W', 'D', 'E', 'I', 'V', 'H', 'S', 'Q']


def menu() -> None:
    """
    RETURNS NONE. Is the menu
    interface function.
    """
    leave = False
    loaded_image = Cimpl.create_image(50, 50)
    error = 0
    while not leave:
        option = 0
        while option not in CHOICES:
            if error == 1:
                print("Command not found")
            print("Please select an option: \n"
                "\tL)oad image\tG)rayscale\tS)epia\tP)osterize\tW)oodcut\tD)eep Fried"
                  "\tE)dge detect\tI)mproved edges\tV)ert Flip\tH)oriz Flip\tS)ave image\tQ)uit\n")
            option = input("Option: ")
            error = 1
        if option == 'L':
            filename = input("Input an image filename: ")
            loaded_image = Cimpl.load_image(filename)
        elif option == 'G':
            loaded_image = grayscale(loaded_image)
        elif option == 'S':
            loaded_image = sepia(loaded_image)
        elif option == 'P':
            loaded_image = posterize(loaded_image)
        elif option == 'W':
            loaded_image = woodcut(loaded_image)
        elif option == 'D':
            loaded_image = extreme_contrast(loaded_image)
        elif option == 'E':
            thres = input("Input a threshold value: ")
            loaded_image = detect_edges(loaded_image, int(thres))
        elif option == 'I':
            thres = input("Input a threshold value: ")
            loaded_image = detect_edges_better(loaded_image, int(thres))
        elif option == 'V':
            loaded_image = flip_vertical(loaded_image)
        elif option == 'H':
            loaded_image = flip_horizontal(loaded_image)
        elif option == 'S':
            saved_name = input("Input the name that you would like to save this file as: ")
            Cimpl.save_as(loaded_image, saved_name)
        elif option == 'Q':
            leave = True
            break

        Cimpl.show(loaded_image)
        error = 0


menu()
print("Program has finished. Have a good day.")