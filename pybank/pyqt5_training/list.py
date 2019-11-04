import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.list_widget = qt_widgets.QListWidget(self)
        self.add_record = qt_widgets.QLineEdit(self)
        self.setWindowTitle('Using List Widgets')
        self.setGeometry(50, 50, 500, 500)
        self.user_interface()

    def user_interface(self):
        self.add_record.move(100, 50)
        self.list_widget.move(100, 80)

        list_of_items = ['Batman', 'Spiderman', 'Wonderwoman']
        self.list_widget.addItems(list_of_items)
        self.list_widget.addItem('Superman')

        btn_add = qt_widgets.QPushButton('Add', self)
        btn_add.move(360, 80)
        btn_add.clicked.connect(self.func_add)

        btn_delete = qt_widgets.QPushButton('Delete', self)
        btn_delete.move(360, 110)
        btn_delete.clicked.connect(self.func_delete)

        btn_get = qt_widgets.QPushButton('Get', self)
        btn_get.move(360, 140)
        btn_get.clicked.connect(self.func_get)

        btn_delete_all = qt_widgets.QPushButton('Delete All', self)
        btn_delete_all.move(360, 170)
        btn_delete_all.clicked.connect(self.func_delete_all)

        self.show()

    def func_add(self):
        value = self.add_record.text()   # get the item from the QLineEdit text field
        self.list_widget.addItem(value)  # add the item to the list of items
        self.add_record.setText('')      # reset the QLineEdit text field so that it is blank after adding

    def func_delete(self):
        item_index = self.list_widget.currentRow()
        # print(item_index)  # prints the index value for the associated list item
        self.list_widget.takeItem(item_index)

    def func_get(self):
        item = self.list_widget.currentItem().text()
        print(item)

    def func_delete_all(self):
        self.list_widget.clear()

