"""
Team Identifier: 121
Contributing Members: Zakaria Ismail, Ibrahim Kasim, Himanshu Singh, Yanglong Liu
"""

import Cimpl
from T121_image_filters import *


def main() -> None:
    """
    Author: Zakaria Ismail

    RETURNS nothing. Is PASSED nothing.

    Main function containing all of
    the main components.

    >>> main()
    """
    # Things to do:
    #   - Read file line by line
    #   - Identify filenames and commands
    #       - Identify threshold value associated with E and I
    #   - Sort

    batch_filename = 'batch_sample.txt'

    file = open(batch_filename, 'r')

    for line in file:
        data = parse_linedata(line)
        image = apply_filters(data)
        save_image(image, data['save_file_as'])


def parse_linedata(linedata: str) -> dict:
    """
    Author: Zakaria Ismail

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


def apply_filters(data: dict) -> Cimpl.Image:
    """
    Author: Zakaria Ismail

    RETURNS a Cimpl.Image object and applies filters
    to an image after being PASSED data.

    data is a dict that contains information for filter sequences and saving the file

    >>> apply_filters(data)
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

    image = Cimpl.load_image(data["filename"])

    i = 0
    while i < len(data['commands']):
        if data['commands'][i] == '2':
            image = filter_functions['2'](image, 'yellow', 'cyan')
        elif data['commands'][i] == '3':
            image = filter_functions['3'](image, 'yellow', 'magenta', 'cyan')
        elif data['commands'][i] == 'E' or data['commands'][i] == 'I':
            threshold = int(data['commands'][i+1])
            image = filter_functions[data['commands'][i]](image, threshold)
            i += 1
        else:
            image = filter_functions[data['commands'][i]](image)
        i += 1
    return image


def save_image(image: Cimpl.Image, filename: str) -> None:
    """
    Author: Zakaria Ismail

    RETURNS None and saves image
    to the directory using information
    from filename

    image is a Cimpl.Image object that is going to be saved
    filename is a str that defines the image's filename when saved

    >>> save_image(Cimpl.create_image(1,1), 'filename.png')
    """
    Cimpl.save_as(image, filename)


main()
