import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Label Widgets')
        self.setGeometry(50, 50, 640, 480)
        self.user_interface()

    def user_interface(self):
        first_label = qt_widgets.QLabel('Hello, Python!', self)
        first_label.move(100, 50)
        second_label = qt_widgets.QLabel('Hello, World!', self)
        second_label.move(100, 150)
        third_label = qt_widgets.QLabel('Hello, Programmer!', self)
        third_label.move(100, 250)
        self.show()
