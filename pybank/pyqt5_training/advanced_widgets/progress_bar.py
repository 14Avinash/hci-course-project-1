import sys
import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core

# for the timer
count = 0

class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress Bar Widget")
        self.setGeometry(350, 150, 500, 500)
        self.user_interface()

    def user_interface(self):
        v_box = qt_widgets.QVBoxLayout()
        h_box = qt_widgets.QHBoxLayout()
        self.progress_bar = qt_widgets.QProgressBar()

        btn_start = qt_widgets.QPushButton("Start")
        btn_start.clicked.connect(self.timer_start)
        btn_stop = qt_widgets.QPushButton("Stop")
        btn_stop.clicked.connect(self.timer_stop)

        self.timer = qt_core.QTimer()
        self.timer.setInterval(100)  # set interval so that every 100 ms update the progress bar
        self.timer.timeout.connect(self.run_progress_bar)

        v_box.addWidget(self.progress_bar)
        v_box.addLayout(h_box)

        h_box.addWidget(btn_start)
        h_box.addWidget(btn_stop)

        self.setLayout(v_box)

        self.show()

    def run_progress_bar(self):
        global count
        count += 1
        print(count)
        self.progress_bar.setValue(count)

        if count == 100:
            self.timer.stop()
            count = 0

    def timer_start(self):
        self.timer.start()

    def timer_stop(self):
        self.timer.stop()
