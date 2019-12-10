# PyQt5 Imports
import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import PyQt5.QtGui as qt_gui

# Account-based imports
import handlers.userhandler as user_handling
import handlers.accounthandler as account_handling
import pyqt5_global.variables as stack
import app_code.nav_menu as nav_menu

# Python standard library imports
import datetime
import csv

welcome_label_font = qt_gui.QFont('Helvetica', 28)


# Account overview class  *********************************************************************************************
class Window_Overview(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.chk_tx_number = 1
        self.svg_tx_number = 1
        self.crd_tx_number = 1
        self.nav_h_layout = qt_widgets.QHBoxLayout()
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

    # Account overview interface  *************************************************************************************
    def user_interface(self, user_data):
        # Create the main layout
        main_layout = qt_widgets.QVBoxLayout()

        # Create the navigation menu layout
        self.nav_h_layout.addWidget(nav_menu.Window())
        self.nav_h_layout.setContentsMargins(1, 0, 0, 0)
        self.nav_h_layout.setSpacing(0)

        # Add tabs to the tab layout
        self.tab_container.addTab(self.tab_1, "Checking")
        self.tab_container.addTab(self.tab_2, "Savings")
        self.tab_container.addTab(self.tab_3, "Credit Card")

        # Create the checking account tab widgets
        self.create_checking_account_tab(user_data)
        self.create_savings_account_tab(user_data)
        self.create_credit_card_tab(user_data)

        # Add the navigation menu and tabs to the main layout
        main_layout.addLayout(self.nav_h_layout)
        main_layout.addWidget(self.tab_container)

        # Set and show the main layout for the account overview
        self.setLayout(main_layout)
        self.show()

    # Checking account operations *************************************************************************************
    def create_checking_account_tab(self, user_data):
        # Store the username and capitalize the first letter.
        self.username = str(user_data["username"])

        # Create a label to greet the user based on their username when viewing the checking account tab.
        welcome_label_checking = qt_widgets.QLabel(f'Hello, {self.username}!', self)

        # Underline and set the font for the welcome label.
        welcome_label_font.setUnderline(True)
        welcome_label_checking.setFont(welcome_label_font)

        # Set the dimensions of the table.
        self.table_1.setMaximumWidth(940)
        self.table_1.setMinimumHeight(620)
        self.table_1.setMaximumHeight(620)
        self.checking_hbox.addWidget(self.table_1)
        self.table_1.setRowCount(25)
        self.table_1.setColumnCount(6)

        # Set the table headers.
        self.table_1.setHorizontalHeaderItem(0, qt_widgets.QTableWidgetItem("Transaction ID"))
        self.table_1.setHorizontalHeaderItem(1, qt_widgets.QTableWidgetItem("Transaction Type"))
        self.table_1.setHorizontalHeaderItem(2, qt_widgets.QTableWidgetItem("Amount"))
        self.table_1.setHorizontalHeaderItem(3, qt_widgets.QTableWidgetItem("Category"))
        self.table_1.setHorizontalHeaderItem(4, qt_widgets.QTableWidgetItem("Date"))
        self.table_1.setHorizontalHeaderItem(5, qt_widgets.QTableWidgetItem("Time"))

        # Set the columns for the table.
        header = self.table_1.horizontalHeader()
        header.setSectionResizeMode(0, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, qt_widgets.QHeaderView.Stretch)
        self.table_1.setEditTriggers(qt_widgets.QAbstractItemView.NoEditTriggers)
        self.table_1.verticalHeader().setVisible(False)

        # Checking account buttons.
        btn_1 = qt_widgets.QPushButton("Make A Deposit")
        btn_2 = qt_widgets.QPushButton("Make A Withdrawal")
        btn_3 = qt_widgets.QPushButton("Transfer Funds")
        btn_4 = qt_widgets.QPushButton("Show Graphs")
        btn_5 = qt_widgets.QPushButton("More Details")

        # Create a new layout inside checking for the buttons
        v_layout_inside_checking = qt_widgets.QVBoxLayout()
        self.checking_hbox.addLayout(v_layout_inside_checking)

        # Add the buttons to the layout and set their lengths.
        v_layout_inside_checking.addStretch()
        v_layout_inside_checking.addWidget(welcome_label_checking, alignment=qt_core.Qt.AlignCenter)
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

        # Connect buttons to handlers
        btn_1.clicked.connect(self.make_deposit_handler)
        btn_2.clicked.connect(self.make_withdrawal_handler)
        btn_3.clicked.connect(self.transfer_funds_handler)
        btn_4.clicked.connect(self.show_graphs)
        btn_5.clicked.connect(self.details_handler)

        # Add the checking account internal layout to the checking account horizontal layout
        self.tab_1.setLayout(self.checking_hbox)

    # Savings account operations **************************************************************************************
    def create_savings_account_tab(self, user_data):
        # Store the username and capitalize the first letter.
        self.username = str(user_data["username"])

        # Create a label to greet the user based on their username when viewing the checking account tab.
        welcome_label_savings = qt_widgets.QLabel(f'Hello, {self.username}!', self)

        # Underline and set the font for the welcome label.
        welcome_label_font.setUnderline(True)
        welcome_label_savings.setFont(welcome_label_font)

        # Set the dimensions of the table.
        self.table_2.setMaximumWidth(940)
        self.table_2.setMinimumHeight(620)
        self.table_2.setMaximumHeight(620)
        self.savings_hbox.addWidget(self.table_2)
        self.table_2.setRowCount(25)
        self.table_2.setColumnCount(6)

        # Set the table headers.
        self.table_2.setHorizontalHeaderItem(0, qt_widgets.QTableWidgetItem("Transaction ID"))
        self.table_2.setHorizontalHeaderItem(1, qt_widgets.QTableWidgetItem("Transaction Type"))
        self.table_2.setHorizontalHeaderItem(2, qt_widgets.QTableWidgetItem("Amount"))
        self.table_2.setHorizontalHeaderItem(3, qt_widgets.QTableWidgetItem("Category"))
        self.table_2.setHorizontalHeaderItem(4, qt_widgets.QTableWidgetItem("Date"))
        self.table_2.setHorizontalHeaderItem(5, qt_widgets.QTableWidgetItem("Time"))

        # Set the columns for the table.
        header = self.table_2.horizontalHeader()
        header.setSectionResizeMode(0, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, qt_widgets.QHeaderView.Stretch)
        self.table_2.setEditTriggers(qt_widgets.QAbstractItemView.NoEditTriggers)
        self.table_2.verticalHeader().setVisible(False)

        # Checking account buttons.
        btn_1 = qt_widgets.QPushButton("Make A Deposit")
        btn_2 = qt_widgets.QPushButton("Make A Withdrawal")
        btn_3 = qt_widgets.QPushButton("Transfer Funds")
        btn_4 = qt_widgets.QPushButton("Show Graphs")
        btn_5 = qt_widgets.QPushButton("More Details")

        # Create a new layout inside checking for the buttons
        v_layout_inside_savings = qt_widgets.QVBoxLayout()
        self.savings_hbox.addLayout(v_layout_inside_savings)

        # Add the buttons to the layout and set their lengths.
        v_layout_inside_savings.addStretch()
        v_layout_inside_savings.addWidget(welcome_label_savings, alignment=qt_core.Qt.AlignCenter)
        v_layout_inside_savings.addStretch()
        v_layout_inside_savings.addWidget(btn_1)
        v_layout_inside_savings.addStretch()
        v_layout_inside_savings.addWidget(btn_2)
        v_layout_inside_savings.addStretch()
        v_layout_inside_savings.addWidget(btn_3)
        v_layout_inside_savings.addStretch()
        v_layout_inside_savings.addWidget(btn_4)
        v_layout_inside_savings.addStretch()
        v_layout_inside_savings.addWidget(btn_5)
        v_layout_inside_savings.addStretch()

        # Connect buttons to handlers
        btn_1.clicked.connect(self.make_deposit_handler)
        btn_2.clicked.connect(self.make_withdrawal_handler)
        btn_3.clicked.connect(self.transfer_funds_handler)
        btn_4.clicked.connect(self.show_graphs)
        btn_5.clicked.connect(self.details_handler)

        # Add the checking account internal layout to the checking account horizontal layout
        self.tab_2.setLayout(self.savings_hbox)

    # Credit card account operations **********************************************************************************
    def create_credit_card_tab(self, user_data):
        # Store the username and capitalize the first letter.
        self.username = str(user_data["username"])

        # Create a label to greet the user based on their username when viewing the checking account tab.
        welcome_label_credit_card = qt_widgets.QLabel(f'Hello, {self.username}!', self)

        # Underline and set the font for the welcome label.
        welcome_label_font.setUnderline(True)
        welcome_label_credit_card.setFont(welcome_label_font)

        # Set the dimensions of the table.
        self.table_3.setMaximumWidth(940)
        self.table_3.setMinimumHeight(620)
        self.table_3.setMaximumHeight(620)
        self.credit_card_hbox.addWidget(self.table_3)
        self.table_3.setRowCount(25)
        self.table_3.setColumnCount(6)

        # Set the table headers.
        self.table_3.setHorizontalHeaderItem(0, qt_widgets.QTableWidgetItem("Transaction ID"))
        self.table_3.setHorizontalHeaderItem(1, qt_widgets.QTableWidgetItem("Transaction Type"))
        self.table_3.setHorizontalHeaderItem(2, qt_widgets.QTableWidgetItem("Amount"))
        self.table_3.setHorizontalHeaderItem(3, qt_widgets.QTableWidgetItem("Category"))
        self.table_3.setHorizontalHeaderItem(4, qt_widgets.QTableWidgetItem("Date"))
        self.table_3.setHorizontalHeaderItem(5, qt_widgets.QTableWidgetItem("Time"))

        # Set the columns for the table.
        header = self.table_3.horizontalHeader()
        header.setSectionResizeMode(0, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, qt_widgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, qt_widgets.QHeaderView.Stretch)
        self.table_3.setEditTriggers(qt_widgets.QAbstractItemView.NoEditTriggers)
        self.table_3.verticalHeader().setVisible(False)

        # Checking account buttons.
        btn_1 = qt_widgets.QPushButton("Make A Payment")
        btn_2 = qt_widgets.QPushButton("Request A Cash Advance")
        btn_3 = qt_widgets.QPushButton("Request A Credit Line Increase")
        btn_4 = qt_widgets.QPushButton("Show Graphs")
        btn_5 = qt_widgets.QPushButton("More Details")

        # Create a new layout inside checking for the buttons
        v_layout_inside_credit_card = qt_widgets.QVBoxLayout()
        self.credit_card_hbox.addLayout(v_layout_inside_credit_card)

        # Add the buttons to the layout and set their lengths.
        v_layout_inside_credit_card.addStretch()
        v_layout_inside_credit_card.addWidget(welcome_label_credit_card, alignment=qt_core.Qt.AlignCenter)
        v_layout_inside_credit_card.addStretch()
        v_layout_inside_credit_card.addWidget(btn_1)
        v_layout_inside_credit_card.addStretch()
        v_layout_inside_credit_card.addWidget(btn_2)
        v_layout_inside_credit_card.addStretch()
        v_layout_inside_credit_card.addWidget(btn_3)
        v_layout_inside_credit_card.addStretch()
        v_layout_inside_credit_card.addWidget(btn_4)
        v_layout_inside_credit_card.addStretch()
        v_layout_inside_credit_card.addWidget(btn_5)
        v_layout_inside_credit_card.addStretch()

        # Connect buttons to handlers
        btn_1.clicked.connect(self.make_deposit_handler)
        btn_2.clicked.connect(self.make_withdrawal_handler)
        btn_3.clicked.connect(self.transfer_funds_handler)
        btn_4.clicked.connect(self.show_graphs)
        btn_5.clicked.connect(self.details_handler)

        # Add the checking account internal layout to the checking account horizontal layout
        self.tab_3.setLayout(self.credit_card_hbox)

    # Account overview handlers ***************************************************************************************
    def load_account_data_from_csv(self):
        pass

    def make_deposit_handler(self):
        dt = datetime.datetime.now()

        if self.tab_container.currentIndex() == 0 or self.tab_container.currentIndex() == 1:
            tx_type = qt_widgets.QTableWidgetItem("Deposit")
            amt, ok1 = qt_widgets.QInputDialog.getText(self, 'Make A Deposit',
                                                       'Enter An Amount To Deposit')

            cat, ok2 = qt_widgets.QInputDialog.getText(self, 'Make A Deposit',
                                                       'Enter A Category For The Deposit')
        else:
            tx_type = qt_widgets.QTableWidgetItem("Payment")
            amt, ok1 = qt_widgets.QInputDialog.getText(self, 'Make A Payment',
                                                       'Enter An Amount To Pay')

            cat, ok2 = qt_widgets.QInputDialog.getText(self, 'Make A Payment',
                                                       'Enter A Category For The Payment')

        # Debugging Only Code
        # if ok1 and ok2:
        #     print(str(amt))
        #     print(cat)
        #     cat = str(cat).capitalize()

        if str(amt) == '' or str(cat) == '':
            return

        tx_amt = qt_widgets.QTableWidgetItem(f"${amt}")
        tx_cat = qt_widgets.QTableWidgetItem(f"{cat}")
        tx_date = qt_widgets.QTableWidgetItem(str(dt.strftime("%m") + "/" + dt.strftime("%d") + "/" + dt.strftime("%Y")))
        tx_time = qt_widgets.QTableWidgetItem(str(dt.time().strftime('%H:%M:%S')))

        if self.tab_container.currentIndex() == 0:
            tx_id = qt_widgets.QTableWidgetItem(str(self.chk_tx_number))

            self.table_1.setItem(self.chk_tx_number - 1, 0, tx_id)
            tx_id.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 1, tx_type)
            tx_type.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 2, tx_amt)
            tx_amt.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 3, tx_cat)
            tx_cat.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 4, tx_date)
            tx_date.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 5, tx_time)
            tx_time.setTextAlignment(qt_core.Qt.AlignCenter)

            self.chk_tx_number += 1

        elif self.tab_container.currentIndex() == 1:
            tx_id = qt_widgets.QTableWidgetItem(str(self.svg_tx_number))

            self.table_2.setItem(self.svg_tx_number - 1, 0, tx_id)
            tx_id.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 1, tx_type)
            tx_type.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 2, tx_amt)
            tx_amt.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 3, tx_cat)
            tx_cat.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 4, tx_date)
            tx_date.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 5, tx_time)
            tx_time.setTextAlignment(qt_core.Qt.AlignCenter)

            self.svg_tx_number += 1

        elif self.tab_container.currentIndex() == 2:
            tx_id = qt_widgets.QTableWidgetItem(str(self.crd_tx_number))

            self.table_3.setItem(self.crd_tx_number - 1, 0, tx_id)
            tx_id.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 1, tx_type)
            tx_type.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 2, tx_amt)
            tx_amt.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 3, tx_cat)
            tx_cat.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 4, tx_date)
            tx_date.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 5, tx_time)
            tx_time.setTextAlignment(qt_core.Qt.AlignCenter)

            self.crd_tx_number += 1

    def make_withdrawal_handler(self):
        dt = datetime.datetime.now()

        if self.tab_container.currentIndex() == 0 or self.tab_container.currentIndex() == 1:
            tx_type = qt_widgets.QTableWidgetItem("Withdrawal")
            amt, ok1 = qt_widgets.QInputDialog.getText(self, 'Make A Withdrawal',
                                                       'Enter An Amount To Withdrawal')

            cat, ok2 = qt_widgets.QInputDialog.getText(self, 'Make A Withdrawal',
                                                       'Enter A Category For The Withdrawal')
        else:
            tx_type = qt_widgets.QTableWidgetItem("Cash Advance")
            amt, ok1 = qt_widgets.QInputDialog.getText(self, 'Request A Cash Advance',
                                                       'Enter An Amount To Request')

            cat, ok2 = qt_widgets.QInputDialog.getText(self, 'Request A Cash Advance',
                                                       'Enter A Category For The Request')

        # Debugging Only Code
        # if ok1 and ok2:
        #     print(str(amt))
        #     print(cat)
        #     cat = str(cat).capitalize()

        if str(amt) == '' or str(cat) == '':
            return

        tx_amt = qt_widgets.QTableWidgetItem(f"${amt}")
        tx_cat = qt_widgets.QTableWidgetItem(f"{cat}")
        tx_date = qt_widgets.QTableWidgetItem(
            str(dt.strftime("%m") + "/" + dt.strftime("%d") + "/" + dt.strftime("%Y")))
        tx_time = qt_widgets.QTableWidgetItem(str(dt.time().strftime('%H:%M:%S')))

        if self.tab_container.currentIndex() == 0:
            tx_id = qt_widgets.QTableWidgetItem(str(self.chk_tx_number))

            self.table_1.setItem(self.chk_tx_number - 1, 0, tx_id)
            tx_id.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 1, tx_type)
            tx_type.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 2, tx_amt)
            tx_amt.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 3, tx_cat)
            tx_cat.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 4, tx_date)
            tx_date.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 5, tx_time)
            tx_time.setTextAlignment(qt_core.Qt.AlignCenter)

            self.chk_tx_number += 1

        elif self.tab_container.currentIndex() == 1:
            tx_id = qt_widgets.QTableWidgetItem(str(self.svg_tx_number))

            self.table_2.setItem(self.svg_tx_number - 1, 0, tx_id)
            tx_id.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 1, tx_type)
            tx_type.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 2, tx_amt)
            tx_amt.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 3, tx_cat)
            tx_cat.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 4, tx_date)
            tx_date.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 5, tx_time)
            tx_time.setTextAlignment(qt_core.Qt.AlignCenter)

            self.svg_tx_number += 1

        elif self.tab_container.currentIndex() == 2:
            tx_id = qt_widgets.QTableWidgetItem(str(self.crd_tx_number))

            self.table_3.setItem(self.crd_tx_number - 1, 0, tx_id)
            tx_id.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 1, tx_type)
            tx_type.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 2, tx_amt)
            tx_amt.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 3, tx_cat)
            tx_cat.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 4, tx_date)
            tx_date.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 5, tx_time)
            tx_time.setTextAlignment(qt_core.Qt.AlignCenter)

            self.crd_tx_number += 1

    def transfer_funds_handler(self):
        dt = datetime.datetime.now()

        if self.tab_container.currentIndex() == 0 or self.tab_container.currentIndex() == 1:
            tx_type = qt_widgets.QTableWidgetItem("Transfer")
            amt, ok1 = qt_widgets.QInputDialog.getText(self, 'Transfer Funds',
                                                       'Enter An Amount To Transfer')

            cat, ok2 = qt_widgets.QInputDialog.getText(self, 'Transfer Funds',
                                                       'Enter A Category For The Transfer')
        else:
            tx_type = qt_widgets.QTableWidgetItem("Credit Line Increase")
            amt, ok1 = qt_widgets.QInputDialog.getText(self, 'Request A Credit Line Increase',
                                                       'Enter An Amount To Request')

            cat, ok2 = qt_widgets.QInputDialog.getText(self, 'Request A Credit Line Increase',
                                                       'Enter A Category For The Request')

        # Debugging Only Code
        # if ok1 and ok2:
        #     print(str(amt))
        #     print(cat)
        #     cat = str(cat).capitalize()

        if str(amt) == '' or str(cat) == '':
            return

        tx_amt = qt_widgets.QTableWidgetItem(f"${amt}")
        tx_cat = qt_widgets.QTableWidgetItem(f"{cat}")
        tx_date = qt_widgets.QTableWidgetItem(
            str(dt.strftime("%m") + "/" + dt.strftime("%d") + "/" + dt.strftime("%Y")))
        tx_time = qt_widgets.QTableWidgetItem(str(dt.time().strftime('%H:%M:%S')))

        if self.tab_container.currentIndex() == 0:
            tx_id = qt_widgets.QTableWidgetItem(str(self.chk_tx_number))

            self.table_1.setItem(self.chk_tx_number - 1, 0, tx_id)
            tx_id.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 1, tx_type)
            tx_type.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 2, tx_amt)
            tx_amt.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 3, tx_cat)
            tx_cat.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 4, tx_date)
            tx_date.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_1.setItem(self.chk_tx_number - 1, 5, tx_time)
            tx_time.setTextAlignment(qt_core.Qt.AlignCenter)

            self.chk_tx_number += 1

        elif self.tab_container.currentIndex() == 1:
            tx_id = qt_widgets.QTableWidgetItem(str(self.svg_tx_number))

            self.table_2.setItem(self.svg_tx_number - 1, 0, tx_id)
            tx_id.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 1, tx_type)
            tx_type.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 2, tx_amt)
            tx_amt.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 3, tx_cat)
            tx_cat.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 4, tx_date)
            tx_date.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_2.setItem(self.svg_tx_number - 1, 5, tx_time)
            tx_time.setTextAlignment(qt_core.Qt.AlignCenter)

            self.svg_tx_number += 1

        elif self.tab_container.currentIndex() == 2:
            tx_id = qt_widgets.QTableWidgetItem(str(self.crd_tx_number))

            self.table_3.setItem(self.crd_tx_number - 1, 0, tx_id)
            tx_id.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 1, tx_type)
            tx_type.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 2, tx_amt)
            tx_amt.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 3, tx_cat)
            tx_cat.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 4, tx_date)
            tx_date.setTextAlignment(qt_core.Qt.AlignCenter)

            self.table_3.setItem(self.crd_tx_number - 1, 5, tx_time)
            tx_time.setTextAlignment(qt_core.Qt.AlignCenter)

            self.crd_tx_number += 1

    def show_graphs(self):
        stack.windowStack[3].user_interface()

    def details_handler(self):
        pass
