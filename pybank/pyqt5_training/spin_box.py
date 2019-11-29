import sys
import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtGui as qt_gui

spin_box_font = qt_gui.QFont('Times', 16)


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Spin Box')
        self.setGeometry(250, 150, 500, 500)
        self.user_interface()

    def user_interface(self):
        self.spin_box = qt_widgets.QSpinBox(self)
        self.spin_box.move(150, 100)
        self.spin_box.setFont(spin_box_font)  # min value 0, max value 99 is default

        # self.spin_box.setMinimum(-1000)     # set new min value
        # self.spin_box.setMaximum(1000)      # set new max value

        self.spin_box.setRange(-10000, 10000)   # set both new min and max value
        self.spin_box.setPrefix('$')

        # self.spin_box.setSuffix(' cm')     # sets suffix unit
        # self.spin_box.setSingleStep(5)     # increase/decrease by 5
        # self.spin_box.valueChanged.connect(self.get_value)
        button = qt_widgets.QPushButton('Send', self)
        button.move(150, 140)
        button.clicked.connect(self.get_value)

        self.show()

    def get_value(self):
        value = self.spin_box.value()
        print(value)