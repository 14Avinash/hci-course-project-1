import sys
import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtGui as qt_gui

# Set the font family and font size
font = qt_gui.QFont('Times', 11)

class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Message Boxes')
        self.setGeometry(250, 150, 500, 500)
        self.user_interface()

    def user_interface(self):
        button = qt_widgets.QPushButton('Click Me', self)
        # button.setFont(font)
        button.move(200, 150)
        button.clicked.connect(self.message_box)

        self.show()

    def message_box(self):
        # Create a question message box
        # q_message_box = qt_widgets.QMessageBox.question(self, 'Warning', 'Are you sure you would like to continue?',
        #                                                 qt_widgets.QMessageBox.No |     # Message Box No button
        #                                                 qt_widgets.QMessageBox.Yes |    # Message Box Yes button
        #                                                 qt_widgets.QMessageBox.Cancel,  # Message Box Cancel button
        #                                                 qt_widgets.QMessageBox.Cancel)  # Set Focus on Cancel button
        #
        # if q_message_box == qt_widgets.QMessageBox.Yes:
        #     print('You clicked Yes')
        # elif q_message_box == qt_widgets.QMessageBox.No:
        #     print('You clicked No')
        # else:
        #     print('You clicked Cancel')

        # Create an information message box
        i_message_box = qt_widgets.QMessageBox.information(self, 'Information', 'You are now logged out.')
