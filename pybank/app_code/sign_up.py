import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import handlers.userhandler as user_handling
import handlers.accounthandler as account_handling
import pyqt5_global.variables as stack


# Signup window class and functionality
class Window_Signup(qt_widgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sign-up')
        self.setGeometry(50, 50, 500, 500)
        self.setProperty('Main_Window', True)
        self.current_widget = qt_widgets.QStackedWidget()
        self.setCentralWidget(self.current_widget)
        self.step1_widget = Widget_Signup_User(self)
        self.current_widget.addWidget(self.step1_widget)
        self.step1_widget.buttonSignup.clicked.connect(self.check_login)
        self.step1_widget.buttonSignup.installEventFilter(self)
    def check_login(self):
        self.user = self.step1_widget.check_login()
        if self.user is not None:
            self.step2_widget = Widget_Signup_Checking(self)
            self.current_widget.addWidget(self.step2_widget)
            self.current_widget.setCurrentWidget(self.step2_widget)
            self.step2_widget.buttonSignup.clicked.connect(self.signup)
    def signup(self):
        self.user = self.step2_widget.makeChecking(self.user)
        user_handling.addNewCustomer(self.user)
        if(user_handling.findChecking(self.user)):
            account_handling.createChecking(user_handling.findDir(self.user))
        stack.windowStack[2].user_interface(self.user)
        self.hide()
    def backLogin(self):
        self.hide()
        self.current_widget.setCurrentWidget(self.step1_widget)
    #Key handling functions
    def keyPressEvent(self, keyInput):
        #Exit on ESCAPE
        if keyInput.key() == qt_core.Qt.Key_Escape:
            self.close()
    def eventFilter(self, obj, event):
        if obj == self.step1_widget.buttonSignup and event.type() == qt_core.QEvent.KeyPress:
            #Attempt login on ENTER or RETURN
            keyInput = event.key()
            if keyInput == qt_core.Qt.Key_Return or keyInput == qt_core.Qt.Key_Enter:
                self.check_login()        #Call Signup page
        return False

#Signup password and username view
class Widget_Signup_User(qt_widgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.user_interface()
        self.parent = parent

    def user_interface(self):
        #Create grid
        self.layout = qt_widgets.QGridLayout()

        # Set the stretch
        self.layout.setColumnStretch(0, 3)
        self.layout.setColumnStretch(5, 3)
        self.layout.setRowStretch(0, 2)
        self.layout.setRowStretch(2, 1)
        self.layout.setRowStretch(11, 2)

        self.progress = qt_widgets.QProgressBar(self)
        self.progress.setGeometry(30, 40, 200, 25)
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.layout.addWidget(self.progress, 1, 1, 1, 3)

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

        #Confirm password
        self.textPasswordConfirm = qt_widgets.QLineEdit(self)
        self.textPasswordConfirm.setEchoMode(qt_widgets.QLineEdit.Password)
        self.labelPasswordConfirm = qt_widgets.QLabel(self)
        self.labelPasswordConfirm.setText('Confirm Password')
        self.layout.addWidget(self.labelPasswordConfirm, 7, 1)
        self.layout.addWidget(self.textPasswordConfirm, 8, 1, 1, 3)

        # #Show Password Widget
        self.buttonShowPassword = qt_widgets.QPushButton(' ', self)
        self.buttonShowPassword.setProperty('Info', True)
        self.buttonShowPassword.installEventFilter(self)
        self.layout.addWidget(self.buttonShowPassword, 6, 4, 1, 1)

        # #Add accounts using checkboxes
        # self.labelAccounts = qt_widgets.QLabel(self)
        # self.labelAccounts.setText('Select accounts to add')
        # self.checking = qt_widgets.QCheckBox('Checking', self)
        # self.savings = qt_widgets.QCheckBox('Savings', self)
        # #Upload account CSV option

        #Signup button
        self.buttonSignup = qt_widgets.QPushButton('Next', self)
        self.layout.addWidget(self.buttonSignup, 10, 1, 1, 3, qt_core.Qt.AlignRight)

        #Login option
        self.labelSignin = qt_widgets.QLabel(self)
        self.labelSignin.setText('Already have an account?')
        self.layout.addWidget(self.labelSignin, 11, 1, 1, 1)
        self.buttonLogin = qt_widgets.QLabel(self)
        self.buttonLogin.setProperty('Link', True)
        self.buttonLogin.setText('Sign-in')
        self.layout.addWidget(self.buttonLogin, 11, 3, 1, 1, qt_core.Qt.AlignCenter)
        self.buttonLogin.installEventFilter(self)

        #FOR ALIGNMENT
        self.labelAlignment2 = qt_widgets.QLabel(self)
        self.labelAlignment2.setText('Alr')
        self.labelAlignment2.setProperty('Hidden', True)
        self.layout.addWidget(self.labelAlignment2, 9, 2, 1, 2)

        self.setLayout(self.layout)

        self.show()

    def check_login(self):
        #If username entered
        if(self.textUser.text() is not "" ):
            #If password entered
            if(self.textPassword.text() is not "" ):
                #If password and confirmed password match
                if(self.textPassword.text() == self.textPasswordConfirm.text()):
                    userData = user_handling.findUser(self.textUser.text().lower())
                    #If no user with that username exists, create user
                    if(userData is None):
                        userData = {
                            'username': self.textUser.text().lower(),
                            'password': self.textPassword.text(),
                            'flags': {}
                        }
                        return userData
                    else:
                        qt_widgets.QMessageBox.warning(self, 'Error', 'Username already taken')
                else:
                    qt_widgets.QMessageBox.warning(self, 'Error', 'Passwords do not match')
            else:
                qt_widgets.QMessageBox.warning(self, 'Error', 'Please enter a password')
        else:
            qt_widgets.QMessageBox.warning(self, 'Error', 'Please enter a username')

    def eventFilter(self, obj, event):
        #Handling show password event
        if event.type() == qt_core.QEvent.KeyRelease or obj is not self.buttonShowPassword:
            self.textPassword.setEchoMode(qt_widgets.QLineEdit.Password)
            self.textPasswordConfirm.setEchoMode(qt_widgets.QLineEdit.Password)
        elif obj == self.buttonShowPassword:
            if event.type() == qt_core.QEvent.MouseButtonPress:
                self.textPassword.setEchoMode(qt_widgets.QLineEdit.Normal)
                self.textPasswordConfirm.setEchoMode(qt_widgets.QLineEdit.Normal)
            elif event.type() == qt_core.QEvent.MouseButtonRelease:
                self.textPassword.setEchoMode(qt_widgets.QLineEdit.Password)
                self.textPasswordConfirm.setEchoMode(qt_widgets.QLineEdit.Password)
            elif event.type() == qt_core.QEvent.KeyPress:
                keyInput = event.key()
                if (keyInput == qt_core.Qt.Key_Return or keyInput == qt_core.Qt.Key_Enter):
                    self.textPassword.setEchoMode(qt_widgets.QLineEdit.Normal)
                    self.textPasswordConfirm.setEchoMode(qt_widgets.QLineEdit.Normal)
                if (keyInput == qt_core.Qt.Key_Tab):
                    self.textPassword.setEchoMode(qt_widgets.QLineEdit.Password)
                    self.textPasswordConfirm.setEchoMode(qt_widgets.QLineEdit.Password)
        elif obj == self.buttonSignup:
            if event.type() == qt_core.QEvent.MouseButtonPress:
                self.hide()
                stack.windowStack[1].show()
        return False

#Signup page checking
class Widget_Signup_Checking(qt_widgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.user_interface()
        self.parent = parent

    def user_interface(self):
        #Create grid
        self.layout = qt_widgets.QGridLayout()

        # Set the stretch
        self.layout.setColumnStretch(0, 3)
        self.layout.setColumnStretch(5, 3)
        self.layout.setRowStretch(0, 2)
        self.layout.setRowStretch(2, 1)
        self.layout.setRowStretch(9, 2)

        #Progress Bar
        self.progress = qt_widgets.QProgressBar(self)
        self.progress.setGeometry(30, 40, 200, 25)
        self.progress.setRange(0, 100)
        self.progress.setValue(25)
        self.layout.addWidget(self.progress, 1, 1, 1, 3)

        #Checking Entry Group Box
        self.exclusiveGroup = qt_widgets.QGroupBox("Add Checking")
        self.layout.addWidget(self.exclusiveGroup, 3, 1, 1, 3)

        vbox = qt_widgets.QVBoxLayout()
        self.exclusiveGroup.setLayout(vbox)

        #Box items
        self.checking = qt_widgets.QCheckBox('I do not wish to add a checking account', self)
        vbox.addWidget(self.checking)
        radiobutton = qt_widgets.QRadioButton("Sync Account")
        vbox.addWidget(radiobutton)
        radiobutton = qt_widgets.QRadioButton("Add Account Manually")
        vbox.addWidget(radiobutton)


        #Signup button
        self.buttonSignup = qt_widgets.QPushButton('Signup', self)
        # self.buttonSignup.clicked.connect(self.check_login)
        self.layout.addWidget(self.buttonSignup, 8, 1, 1, 3, qt_core.Qt.AlignRight)

        #Login option
        self.labelSignin = qt_widgets.QLabel(self)
        self.labelSignin.setText('Already have an account?')
        self.layout.addWidget(self.labelSignin, 9, 1, 1, 1)
        self.buttonLogin = qt_widgets.QLabel(self)
        self.buttonLogin.setProperty('Link', True)
        self.buttonLogin.setText('Login')
        self.layout.addWidget(self.buttonLogin, 9, 3, 1, 1, qt_core.Qt.AlignCenter)
        self.buttonLogin.installEventFilter(self)

        #FOR ALIGNMENT
        self.labelAlignment2 = qt_widgets.QLabel(self)
        self.labelAlignment2.setText('Alr')
        self.labelAlignment2.setProperty('Hidden', True)
        self.layout.addWidget(self.labelAlignment2, 7, 2, 1, 2)

        self.setLayout(self.layout)

        self.show()

    def makeChecking(self, userData):
        userData['flags']['checking'] = not self.checking.isChecked()
        return userData

    def eventFilter(self, obj, event):
        if event.type() == qt_core.QEvent.MouseButtonPress:
            print(obj)
        #Call Login page
        if obj == self.buttonLogin:
            if event.type() == qt_core.QEvent.MouseButtonPress:
                self.parent.backLogin()
                stack.windowStack[0].show()
        return False
