import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Combo Boxes')
        self.setGeometry(250, 150, 500, 500)
        self.user_interface()

    def user_interface(self):
        # Create combo box
        self.combo = qt_widgets.QComboBox(self)
        self.combo.move(150, 100)

        # Add a single item to the combo box
        # self.combo.addItem('Python')

        # Add multiple items to the combo box
        self.combo.addItems(['Python', 'C++', 'Java', 'Go'])

        # Add additional items to the combo box using list and for loop
        list_of_combo_items = ['PHP', 'HTML', 'CSS', 'SQL']

        for item in list_of_combo_items:
            self.combo.addItem(item)

        # for number in range(18, 101):
        #     self.combo.addItem(str(number))

        # Create save button
        button = qt_widgets.QPushButton('Save', self)
        button.move(150, 150)
        button.clicked.connect(self.get_combo_value)

        self.show()

    def get_combo_value(self):
        value = self.combo.currentText()
        print(value)