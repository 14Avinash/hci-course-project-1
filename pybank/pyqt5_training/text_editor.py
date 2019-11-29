import sys
import PyQt5.QtWidgets as qt_widgets


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Text Editor')
        self.setGeometry(250, 150, 500, 500)
        self.user_interface()

    def user_interface(self):
        self.editor = qt_widgets.QTextEdit(self)
        self.editor.setAcceptRichText(False)  # do not allow rich text
        self.editor.move(150, 80)
        button = qt_widgets.QPushButton('Send Response', self)
        button.move(275, 280)
        button.clicked.connect(self.get_value)

        self.show()

    def get_value(self):
        text = self.editor.toPlainText()  # must use 'toPlainText' because editor accepts rich text
        print(text)
