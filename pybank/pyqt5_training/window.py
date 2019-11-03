import sys
import PyQt5.QtWidgets as qt_widgets


# Window class, inherit from QWidget
class Window(qt_widgets.QWidget):
    def __init__(self):
        # Call the base class constructor
        super().__init__()

        # Set the location for the window
        # Start window at location x = 50, location y = 50, x-resolution = 300, y-resolution = 450
        self.setGeometry(50, 50, 640, 480)

        # Set the window title
        self.setWindowTitle("This Is Our Window Title")

        # Show the window
        self.show()
