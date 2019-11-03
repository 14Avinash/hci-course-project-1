#! /usr/bin/env python3

# Written By: Brianna Blain-Castelli and Nikkolas Irwin
# Date: 10/23/2019
# File: main.py
# Purpose: The driver module for PyBank, our interactive GUI-based desktop client banking application.
# Description: Contains the main program logic to run our program until the user exits.

import sys

# Imports used with the pyqt5_training package
# import pyqt5_training.window as window_simple
# import pyqt5_training.label as window_with_labels
# import pyqt5_training.button as window_with_buttons
# import pyqt5_training.lineedit as window_with_line_edits
import pyqt5_training.image as window_with_image
import PyQt5.QtWidgets as qt_widgets


def main():
    # Create the PyQt5 application
    app = qt_widgets.QApplication(sys.argv)
    # Create an instance of the main application window
    win = window_with_image.Window()
    # Exit the application
    sys.exit(app.exec_())


try:  # Run the program only if this module is set properly by the interpreter as the entry point of our program.
    if __name__ == '__main__':
        print('No exceptions were raised.')
    else:  # If this module is imported raise/throw an ImportError.
        raise ImportError
except ImportError:  # If an ImportError is thrown exit the program attempting to import main.py prematurely.
    sys.exit('Import Error: main.py must be run directly, not imported.')
except Exception as err:  # Print any other exception that causes the program to not start successfully.
    print(err)
else:  # Call the main function if no exceptions were raised
    print('Starting the program.')
    main()
    print('Exiting the program.')
