#! /usr/bin/env python3

# Written By: Brianna Blain-Castelli and Nikkolas Irwin
# Date: 10/23/2019
# File: main.py
# Purpose: The driver module for PyBank, our interactive GUI-based desktop client banking application.
# Description: Contains the main program logic to run our program until the user exits.

# System libraries, QtWidgets, QSS
import sys
import PyQt5.QtWidgets as qt_widgets
import handlers.stylesheethandler as stylesheets

# PyBank specific window imports
import app_code.sign_in as window_with_login
import app_code.sign_up as window_with_signup
import app_code.account_overview as window_with_overview
import app_code.graphs as window_with_graphs

# Global variables for the window management, style management
import pyqt5_global.variables as gbl_vars


def main():
    # Create the PyQt5 application
    app = qt_widgets.QApplication(sys.argv)

    # Select StyleSheet
    stylesheets.readQSS()
    app.setStyleSheet(gbl_vars.stylesheet)

    # Create an instance of the main application window
    gbl_vars.windowStack.append(window_with_login.Window_Login())
    gbl_vars.windowStack.append(window_with_signup.Window_Signup())
    gbl_vars.windowStack.append(window_with_overview.Window_Overview())
    gbl_vars.windowStack.append(window_with_graphs.Window_Graphs())
    # win = window_with_signup.Window_Signup()
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
