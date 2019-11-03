import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Radio Buttons')
        self.setGeometry(250, 150, 500, 500)
        self.user_interface()

    def user_interface(self):
        self.name = qt_widgets.QLineEdit(self)
        self.name.move(150, 50)
        self.name.setPlaceholderText('Enter your name')

        self.surname = qt_widgets.QLineEdit(self)
        self.surname.move(150, 80)
        self.surname.setPlaceholderText('Enter your surname')

        self.male = qt_widgets.QRadioButton('Male', self)
        self.male.move(150, 110)
        self.male.setChecked(True)

        self.female = qt_widgets.QRadioButton('Female', self)
        self.female.move(210, 110)

        button = qt_widgets.QPushButton('Submit', self)
        button.clicked.connect(self.get_values)
        button.move(210, 140)

        self.show()

    def get_values(self):
        # Get name from QLineEdit fields
        name = self.name.text()
        surname = self.surname.text()
        # Get value of radio button
        if self.male.isChecked():
            sex = self.male.text()
            print(name, surname, sex)
        elif self.female.isChecked():
            sex = self.female.text()
            print(name, surname, sex)
