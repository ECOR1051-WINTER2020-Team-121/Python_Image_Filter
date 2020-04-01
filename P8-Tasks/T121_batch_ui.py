"""
Team Identifier: 121
Contributing Members: Zakaria Ismail, Yanglong Liu
"""

import Cimpl
from T121_image_filters import *


def main() -> None:
    """
    Authors: Zakaria Ismail, Yanglong Liu

    RETURNS nothing.

    Main function containing all of
    the main components.

    >>> main()
    None
    """
    batch_filename = prompt_filename()

    file = open(batch_filename, 'r')

    for line in file:
        data = parse_linedata(line)
        image = apply_filters(data['filename'], data['commands'])
        save_image(image, data['save_file_as'])

    file.close()


def prompt_filename() -> str:
    """
    Authors: Zakaria Ismail, Yanglong Liu

    RETURNS a string and prompts the user
    to select a text file.

    >>> prompt_filename()
    'batch_sample.txt'
    """
    print("Select a .txt file")
    return input("Input a text file name: ")
    # return Cimpl.choose_file()


def parse_linedata(linedata: str) -> dict:
    """
    Authors: Zakaria Ismail, Yanglong Liu

    RETURNS a dict that contains
    organized information from line

    line is a str that contains text file data

    >>> parse_linedata('miss_sullivan.png batch_result.png 2 X V P')
    {"filename": "miss_sullivan.png", "save_file_as": batch_result.png", "commands": ['2', 'X', 'V', 'P']}
    """
    datalist = linedata.split()
    data = {
        "filename": datalist[0],
        "save_file_as": datalist[1],
        "commands": datalist[2:]
    }
    return data


def apply_filters(filename: str, commands: list) -> Cimpl.Image:
    """
    Authors: Zakaria Ismail, Yanglong Liu

    RETURNS a Cimpl.Image object and applies filters
    to an image after being PASSED filename and commands

    filename is a string directing to the location of the image file

    commands is a list containing the image filter sequences

    >>> apply_filters('filename.png', ['2', 'X', 'V', 'P'])
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

    image = Cimpl.load_image(filename)

    i = 0
    while i < len(commands):
        # Note: Functions that have parameters have default arguments set in T121_image_filters.py
        image = filter_functions[commands[i]](image)
        i += 1
    return image


def save_image(image: Cimpl.Image, filename: str) -> None:
    """
    Authors: Zakaria Ismail, Yanglong Liu

    RETURNS None and saves image
    to the directory using information
    from filename

    image is a Cimpl.Image object that is going to be saved

    filename is a str that defines the image's filename when saved

    >>> save_image(Cimpl.load_image(Cimpl.choose_file()), 'filename.png')
    None
    """
    Cimpl.save_as(image, filename)


main()
