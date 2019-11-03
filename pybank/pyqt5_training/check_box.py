import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        # Create QLineEdits
        self.name = qt_widgets.QLineEdit(self)
        self.surname = qt_widgets.QLineEdit(self)
        # Create Checkbox
        self.remember = qt_widgets.QCheckBox('Remember Me', self)
        self.setWindowTitle('Using Check Boxes')
        self.setGeometry(50, 50, 500, 500)
        self.user_interface()

    def user_interface(self):
        # Set placeholder text
        self.name.setPlaceholderText('Enter your name')
        self.surname.setPlaceholderText('Enter your surname')

        # Move QLineEdits
        self.name.move(200, 50)
        self.surname.move(200, 80)

        # Move checkbox
        self.remember.move(200, 110)

        # Create a submit button
        button = qt_widgets.QPushButton('Submit', self)
        button.move(220, 140)
        button.clicked.connect(self.submit)

        self.show()

    def submit(self):
        # Determine if the checkbox was checked and display the appropriate response to the console
        if self.remember.isChecked():
            print(f'Name: {self.name.text()}' + f'\nSurname: {self.surname.text()}', '\nRemember me was checked')
        else:
            print(f'Name: {self.name.text()}' + f'\nSurname: {self.surname.text()}', '\nRemember me was NOT checked')
