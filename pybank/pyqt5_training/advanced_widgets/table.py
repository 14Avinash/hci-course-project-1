import sys
import  PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table")
        self.setGeometry(350, 150, 400, 400)
        self.user_interface()

    def user_interface(self):
        main_layout = qt_widgets.QVBoxLayout()

        self.table = qt_widgets.QTableWidget()
        main_layout.addWidget(self.table)

        btn = qt_widgets.QPushButton("Get")
        main_layout.addWidget(btn)

        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0, qt_widgets.QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(1, qt_widgets.QTableWidgetItem("Surname"))
        self.table.setHorizontalHeaderItem(2, qt_widgets.QTableWidgetItem("Address"))

        # Hide the column headers...
        # self.table.horizontalHeader().hide()
        # self.table.verticalHeader().hide()

        # Add items to cells in the table
        self.table.setItem(0, 0, qt_widgets.QTableWidgetItem("Red"))
        self.table.setItem(0, 1, qt_widgets.QTableWidgetItem("Blue"))
        self.table.setItem(1, 0, qt_widgets.QTableWidgetItem("Yellow"))
        self.table.setItem(4, 2, qt_widgets.QTableWidgetItem("Green"))
        self.table.setEditTriggers(qt_widgets.QAbstractItemView.NoEditTriggers)  # Make cells not editable

        btn.clicked.connect(self.get_value)  # Get cell values using the button
        self.table.doubleClicked.connect(self.double_clicked)  # Get cell values using double-click

        self.setLayout(main_layout)

        self.show()

    def get_value(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())

    def double_clicked(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())
