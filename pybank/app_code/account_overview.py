import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import PyQt5.QtGui as qt_gui
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget
import pybank.handlers.userhandler as user_handling
import pybank.handlers.accounthandler as account_handling
import pybank.pyqt5_global.variables as stack
import datetime

font = qt_gui.QFont('Helvetica', 28)


# Signup window class and functionality
class Window_Overview(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.credit_card_hbox = qt_widgets.QHBoxLayout()
        self.savings_hbox = qt_widgets.QHBoxLayout()
        self.checking_hbox = qt_widgets.QHBoxLayout()
        self.table_3 = qt_widgets.QTableWidget()
        self.table_2 = qt_widgets.QTableWidget()
        self.table_1 = qt_widgets.QTableWidget()
        self.tab_3 = qt_widgets.QWidget()
        self.tab_2 = qt_widgets.QWidget()
        self.tab_1 = qt_widgets.QWidget()
        self.tab_container = qt_widgets.QTabWidget()

        self.setWindowTitle('Account Overview')
        self.setProperty('Main_Window', True)
        self.setGeometry(50, 50, 1280, 720)

        # Center the window based on the properties of the desktop
        qtRectangle = qt_widgets.QWidget.frameGeometry(self)
        centerPoint = qt_widgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def user_interface(self, user_data):
        main_layout = qt_widgets.QVBoxLayout()
        username = str(user_data["username"])
        username = username.capitalize()
        self.welcome_label = qt_widgets.QLabel(f'Hello, {username}!', self)
        font.setUnderline(True)
        self.welcome_label.setFont(font)


        # Add tabs to main tab
        self.tab_container.addTab(self.tab_1, "Checking")
        self.tab_container.addTab(self.tab_2, "Savings")
        self.tab_container.addTab(self.tab_3, "Credit Card")

        self.create_checking_account_tab()

        # For testing the table
        dt = datetime.datetime.now()

        tx_id = qt_widgets.QTableWidgetItem("1")
        tx_type = qt_widgets.QTableWidgetItem("Deposit")
        tx_amt = qt_widgets.QTableWidgetItem("[+] $50.99")
        tx_cat = qt_widgets.QTableWidgetItem("ATM")
        tx_date = qt_widgets.QTableWidgetItem(str(dt.strftime("%A") + ", " + dt.strftime("%B") + " " + dt.strftime("%d") + ", " + str(dt.year)))
        tx_time = qt_widgets.QTableWidgetItem(str(dt.time().strftime('%H:%M:%S')))

        self.table_1.setItem(0, 0, tx_id)
        tx_id.setTextAlignment(qt_core.Qt.AlignCenter)

        self.table_1.setItem(0, 1, tx_type)
        tx_type.setTextAlignment(qt_core.Qt.AlignCenter)

        self.table_1.setItem(0, 2, tx_amt)
        tx_amt.setTextAlignment(qt_core.Qt.AlignCenter)

        self.table_1.setItem(0, 3, tx_cat)
        tx_cat.setTextAlignment(qt_core.Qt.AlignCenter)


        btn_1 = qt_widgets.QPushButton("Make A Deposit")
        btn_2 = qt_widgets.QPushButton("Make A Withdrawal")
        btn_3 = qt_widgets.QPushButton("Transfer Funds")
        btn_4 = qt_widgets.QPushButton("Show Graphs")
        btn_5 = qt_widgets.QPushButton("Details")

        btn_4.clicked.connect(self.display_graphs)

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

        self.table_1.setItem(0, 4, tx_date)
        tx_date.setTextAlignment(qt_core.Qt.AlignCenter)


        self.table_1.setItem(0, 5, tx_time)
        tx_time.setTextAlignment(qt_core.Qt.AlignCenter)

        # self.table_1.setItem(1, 0, qt_widgets.QTableWidgetItem("2"))
        # self.table_1.setItem(1, 1, qt_widgets.QTableWidgetItem("[-] $19.49"))
        # self.table_1.setItem(2, 0, qt_widgets.QTableWidgetItem("3"))
        # self.table_1.setItem(2, 1, qt_widgets.QTableWidgetItem("[+] $150.11"))
        # self.table_1.setItem(3, 0, qt_widgets.QTableWidgetItem("4"))
        # self.table_1.setItem(3, 1, qt_widgets.QTableWidgetItem("[-] $24.78"))

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

        main_layout.addWidget(self.tab_container)

        self.setLayout(main_layout)

        self.show()


    # Temporary functionality to reach the Graphs page. This can be adjusted.
    def display_graphs(self):
        stack.windowStack[3].user_interface()

    def create_checking_account_tab(self):
        self.table_1.setMaximumWidth(980)
        self.checking_hbox.addWidget(self.table_1)
        self.table_1.setRowCount(25)
        self.table_1.setColumnCount(6)
        self.table_1.setHorizontalHeaderItem(0, qt_widgets.QTableWidgetItem("Transaction ID"))
        self.table_1.setHorizontalHeaderItem(1, qt_widgets.QTableWidgetItem("Transaction Type"))
        self.table_1.setHorizontalHeaderItem(2, qt_widgets.QTableWidgetItem("Amount"))
        self.table_1.setHorizontalHeaderItem(3, qt_widgets.QTableWidgetItem("Category"))
        self.table_1.setHorizontalHeaderItem(4, qt_widgets.QTableWidgetItem("Date"))
        self.table_1.setHorizontalHeaderItem(5, qt_widgets.QTableWidgetItem("Time"))

        header = self.table_1.horizontalHeader()
        header.setSectionResizeMode(0, qt_widgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, qt_widgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, qt_widgets.QHeaderView.ResizeToContents)
        self.table_1.setEditTriggers(qt_widgets.QAbstractItemView.NoEditTriggers)

        btn_1 = qt_widgets.QPushButton("Make A Deposit")
        btn_2 = qt_widgets.QPushButton("Make A Withdrawal")
        btn_3 = qt_widgets.QPushButton("Transfer Funds")
        btn_4 = qt_widgets.QPushButton("Show Graphs")
        btn_5 = qt_widgets.QPushButton("Details")

        v_layout_inside_checking = qt_widgets.QVBoxLayout()
        self.checking_hbox.addLayout(v_layout_inside_checking)

        v_layout_inside_checking.addStretch()
        v_layout_inside_checking.addWidget(self.welcome_label, alignment=qt_core.Qt.AlignCenter)
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

        self.tab_1.setLayout(self.checking_hbox)

    def add_checking_account_data_from_csv(self):
        pass

    def create_savings_account_tab(self):
        pass

    def add_savings_account_data_from_csv(self):
        pass

    def create_credit_card_tab(self):
        pass

    def add_credit_card_data_from_csv(self):
        pass
