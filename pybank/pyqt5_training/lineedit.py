import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        # Call the QWidget base class constructor
        super().__init__()
        # Create a QlineEdit for entering a name
        self.name_text_box = qt_widgets.QLineEdit(self)
        # Create a QlineEdit for entering a password
        self.password_text_box = qt_widgets.QLineEdit(self)
        # Set the window title
        self.setWindowTitle("Using LineEdit Widgets")
        # Set the main application window's resolution
        self.setGeometry(50, 50, 1280, 720)
        # Call the UI function to display the user interface
        self.user_interface()

    def user_interface(self):
        # Create placeholder text inside of the name text box
        self.name_text_box.setPlaceholderText('Please enter your name')
        # Resize the name text box to fit the placeholder text
        self.name_text_box.resize(175, 20)
        # Place/move the name text box to a new location
        self.name_text_box.move(150, 150)
        # Create placeholder text inside fo the password text box
        self.password_text_box.setPlaceholderText('Please enter your password')
        # Set the echo mode for the password textbox to 'Password' so it does not display as clear text output
        self.password_text_box.setEchoMode(qt_widgets.QLineEdit.Password)
        # Resize the password text box to fit the placeholder text
        self.password_text_box.resize(175, 20)
        # Place/move the password text box to a new location
        self.password_text_box.move(150, 175)
        button = qt_widgets.QPushButton('Save', self)
        button.move(260, 200)
        button.clicked.connect(self.get_values)
        # Display the user interface/main application window
        self.show()

    def get_values(self):
        name = self.name_text_box.text()
        password = self.password_text_box.text()
        print('Name:', name)
        print('Password:', password)
        self.setWindowTitle(f'Welcome {name}')
