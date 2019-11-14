import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import handlers.userhandler as user_handling
import globalvars.variables as stack
import pyqt5_training.account_overview as overview

#Login window class and functionality
class Window_Login(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Login')
        self.setGeometry(50, 50, 500, 500)
        self.user_interface()

    def user_interface(self):
        #Username Entry
        self.textUser = qt_widgets.QLineEdit(self)
        self.textUser.move(160, 50)
        self.labelUser = qt_widgets.QLabel(self)
        self.labelUser.setText('Username')
        self.labelUser.move(160, 30)

        #Password Entry
        self.textPassword = qt_widgets.QLineEdit(self)
        self.textPassword.setEchoMode(qt_widgets.QLineEdit.Password)
        self.textPassword.move(160, 100)
        self.labelPassword = qt_widgets.QLabel(self)
        self.labelPassword.setText('Password')
        self.labelPassword.move(160, 80)

        #Show Password Widget
        self.buttonShowPassword = qt_widgets.QPushButton('i', self)
        self.buttonShowPassword.installEventFilter(self)
        self.buttonShowPassword.setGeometry(310, 100, 30, 25)

        #Login button
        buttonLogin = qt_widgets.QPushButton('Login', self)
        buttonLogin.clicked.connect(self.check_login)
        buttonLogin.move(190, 130)

        #Signup option
        self.labelSignup = qt_widgets.QLabel(self)
        self.labelSignup.setText('New to Pybank?')
        self.labelSignup.move(150, 180)
        self.buttonSignup = qt_widgets.QLabel(self)
        self.buttonSignup.setText('Sign up')
        self.buttonSignup.setStyleSheet("color: blue;")
        self.buttonSignup.move(275, 180)
        self.buttonSignup.installEventFilter(self)

        self.show()


    def eventFilter(self, obj, event):
        #Handling show password event
        if obj == self.buttonShowPassword:
            if event.type() == qt_core.QEvent.MouseButtonPress:
                self.textPassword.setEchoMode(qt_widgets.QLineEdit.Normal)
            elif event.type() == qt_core.QEvent.MouseButtonRelease:
                self.textPassword.setEchoMode(qt_widgets.QLineEdit.Password)
        #Call Signup page
        elif obj == self.buttonSignup:
            if event.type() == qt_core.QEvent.MouseButtonPress:
                self.hide()
                stack.windowStack[1].show()
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
                self.hide()
                stack.windowStack[2].user_interface(userData)
            else:
                qt_widgets.QMessageBox.warning(self, 'Error', 'Incorrect password')
        else:
            qt_widgets.QMessageBox.warning(self, 'Error', 'User does not exist')
