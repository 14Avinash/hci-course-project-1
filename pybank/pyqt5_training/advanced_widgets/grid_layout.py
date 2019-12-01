import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        self.setGeometry(350, 150, 600, 600)
        self.user_interface()

    def user_interface(self):
        self.grid_layout = qt_widgets.QGridLayout()
        # btn_1 = qt_widgets.QPushButton('Button 1')
        # btn_2 = qt_widgets.QPushButton('Button 2')
        # btn_3 = qt_widgets.QPushButton('Button 3')
        # btn_4 = qt_widgets.QPushButton('Button 4')
        #
        # self.grid_layout.addWidget(btn_1, 0, 0)
        # self.grid_layout.addWidget(btn_2, 0, 1)
        # self.grid_layout.addWidget(btn_3, 1, 0)
        # self.grid_layout.addWidget(btn_4, 1, 1)

        for i in range(0, 3):
            for j in range (0, 3):
                btn = qt_widgets.QPushButton("Button Row: {} Column: {}".format(i, j))
                self.grid_layout.addWidget(btn, i, j)
                btn.clicked.connect(self.was_clicked)

        self.setLayout(self.grid_layout)

        self.show()

    def was_clicked(self):
        button_id = self.sender().text()

        if button_id == 'Button Row: 0 Column: 0':
            print('You clicked the first button.')
