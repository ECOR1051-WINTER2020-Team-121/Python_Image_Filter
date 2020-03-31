"""
Team Identifier: 121
Contributing Members: Ibrahim Kasim, Himanshu Singh, Zakaria Ismail
"""

import Cimpl
from T121_image_filters import *


def main() -> None:
    """
    Authors: Ibrahim Kasim, Himanshu Singh, Zakaria Ismail

    RETURNS None.

    Main function where all of the
    components of the user interface
    are located.

    >>> main()
    """
    # Things the function needs
    #   1. A menu prompt asking for an input
    #       - Must not be case-sensitive
    #   2. Error catching for when:
    #       - Image is not loaded
    #       - Improper input
    #   3. Prompt for threshold value for when the user selects one of the edge detect filters
    #   4. Display the image after selecting a valid filter
    #   5. (Save_as should prompt for filename)
    exit_function = False
    is_image_loaded = False
    loaded_image = None
    while not exit_function:
        option = menu_prompt(is_image_loaded)

        # Could this be improved by implementing dict function calls? (or keep it for filters only?)
        if option == 'L':
            loaded_image = load_image()
            # Cimpl.show(loaded_image)
            is_image_loaded = True
        elif option == 'S':
            save_image(loaded_image)
        elif option == 'Q':
            exit_function = True
        else:
            loaded_image = apply_filter(loaded_image, option)
            # Cimpl.show(loaded_image)


def menu_prompt(is_image_loaded: bool) -> str:
    """
    Author: Ibrahim Kasim, Himanshu Singh, Zakaria Ismail

    RETURNS a string representing the
    selected user-input and performs outputs
    based on is_image_loaded.

    Prompts the user to provide an input.
    Errors such as non-existing inputted commands
    and selecting a filter option when there is no
    image loaded are caught.

    is_image_loaded is a Boolean telling whether an image is loaded or not

    >>> menu_prompt(True)
    """
    user_options = ['L', 'S', '2', '3', 'X', 'T', 'P', 'E', 'I', 'V', 'H', 'Q']
    is_valid_option = False
    while not is_valid_option:
        print("\nL)oad Image  S)ave as\n"
              "2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize\n"
              "E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip\n"
              "Q)uit\n")
        option = input(": ").upper()

        # Needs refactoring
        if is_image_loaded:
            if option in user_options:
                is_valid_option = True
            else:
                print("No such command")
        elif option in ['L', 'Q']:
            is_valid_option = True
        elif option in user_options:
            print("Image not loaded")
        else:
            print("No such command")

    return option


def load_image() -> Cimpl.Image:
    """
    Author: Ibrahim Kasim, Himanshu Singh, Zakaria Ismail

    RETURNS a Cimpl.Image object.

    Prompts the user to select
    an image file to load, and
    displays the loaded image

    >>> load_image()
    """
    # Cimpl.choose_file()
    filename = input("Input filename: ")
    image = Cimpl.load_image(filename)
    Cimpl.show(image)
    return image


def save_image(image: Cimpl.Image) -> None:
    """
    Author: Ibrahim Kasim, Himanshu Singh, Zakaria Ismail

    RETURNS None and prompts the user to
    select a filename to save image as

    image is a Cimpl.Image object

    >>> save_image(Cimpl.create_image(1,1))
    """
    # Observation: Why do the pictures save once the program has ended?
    filename = input("Input filename to save as: ")
    Cimpl.save_as(image, filename)
    # Cimpl.save_as(image)    # Filename and directory prompt is broken, ASK ABOUT THIS


def apply_filter(image: Cimpl.Image, command: str) -> Cimpl.Image:
    """
    Author: Ibrahim Kasim, Himanshu Singh, Zakaria Ismail

    RETURNS a Cimpl.Image object and
    applies a filter to image based on command,
    and displays the result.

    image is a Cimpl.Image object
    command is a str representing the filter to be applied

    >>> apply_filter(Cimpl.create_image(1,1), 'X')
    """
    filter_functions = {
        '2': two_tone,
        '3': three_tone,
        'X': extreme_contrast,
        'T': sepia,
        'P': posterize,
        'E': detect_edges,
        'I': detect_edges_better,
        'V': flip_vertical,
        'H': flip_horizontal,
    }

    # Could be refactored
    if command == '2':
        image = filter_functions[command](image, 'yellow', 'cyan')
    elif command == '3':
        image = filter_functions[command](image, 'yellow', 'magenta', 'cyan')
    elif command == 'E' or command == 'I':
        threshold = prompt_threshold()
        image = filter_functions[command](image, threshold)
    else:
        image = filter_functions[command](image)

    Cimpl.show(image)
    return image


def prompt_threshold() -> int:
    """
    Author: Ibrahim Kasim, Himanshu Singh, Zakaria Ismail

    RETURNS an integer.

    >>> prompt_threshold()
    """
    is_number = False

    while not is_number:
        threshold = input("Input an integer for the threshold: ")
        is_number = threshold.isnumeric()
        if not is_number:
            print("Invalid input")

    return int(threshold)


main()
print("Program has ended. Goodbye.")
