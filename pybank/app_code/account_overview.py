import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import PyQt5.QtGui as qt_gui
import handlers.userhandler as user_handling
import handlers.accounthandler as account_handling
import pyqt5_global.variables as stack

font = qt_gui.QFont('Times', 20)

# Signup window class and functionality
class Window_Overview(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Account Overview')
        self.setProperty('Main_Window', True)
        self.setGeometry(50, 50, 600, 520)

    def user_interface(self, userData):
        main_layout = qt_widgets.QVBoxLayout()
        self.tab_container = qt_widgets.QTabWidget()

        self.tab_1 = qt_widgets.QWidget()
        self.tab_2 = qt_widgets.QWidget()
        self.tab_3 = qt_widgets.QWidget()

        # Add tabs to main tab
        self.tab_container.addTab(self.tab_1, "Checking")
        self.tab_container.addTab(self.tab_2, "Savings")
        self.tab_container.addTab(self.tab_3, "Credit Card")

        checking_hbox = qt_widgets.QHBoxLayout()
        savings_hbox = qt_widgets.QHBoxLayout()
        credit_card_hbox = qt_widgets.QHBoxLayout()

        self.table_1 = qt_widgets.QTableWidget()
        self.table_1.setMaximumWidth(250)
        self.table_2 = qt_widgets.QTableWidget()
        self.table_2.setMaximumWidth(250)
        self.table_3 = qt_widgets.QTableWidget()
        self.table_3.setMaximumWidth(250)

        checking_hbox.addWidget(self.table_1)
        savings_hbox.addWidget(self.table_2)
        credit_card_hbox.addWidget(self.table_3)

        self.table_1.setRowCount(20)
        self.table_1.setColumnCount(2)
        self.table_1.setHorizontalHeaderItem(0, qt_widgets.QTableWidgetItem("Transaction"))
        self.table_1.setHorizontalHeaderItem(1, qt_widgets.QTableWidgetItem("Amount"))

        self.table_2.setRowCount(20)
        self.table_2.setColumnCount(2)
        self.table_2.setHorizontalHeaderItem(0, qt_widgets.QTableWidgetItem("Transaction"))
        self.table_2.setHorizontalHeaderItem(1, qt_widgets.QTableWidgetItem("Amount"))

        self.table_3.setRowCount(20)
        self.table_3.setColumnCount(2)
        self.table_3.setHorizontalHeaderItem(0, qt_widgets.QTableWidgetItem("Transaction"))
        self.table_3.setHorizontalHeaderItem(1, qt_widgets.QTableWidgetItem("Amount"))

        welcome_label = qt_widgets.QLabel(f'Hello, {userData["username"]}!', self)
        welcome_label.setFont(font)

        btn_1 = qt_widgets.QPushButton("Make A Deposit")
        btn_2 = qt_widgets.QPushButton("Make A Withdrawal")
        btn_3 = qt_widgets.QPushButton("Transfer Funds")
        btn_4 = qt_widgets.QPushButton("Show Graphs")
        btn_5 = qt_widgets.QPushButton("Details")

        v_layout_inside_checking = qt_widgets.QVBoxLayout()
        checking_hbox.addLayout(v_layout_inside_checking)

        v_layout_inside_checking.addStretch()
        v_layout_inside_checking.addWidget(welcome_label, alignment=qt_core.Qt.AlignCenter)
        v_layout_inside_checking.addStretch()
        v_layout_inside_checking.addWidget(btn_1)
        v_layout_inside_checking.addStretch()
        v_layout_inside_checking.addWidget(btn_2)
        v_layout_inside_checking.addStretch()
        v_layout_inside_checking.addWidget(btn_3)
        v_layout_inside_checking.addStretch()
        v_layout_inside_checking.addWidget(btn_4)
        v_layout_inside_checking.addStretch()
        v_layout_inside_checking.addWidget(btn_5)
        v_layout_inside_checking.addStretch()

        # For presenation (delate later)
        self.table_1.setItem(0, 0, qt_widgets.QTableWidgetItem("1"))
        self.table_1.setItem(0, 1, qt_widgets.QTableWidgetItem("[+] $50.99"))
        self.table_1.setItem(1, 0, qt_widgets.QTableWidgetItem("2"))
        self.table_1.setItem(1, 1, qt_widgets.QTableWidgetItem("[-] $19.49"))
        self.table_1.setItem(2, 0, qt_widgets.QTableWidgetItem("3"))
        self.table_1.setItem(2, 1, qt_widgets.QTableWidgetItem("[+] $150.11"))
        self.table_1.setItem(3, 0, qt_widgets.QTableWidgetItem("4"))
        self.table_1.setItem(3, 1, qt_widgets.QTableWidgetItem("[-] $24.78"))

        print(userData)

        # # Begin Column: Checking information
        # self.labelChecking = qt_widgets.QLabel(self)
        # self.labelChecking.setText('Checking')
        # self.labelChecking.move(160, 30)
        #
        # self.labelAccountChecking = qt_widgets.QLabel(self)
        # self.buttonChecking = qt_widgets.QPushButton('Details', self)
        # if user_handling.findChecking(userData):
        #     self.labelAccountChecking.setText('Checking account found')
        #     self.labelAccountChecking.move(160, 80)
        #     self.buttonChecking.setText('Details')
        #     self.buttonChecking.move(160, 120)
        # else:
        #     self.labelAccountChecking.setText('Checking account NOT found')
        #     self.labelAccountChecking.move(160, 80)
        #     self.buttonChecking.setText('Add Account')
        #     self.buttonChecking.move(160, 120)
        #
        # # Begin Column: Savings information
        # self.labelSavings = qt_widgets.QLabel(self)
        # self.labelSavings.setText('Savings')
        # self.labelSavings.move(360, 30)
        #
        # self.labelAccountSavings = qt_widgets.QLabel(self)
        # self.buttonSavings = qt_widgets.QPushButton('Details', self)
        #
        # if user_handling.findSavings(userData):
        #     self.labelAccountSavings.setText('Savings account found')
        #     self.labelAccountSavings.move(360, 80)
        #     self.buttonSavings.setText('Details')
        #     self.buttonSavings.move(360, 120)
        # else:
        #     self.labelAccountSavings.setText('Savings account NOT found')
        #     self.labelAccountSavings.move(360, 80)
        #     self.buttonSavings.setText('Add Account')
        #     self.buttonSavings.move(360, 120)
        #
        # #Begin Column: Credit information
        # self.labelCredit = qt_widgets.QLabel(self)
        # self.labelCredit.setText('Credit')
        # self.labelCredit.move(560, 30)

        self.tab_1.setLayout(checking_hbox)
        self.tab_2.setLayout(savings_hbox)
        self.tab_3.setLayout(credit_card_hbox)

        main_layout.addWidget(self.tab_container)

        self.setLayout(main_layout)

        self.show()
