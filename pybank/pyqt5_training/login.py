import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import json_functionality.json_read as user_handling

#Login window class and functionality
class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Login')
        self.setGeometry(50, 50, 500, 500)
        self.user_interface()

    def user_interface(self):
        #Username and password entry
        self.textUser = qt_widgets.QLineEdit(self)
        self.textUser.move(160, 50)
        self.textPassword = qt_widgets.QLineEdit(self)
        self.textPassword.setEchoMode(qt_widgets.QLineEdit.Password)
        self.textPassword.move(160, 80)

        #Show Password Widget
        buttonShowPassword = qt_widgets.QPushButton('i', self)
        buttonShowPassword.installEventFilter(self)
        buttonShowPassword.setGeometry(310, 80, 30, 25)

        #Login button
        buttonLogin = qt_widgets.QPushButton('Login', self)
        buttonLogin.clicked.connect(self.check_login)
        buttonLogin.move(190, 110)

        self.show()

    #Handling show password event
    def eventFilter(self, obj, event):
        if event.type() == qt_core.QEvent.MouseButtonPress:
            self.textPassword.setEchoMode(qt_widgets.QLineEdit.Normal)
        elif event.type() == qt_core.QEvent.MouseButtonRelease:
            self.textPassword.setEchoMode(qt_widgets.QLineEdit.Password)
        return False

    #Key handling functions
    def keyPressEvent(self, keyInput):
        #Attempt login on ENTER or RETURN
        if keyInput.key() == qt_core.Qt.Key_Return or keyInput.key() == qt_core.Qt.Key_Enter:
            self.check_login()
        #Exit on ESCAPE
        if keyInput.key() == qt_core.Qt.Key_Escape:
            self.close()

    def check_login(self):
        userData = user_handling.findUser(self.textUser.text().lower())
        if(userData is not None):
            if(self.textPassword.text() == user_handling.findPassword(userData)):
                qt_widgets.QMessageBox.warning(self, 'Success', 'Login Successful')
            else:
                qt_widgets.QMessageBox.warning(self, 'Error', 'Incorrect password')
        else:
            qt_widgets.QMessageBox.warning(self, 'Error', 'User does not exist')
