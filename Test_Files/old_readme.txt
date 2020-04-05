Python Image Filtering Project Version 1.0 02/04/2020

---
Contact Information

This project can be reached at:
    Phone:  613-316-7187
    E-mail: zakariaismail@cmail.carleton.ca


---
Table of Contents

    - Description
    - Installation
    - Usage
    - Credits
    - License


---
Description

    This project includes text-based UI and batch file-based UI
    programs that consecutively filter images based on a series of
    commands using the Python programming language and the Cimpl
    library, written by Donald Bailey at Carleton University, which
    utilizes Pillow for the image processing and Tkinter for displaying images.

    This project consists of the following files:
    - T121_interactive_ui.py
    - T121_batch_ui.py
    - T121_image_filters.py

---
Installation

    Python 3.7.4 or later must be installed.
    Built-in and external modules are used.

    External modules:
        - Pillow
        - Cimpl

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

        - Once the download has finished, place the file in folder Python_Image_Filter

        Cimpl is now installed on your machine.


---
Installation

    To use this application, Python 3.7.4 or later, the Pillow module, and the Cimpl module
    must be installed.


    Installing Python 3

        Skip this step if you already have Python 3 installed.

        On Mac:

            - Install homebrew. To do this, open Terminal and paste into the command line:
                $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

            - The following will install Python 3. Paste into the command line:
                $ brew install python3

            Python 3 is now installed on your Mac.

        On Windows:

            - Open a web browser and paste the following link:
                https://www.python.org/downloads/windows/

            - Click on the link labelled 'Download Windows x86-64 executable installer'. This will prompt
            a .exe file download.

            - Once the download has finished, run the file and follow the steps provided by the install
            wizard.

            Python 3 is now installed on your PC.


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

        - Once the download has finished, place the file in folder Python_Image_Filter


    Installing the application files

        - Create a folder in your home directory and name it 'Python_Image_Filter'.

        - Place the Python scripts T121_image_filters.py, T121_interactive_ui.py,
        T121_batch_ui.py, and Cimpl.py in directory 'Python_Image_Filter'.


---
Usage

    To use the text-based UI:

        - Place any image (.jpg, .png) in the Python_Image_Filter folder

        - Open Terminal and type the following into the command line to run the program:
            $ cd
            $ cd Python_Image_Filter
            $ python3 T121_interactive_ui.py

        - A menu will prompt you to select an option. Input into the command line:
            : L

        This will load an image into the interface

        - Inputting the displayed letter options into the command line will allow you
        to apply the corresponding filter into the image. An image with the
        corresponding filter will be displayed shortly after.

        Certain filters, such as Edge Detect and Improved Edge Detect will prompt
        you to enter an integer before applying the filter.

        - Close the displayed image to return to the menu.

        - To exit the program, when prompted by the menu, input:
            : Q


    To use the batch file-based UI:

        - Place any image (.jpg, .png) in the Python_Image_Filter folder

        - Create a .txt file titled 'batch_sample.txt' and save it in the
        Python_Image_Filter directory.

        - To create an image filter command, enter in a newline the filename of an
        image file (.png, .jpg) inside of the same directory as T121_batch_ui.py,
        the filename to save the produced result (.png, .jpg), and then a series
        of letter commands, each separated by a space.

        - Open batch_sample.txt and enter, in a newline, the filename of an image
        file (.png, .jpg) located in directory Python_Image_Filter, a filename to
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
        contrast, a vertical flip, and a posterize filter, consecutively.

        - Open Terminal and type the following to run the batch UI program:
            $ python3 T121_batch_ui.py

        You will be prompted to enter the filename of the .txt file from which the
        program will get its commands. Input:
            : batch_sample.txt

        One or more image files should appear in your directory shortly after.

        - Edit batch_sample.txt by adding new lines of commands or changing existing
        ones to produce different results.


---
Credits



---
License

    Copyright 2020

