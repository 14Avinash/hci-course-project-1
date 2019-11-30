import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Widget")
        self.setGeometry(350, 150, 600, 600)
        self.user_interface()

    def user_interface(self):
        main_layout = qt_widgets.QVBoxLayout()
        self.tab_container = qt_widgets.QTabWidget()

        self.tab_1 = qt_widgets.QWidget()
        self.tab_2 = qt_widgets.QWidget()
        self.tab_3 = qt_widgets.QWidget()

        # Add tabs to main tab
        self.tab_container.addTab(self.tab_1, "Tab 1")
        self.tab_container.addTab(self.tab_2, "Tab 2")
        self.tab_container.addTab(self.tab_3, "Tab 3")

        # Add widgets to tabs
        inner_v_box = qt_widgets.QVBoxLayout()
        inner_h_box = qt_widgets.QHBoxLayout()

        self.some_text = qt_widgets.QLabel("Hello Python")
        self.btn_1 = qt_widgets.QPushButton("First Tab Button")
        self.btn_1.clicked.connect(self.btn_func)
        self.btn_2 = qt_widgets.QPushButton("Second Tab Button")

        inner_v_box.addWidget(self.some_text)
        inner_v_box.addWidget(self.btn_1)
        inner_h_box.addWidget(self.btn_2)

        self.tab_1.setLayout(inner_v_box)
        self.tab_2.setLayout(inner_h_box)

        main_layout.addWidget(self.tab_container)

        self.setLayout(main_layout)

        self.show()

    def btn_func(self):
        self.btn_1.setText("You clicked the button!")
