#! /usr/bin/env python3

# Written By: Brianna Blain-Castelli and Nikkolas Irwin
# Date: 10/23/2019
# File: training.py
# Purpose: A module that allows PyQt5 widgets to be individually tested and understood.
# Description: Contains the main program logic to run individual widgets (based on which import statement is
# uncommented) and displays them in an interactive GUI window.

import sys

# Imports used with the pyqt5_training package
# import pyqt5_training.window as window_simple
# import pyqt5_training.label as window_with_labels
# import pyqt5_training.button as window_with_buttons
# import pyqt5_training.line_edit as window_with_line_edits
# import pyqt5_training.image as window_with_image
# import pyqt5_training.check_box as window_with_check_boxes
# import pyqt5_training.combo_box as window_with_combo_boxes
# import pyqt5_training.radio_button as window_with_radio_buttons
# import pyqt5_training.message_box as window_with_message_box
# import pyqt5_training.spin_box as window_with_spin_box
# import pyqt5_training.text_editor as window_with_text_editor
# import pyqt5_training.timer as window_with_timer
import pyqt5_training.list as window_with_list
import PyQt5.QtWidgets as qt_widgets


def main():
    # Create the PyQt5 application
    app = qt_widgets.QApplication(sys.argv)

    # Create an instance of the main application window
    win = window_with_list.Window()
    # win.start()  # when uncommented, starts the timer automatically

    # Exit the application
    sys.exit(app.exec_())


try:  # Run the program only if this module is set properly by the interpreter as the entry point of our program.
    if __name__ == '__main__':
        print('No exceptions were raised...starting the program.')
    else:  # If this module is imported raise/throw an ImportError.
        raise ImportError
except ImportError:  # If an ImportError is thrown exit the program attempting to import training.py prematurely.
    sys.exit('Import Error: training.py must be run directly, not imported.')
except Exception as err:  # Print any other exception that causes the program to not start successfully.
    print(err)
else:  # Call the main function if no exceptions were raised
    main()
