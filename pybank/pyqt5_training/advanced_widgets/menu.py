import sys
import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtGui as qt_gui


class Window(qt_widgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Widget")
        self.setGeometry(350, 150, 600, 600)
        self.user_interface()

    def user_interface(self):
        # Main Menu
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)  # For macOS which treats menu bars differently
        file_bar = menu_bar.addMenu("File")
        edit_bar = menu_bar.addMenu("Edit")
        view_bar = menu_bar.addMenu("View")
        window_bar = menu_bar.addMenu("Window")
        help_bar = menu_bar.addMenu("Help")

        # Sub-menu
        new_project = qt_widgets.QAction("New Project", self)
        new_project.setShortcut("Crtl+N")
        file_bar.addAction(new_project)

        open_project = qt_widgets.QAction("Open Project", self)
        open_project.setShortcut("Crtl+O")
        file_bar.addAction(open_project)

        exit_app = qt_widgets.QAction("Exit", self)
        exit_app.setShortcut("Alt+F4")
        exit_app.setIcon(qt_gui.QIcon('./icons/exit.png'))
        exit_app.triggered.connect(self.exit_func)
        file_bar.addAction(exit_app)

        self.show()

    def exit_func(self):
        msg_box = qt_widgets.QMessageBox.information(self,
                                                     "Warning",
                                                     "Are you sure you want to exit?",
                                                     qt_widgets.QMessageBox.Yes | qt_widgets.QMessageBox.No,
                                                     qt_widgets.QMessageBox.No)

        if msg_box == qt_widgets.QMessageBox.Yes:
            sys.exit()
