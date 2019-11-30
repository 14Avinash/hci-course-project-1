import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical Box Layout")
        self.setGeometry(50, 50, 400, 400)
        self.user_interface()

    def user_interface(self):
        v_box = qt_widgets.QVBoxLayout()

        btn_1 = qt_widgets.QPushButton("Save")
        btn_2 = qt_widgets.QPushButton("Cancel")
        btn_3 = qt_widgets.QPushButton("Exit")

        v_box.addStretch()
        v_box.addWidget(btn_1)
        v_box.addWidget(btn_2)
        v_box.addWidget(btn_3)
        # v_box.addStretch()

        self.setLayout(v_box)

        self.show()
