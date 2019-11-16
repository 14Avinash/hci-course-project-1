import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import handlers.userhandler as user_handling
import handlers.accounthandler as account_handling
import globalvars.variables as stack

#Signup window class and functionality
class Window_Overview(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Overview')
        self.setProperty('Main_Window', True)
        self.setGeometry(50, 50, 1000, 500)

    def user_interface(self, userData):
        #Begin Column: Checking information
        self.labelChecking = qt_widgets.QLabel(self)
        self.labelChecking.setText('Checking')
        self.labelChecking.move(160, 30)

        self.labelAccountChecking = qt_widgets.QLabel(self)
        self.buttonChecking = qt_widgets.QPushButton('Details', self)
        if(user_handling.findChecking(userData)):
            self.labelAccountChecking.setText('Checking account found')
            self.labelAccountChecking.move(160, 80)
            self.buttonChecking.setText('Details')
            self.buttonChecking.move(160, 120)
        else:
            self.labelAccountChecking.setText('Checking account NOT found')
            self.labelAccountChecking.move(160, 80)
            self.buttonChecking.setText('Add Account')
            self.buttonChecking.move(160, 120)

        #Begin Column: Savings information
        self.labelSavings = qt_widgets.QLabel(self)
        self.labelSavings.setText('Savings')
        self.labelSavings.move(360, 30)

        self.labelAccountSavings = qt_widgets.QLabel(self)
        self.buttonSavings = qt_widgets.QPushButton('Details', self)
        if(user_handling.findSavings(userData)):
            self.labelAccountSavings.setText('Savings account found')
            self.labelAccountSavings.move(360, 80)
            self.buttonSavings.setText('Details')
            self.buttonSavings.move(360, 120)
        else:
            self.labelAccountSavings.setText('Savings account NOT found')
            self.labelAccountSavings.move(360, 80)
            self.buttonSavings.setText('Add Account')
            self.buttonSavings.move(360, 120)

        #Begin Column: Credit information
        self.labelCredit = qt_widgets.QLabel(self)
        self.labelCredit.setText('Credit')
        self.labelCredit.move(560, 30)
        self.show()
