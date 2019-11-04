import sys
import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtGui as qt_gui
import PyQt5.QtCore as qt_core

font = qt_gui.QFont('Times', 14)


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Timer')
        self.setGeometry(250, 350, 350, 350)
        self.user_interface()

    def user_interface(self):
        self.color_label = qt_widgets.QLabel(self)
        self.color_label.resize(250, 250)
        self.color_label.setStyleSheet('background-color: green')
        self.color_label.move(50, 40)
        # Buttons
        btn_start = qt_widgets.QPushButton('Start', self)
        btn_stop = qt_widgets.QPushButton('Stop', self)
        btn_start.move(90, 300)
        btn_stop.move(190, 300)
        btn_start.clicked.connect(self.start)
        btn_stop.clicked.connect(self.stop)
        # Timer
        self.timer = qt_core.QTimer()
        self.timer.setInterval(1000)  # 1000 ms <--->  1 second
        self.timer.timeout.connect(self.change_color)
        self.value = 0

        self.show()

    def change_color(self):
        if self.value == 0:
            self.color_label.setStyleSheet('background-color: yellow')
            self.value = 1
        elif self.value == 1:
            self.color_label.setStyleSheet('background-color: red')
            self.value = 0

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()