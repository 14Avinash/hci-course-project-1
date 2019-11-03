import sys
import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtGui as qt_gui


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.image = qt_widgets.QLabel(self)
        self.setWindowTitle("Using Images")
        self.setGeometry(50, 50, 1280, 720)
        self.user_interface()

    def user_interface(self):
        self.image.setPixmap(qt_gui.QPixmap('./img/abstract.jpg'))

        hide_image_button = qt_widgets.QPushButton('Hide', self)
        hide_image_button.move(540, 600)
        hide_image_button.clicked.connect(self.hide_image)

        show_image_button = qt_widgets.QPushButton('Show', self)
        show_image_button.move(780, 600)
        show_image_button.clicked.connect(self.show_image)

        self.show()

    def hide_image(self):
        self.image.close()

    def show_image(self):
        self.image.show()
