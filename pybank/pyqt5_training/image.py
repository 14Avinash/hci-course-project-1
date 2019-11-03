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
        # Set the image location
        self.image.setPixmap(qt_gui.QPixmap('./img/abstract.jpg'))

        # Create the hide image button
        hide_image_button = qt_widgets.QPushButton('Hide', self)
        # Place/move the hide image button
        hide_image_button.move(540, 600)
        # Create an event handler function for hiding the image
        hide_image_button.clicked.connect(self.hide_image)

        # Create the show image button
        show_image_button = qt_widgets.QPushButton('Show', self)
        # Place/move the show image button
        show_image_button.move(780, 600)
        # Create an event handler function for showing the image
        show_image_button.clicked.connect(self.show_image)

        # Display the application window
        self.show()

    # Event handler to hide the image
    def hide_image(self):
        self.image.close()

    # Event handler to show the image
    def show_image(self):
        self.image.show()
