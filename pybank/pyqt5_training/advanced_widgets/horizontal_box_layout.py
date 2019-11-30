import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Box Layout")
        self.setGeometry(50, 50, 400, 400)
        self.user_interface()

    def user_interface(self):
        h_box = qt_widgets.QHBoxLayout()

        btn_1 = qt_widgets.QPushButton("Button 1")
        btn_2 = qt_widgets.QPushButton("Button 2")
        btn_3 = qt_widgets.QPushButton("Button 3")

        h_box.addStretch()
        h_box.addWidget(btn_1)
        h_box.addWidget(btn_2)
        h_box.addWidget(btn_3)
        h_box.addStretch()

        self.setLayout(h_box)

        self.show()
