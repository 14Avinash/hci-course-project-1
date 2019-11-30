import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal and Vertical Box Layout")
        self.setGeometry(50, 50, 400, 400)
        self.user_interface()

    def user_interface(self):
        # Must use vertical layout for main window
        main_layout = qt_widgets.QVBoxLayout()
        # Layouts inside the main window can be of either type
        top_layout_inside_main = qt_widgets.QHBoxLayout()
        bottom_layout_inside_main = qt_widgets.QHBoxLayout()

        # Add internal layouts to the main layout
        main_layout.addLayout(top_layout_inside_main)
        main_layout.addLayout(bottom_layout_inside_main)

        # Create widgets
        chk_box = qt_widgets.QCheckBox()
        radio_btn = qt_widgets.QRadioButton()
        combo_box = qt_widgets.QComboBox()
        btn_1 = qt_widgets.QPushButton()
        btn_2 = qt_widgets.QPushButton()

        # Add widgets to the top layout
        top_layout_inside_main.setContentsMargins(150, 10, 20, 20)  # parameters are in clockwise order
        top_layout_inside_main.addWidget(combo_box)
        top_layout_inside_main.addWidget(radio_btn)
        top_layout_inside_main.addWidget(chk_box)

        # Add widgets to the bottom layout
        bottom_layout_inside_main.setContentsMargins(150, 10, 150, 10)
        bottom_layout_inside_main.addWidget(btn_1)
        bottom_layout_inside_main.addWidget(btn_2)

        # Set the layout for the window
        self.setLayout(main_layout)

        self.show()
