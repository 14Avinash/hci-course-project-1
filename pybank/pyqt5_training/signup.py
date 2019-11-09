import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import handlers.userhandler as user_handling
import handlers.accounthandler as account_handling
import globalvars.variables as stack

#Signup window class and functionality
class Window_Signup(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Signup')
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

        #Confirm password
        self.textPasswordConfirm = qt_widgets.QLineEdit(self)
        self.textPasswordConfirm.setEchoMode(qt_widgets.QLineEdit.Password)
        self.textPasswordConfirm.move(160, 150)
        self.labelPasswordConfirm = qt_widgets.QLabel(self)
        self.labelPasswordConfirm.setText('Confirm Password')
        self.labelPasswordConfirm.move(160, 130)

        #Show Password Widget
        self.buttonShowPassword = qt_widgets.QPushButton('i', self)
        self.buttonShowPassword.installEventFilter(self)
        self.buttonShowPassword.setGeometry(310, 100, 30, 25)

        #Add accounts using checkboxes
        self.labelAccounts = qt_widgets.QLabel(self)
        self.labelAccounts.setText('Select accounts to add')
        self.labelAccounts.move(160, 180)
        self.checking = qt_widgets.QCheckBox('Checking', self)
        self.checking.move(160, 200)
        self.savings = qt_widgets.QCheckBox('Savings', self)
        self.savings.move(160, 220)
        #Upload account CSV option

        #Signup button
        buttonSignup = qt_widgets.QPushButton('Signup', self)
        buttonSignup.clicked.connect(self.check_login)
        buttonSignup.move(190, 250)

        #Login option
        self.labelSignup = qt_widgets.QLabel(self)
        self.labelSignup.setText('Already have an account?')
        self.labelSignup.move(130, 300)
        self.buttonLogin = qt_widgets.QLabel(self)
        self.buttonLogin.setText('Login')
        self.buttonLogin.setStyleSheet("color: blue;")
        self.buttonLogin.move(305, 300)
        self.buttonLogin.installEventFilter(self)


    def eventFilter(self, obj, event):
        #Handling show password event
        if obj == self.buttonShowPassword:
            if event.type() == qt_core.QEvent.MouseButtonPress:
                self.textPassword.setEchoMode(qt_widgets.QLineEdit.Normal)
                self.textPasswordConfirm.setEchoMode(qt_widgets.QLineEdit.Normal)
            elif event.type() == qt_core.QEvent.MouseButtonRelease:
                self.textPassword.setEchoMode(qt_widgets.QLineEdit.Password)
                self.textPasswordConfirm.setEchoMode(qt_widgets.QLineEdit.Password)
        #Call Login page
        elif obj == self.buttonLogin:
            if event.type() == qt_core.QEvent.MouseButtonPress:
                self.hide()
                stack.windowStack[0].show()
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
        #If password and confirmed password match
        if(self.textPassword.text() == self.textPasswordConfirm.text()):
            userData = user_handling.findUser(self.textUser.text().lower())
            #If no user with that username exists, create user
            if(userData is None):
                userData = {
                    'username': self.textUser.text().lower(),
                    'password': self.textPassword.text(),
                    'flags': {
                        'checking': self.checking.isChecked(),
                        'savings': self.savings.isChecked()
                    }
                }
                userData = user_handling.addNewCustomer(userData)
                if(user_handling.findChecking(userData)):
                    account_handling.createChecking(user_handling.findDir(userData))
                qt_widgets.QMessageBox.warning(self, 'Success', 'Signup Successful')

            else:
                qt_widgets.QMessageBox.warning(self, 'Error', 'Username already taken')
        else:
            qt_widgets.QMessageBox.warning(self, 'Error', 'Passwords do not match')
