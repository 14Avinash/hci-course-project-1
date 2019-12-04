# form layout uses rows
# set the rows then add widgets for each row
import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout")
        self.setGeometry(350, 150, 400, 400)
        self.user_interface()

    def user_interface(self):
        # Create the main layout as a form layout
        form_layout = qt_widgets.QFormLayout()
        # form_layout.setRowWrapPolicy(qt_widgets.QFormLayout.WrapAllRows)
        name_lbl = qt_widgets.QLabel("Name: ")
        first_name_input = qt_widgets.QLineEdit()
        first_name_input.setPlaceholderText("First Name")
        last_name_input = qt_widgets.QLineEdit()
        last_name_input.setPlaceholderText("Last Name")
        passw_lbl = qt_widgets.QLabel("Password: ")
        passw_input = qt_widgets.QLineEdit()
        passw_input.setPlaceholderText("Password")

        # Create an inner horizontal box layout for the 'Enter' and 'Exit' buttons
        first_inner_h_box = qt_widgets.QHBoxLayout()
        first_inner_h_box.addStretch()
        first_inner_h_box.addWidget(qt_widgets.QPushButton("Enter"))
        first_inner_h_box.addWidget(qt_widgets.QPushButton("Exit"))
        first_inner_h_box.addStretch()

        # Create an inner horizontal box layout for the First and last name input fields
        second_inner_h_box = qt_widgets.QHBoxLayout()
        second_inner_h_box.addWidget(first_name_input)
        second_inner_h_box.addWidget(last_name_input)

        # The code below shows one way to add the 'Enter' and 'Exit' buttons but it is NOT ideal...
        # ...DONT USE - form_layout.addRow(qt_widgets.QPushButton("Enter"), qt_widgets.QPushButton("Exit"))

        self.setLayout(form_layout)

        self.show()
