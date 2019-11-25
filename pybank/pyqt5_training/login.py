import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import PyQt5.QtGui as qt_gui
import handlers.userhandler as user_handling
import globalvars.variables as stack
import pyqt5_training.account_overview as overview

#Login window class and functionality
class Window_Login(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Login')
        self.setGeometry(50, 50, 500, 500)
        self.setProperty('Main_Window', True)
        self.user_interface()

    def user_interface(self):
        #Create grid
        self.layout = qt_widgets.QGridLayout()

        # Set the stretch
        self.layout.setColumnStretch(0, 3)
        self.layout.setColumnStretch(5, 3)
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(9, 1)

        #Logo info
        self.img = qt_gui.QPixmap("assets/logo.png")
        self.labelLogo = qt_widgets.QLabel(self)
        self.labelLogo.setPixmap(self.img)
        self.layout.addWidget(self.labelLogo, 1, 1, 1, 3, qt_core.Qt.AlignCenter)
        self.labelAppName = qt_widgets.QLabel(self)
        self.labelAppName.setText('PyBank')
        self.labelAppName.setProperty('Title', True)
        self.layout.addWidget(self.labelAppName, 2, 1, 1, 3, qt_core.Qt.AlignCenter)

        #Username Entry
        self.textUser = qt_widgets.QLineEdit(self)
        self.labelUser = qt_widgets.QLabel(self)
        self.labelUser.setText('Username')
        self.layout.addWidget(self.labelUser, 3, 1)
        self.layout.addWidget(self.textUser, 4, 1, 1, 3)

        #Password Entry
        self.textPassword = qt_widgets.QLineEdit(self)
        self.textPassword.setEchoMode(qt_widgets.QLineEdit.Password)
        self.labelPassword = qt_widgets.QLabel(self)
        self.labelPassword.setText('Password')
        self.layout.addWidget(self.labelPassword, 5, 1)
        self.layout.addWidget(self.textPassword, 6, 1, 1, 3)

        #FOR ALIGNMENT
        self.labelAlignment2 = qt_widgets.QLabel(self)
        self.labelAlignment2.setText('New to Pybank?')
        self.labelAlignment2.setProperty('Hidden', True)
        self.layout.addWidget(self.labelAlignment2, 7, 3, 1, 2)

        self.buttonShowPassword = qt_widgets.QPushButton('i', self)
        self.buttonShowPassword.setProperty('Info', True)
        self.buttonShowPassword.installEventFilter(self)
        self.layout.addWidget(self.buttonShowPassword, 6, 4, 1, 1)

        #Login button
        self.buttonLogin = qt_widgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.check_login)
        self.layout.addWidget(self.buttonLogin, 8, 3, 1, 1)

        #Signup option
        self.labelSignup = qt_widgets.QLabel(self)
        self.labelSignup.setText('New to Pybank?')
        self.layout.addWidget(self.labelSignup, 9, 1, 1, 2)
        self.buttonSignup = qt_widgets.QLabel(self)
        self.buttonSignup.setProperty('Link', True)
        self.buttonSignup.setText('Sign up')
        self.layout.addWidget(self.buttonSignup, 9, 3, 1, 1, qt_core.Qt.AlignCenter)
        self.buttonSignup.installEventFilter(self)

        self.setLayout(self.layout)

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
