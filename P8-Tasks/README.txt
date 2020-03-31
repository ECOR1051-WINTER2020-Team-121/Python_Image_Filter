Python Image Filtering Project Version 1.0 02/04/2020

---
Table of Contents

    - Description
    - Installation
    - Usage
    - Credits
    - License
    - Contact Information

---
Description

This project includes a text-based UI and a batch file-based UI
programs that filter images based on a series of commands using
the Python programming language and the Cimpl library, written
by Donald Bailey at Carleton University, which utilize
PIL for the image processing and Tkinter for displaying images.

---
Mac Installation

Things to do:
- Install folder
    (containing T121_batch_ui.py, T121_image_filters.py, T121_interactive_ui.py, and batch_sample.txt)
- Install python 3 (MAC/Windows)
- Install pip? (Does it come with Python?)
- Install PIL, Tkinter
-

---
Usage

To use the text-based UI:

    - Open Terminal and type the following into the command line to run the program:
        python3 T121_interactive_ui.py

    - A menu will prompt you to select an option. Input 'L' into the
    command line and then select a file to load an image into the program

    - Inputting the displayed letters into the command line will allow you
    to apply the corresponding filter into the image.Ac

    Certain filters, such as Edge Detect and Improved Edge Detect will prompt
    you to enter an integer before applying the filter.

    - To exit the program, input 'Q' into the command line, when prompted by
    the menu.

To use the batch file-based UI:

    - Open text file "batch_sample.txt"

    - In a newline, type the filename of the image you wish to filter.
    Then, after placing a space, type the filename of the image you wish
    for the result of the series of image filtering to be saved. After that,
    input a series of command-letters after the two filenames, separated by
    a space each.

    The list of available command-letters are:
        X: Extreme Contrast
        S: Sepia
        P: Posterize
        E: Edge Detect
        I: Improved Edge Detect
        V: Vertical Flip
        H: Horizontal Flip



Install the folder containing Cimpl.py, T121_image_filters.py,
T121_batch_ui.py, T121_interactive_ui.py.





Contact Information

Phone:  613-316-7187
E-mail: zakariaismail@cmail.carleton.ca
