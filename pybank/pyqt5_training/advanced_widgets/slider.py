import sys
import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import PyQt5.QtGui as qt_gui


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.text_2 = qt_widgets.QLabel("Hello, Python")
        self.text_1 = qt_widgets.QLabel("0")
        self.setWindowTitle("Slider")
        self.setGeometry(350, 150, 600, 500)
        self.slider = qt_widgets.QSlider(qt_core.Qt.Horizontal)
        self.user_interface()

    def user_interface(self):
        v_box = qt_widgets.QVBoxLayout()
        v_box.addWidget(self.slider)

        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(qt_widgets.QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.get_value)
        self.text_1.setAlignment(qt_core.Qt.AlignCenter)

        v_box.addWidget(self.text_1)
        v_box.addWidget(self.text_2)
        v_box.addStretch()

        self.setLayout(v_box)

        self.show()

    def get_value(self):
        val = self.slider.value()
        print(val)
        self.text_1.setText(str(val))
        font_size = self.slider.value()
        font = qt_gui.QFont("Times", font_size)
        self.text_2.setFont(font)