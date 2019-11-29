import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Button Widgets')
        self.setGeometry(50, 50, 640, 480)
        self.user_interface()

    def user_interface(self):
        # Create a label
        self.text = qt_widgets.QLabel('Press a Button', self)
        # Create an 'Enter' button
        enter_button = qt_widgets.QPushButton('Enter', self)
        # Create an 'Exit' button
        exit_button = qt_widgets.QPushButton('Exit', self)
        # Place/move widgets on the main window
        self.text.move(160, 50)
        enter_button.move(100, 80)
        exit_button.move(200, 80)

        # Create a click and connect function for the 'Enter' and 'Exit' buttons
        enter_button.clicked.connect(self.enter_func)
        exit_button.clicked.connect(self.exit_func)

        # Show the main application window
        self.show()

    def enter_func(self):
        # Set the text when the 'Enter' button is pressed
        self.text.setText('You pressed Enter')
        # Resize the label so that it can contain the full text
        self.text.resize(150, 20)

    def exit_func(self):
        # Set the text when the 'Exit' button is pressed
        self.text.setText('You pressed Exit')
        # Resize the label so that it can contain the full text
        self.text.resize(150, 20)
