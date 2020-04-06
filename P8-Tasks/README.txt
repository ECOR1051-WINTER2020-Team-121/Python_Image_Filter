FilterIt Version 1.0 02/04/2020

Contact Information
-------------------

    This project can be reached at:
    Phone:  613-316-7187
    E-mail: zakariaismail@cmail.carleton.ca
    Website: https://carleton.ca/sce/


Table of Contents
-----------------

    - Description
    - Installation
    - Usage
    - Credits
    - License


Description
-----------

    This project includes a text-based UI and a batch file-based UI
    Python script that consecutively filters images based on a series
    of commands.

    This project consists of the following files:
        - T121_interactive_ui.py
        - T121_batch_ui.py
        - T121_image_filters.py


Installation
------------

    Python 3.7.4 or later must be installed.
    Built-in and external modules are used.

    External modules:
        - Pillow version 7.0.0 or later
        - Cimpl version 1.04 or later

    Installing Pillow

        - Open Terminal and paste the following:
            $ pip3 install Pillow

        Pillow is now installed on your machine.

    Installing Cimpl

        - Open a web browser and go to cuLearn
            https://culearn.carleton.ca

        - Log in to the site using your credentials

        - Go to the ECOR1051 course page by clicking on its corresponding link

        - Click on the Milestone 1 tab

        - Click on the link labelled 'P1 Task 4 - A folder containing Cimpl.py
        and Approved Sample Images'. This will direct you to a new page with
        several files.

        - Click on the link labelled 'Cimpl.py'. This will prompt a download
        of the Cimpl.py file.

        Cimpl is now installed on your machine.

    Before using this project, the project's files must be placed in the same directory

        - Open Terminal and create a directory titled FilterIt in the home directory.
        Input the following into the command line:
            $ cd
            $ mkdir FilterIt

        - Place the following files inside of directory FilterIt:
            - T121_interactive_ui.py
            - T121_batch_ui.py
            - T121_image_filters.py
            - Cimpl.py

    All of the required files have been properly installed and the project is now ready for use.


Usage
-----

    To use the text-based UI:

        - Place any image (.jpg, .png) in the FilterIt folder

        - Open Terminal and type the following into the command line to run the program:
            $ cd
            $ cd FilterIt
            $ python3 T121_interactive_ui.py

        - A menu will prompt you to select an option. Input into the command line:
            : L

        This will load an image into the interface

        - Inputting the displayed letter options into the command line will allow you
        to apply the corresponding filter into the image. An image with the
        corresponding filter will be displayed shortly after.

        Edge Detect and Improved Edge Detect will prompt you to enter an integer before
        applying the filter.

        - Close the displayed image to return to the menu.

        - To exit the program, when prompted by the menu, input:
            : Q

    To use the batch file-based UI:

        - Place any image (.jpg, .png) in the FilterIt folder

        - Create a .txt file titled 'batch_sample.txt' and save it in the
        FilterIt directory.

        - To create an image filter command, enter in a newline the filename of an
        image file (.png, .jpg) inside of the same directory as T121_batch_ui.py,
        the filename to save the produced result (.png, .jpg), and then a series
        of letter commands, each separated by a space.

        - Open batch_sample.txt and enter, in a newline, the filename of an image
        file (.png, .jpg) located in directory FilterIt , a filename to
        save the produced result (.png, .jpg), and a series of letter commands, each
        separated by a space.

        The list of available command-letters are:
            2: Two-tone (Yellow and Cyan)
            3: Three-tone (Yellow, Magenta, and Cyan)
            X: Extreme Contrast
            S: Sepia
            P: Posterize
            E: Edge Detect
            I: Improved Edge Detect
            V: Vertical Flip
            H: Horizontal Flip

        Here is an example batch image filter command:
            original_image.png batch_result.png X V P

        This batch command produces an image that had been passed through an extreme
        contrast, a vertical flip, and a posterize filter, consecutively and can be found
        in the project directory under batch_result.png.

        There is no error control for improper image filenames and commands and the program
        will crash if these are inputted in the textfile.

        - Open Terminal and type the following to run the batch UI program:
            $ python3 T121_batch_ui.py

        You will be prompted to enter the filename of the .txt file from which the
        program will get its commands. Input:
            : batch_sample.txt

        One or more image files should appear in your directory shortly after.

        There is no error control for improper .txt filenames and the program will crash
        if this is inputted.

        - Edit batch_sample.txt by adding new lines of commands or changing existing
        ones to produce different results.


Credits
-------

    Image filter functions from T121_image_filters.py by author:
        Zakaria Ismail - combine, posterize, flip_horizontal
        Ibrahim Kasim - green_channel, extreme_contrast, detect_edges
        Himanshu Singh - red_channel, two_tone, three_tone, flip_vertical
        Yanglong Liu - blue_channel, sepia, detect_edges_better

    T121_interactive_ui.py - Ibrahim Kasim and Himanshu Singh

    T121_batch_ui.py - Zakaria Ismail and Yanglong Liu


License
-------

    MIT License

    Copyright (c) 2020 Zakaria Ismail

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

