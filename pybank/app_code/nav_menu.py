import sys
import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtGui as qt_gui


class Window(qt_widgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Main menu options
        self.menu_bar = self.menuBar()
        self.file_bar = self.menu_bar.addMenu("File")
        self.edit_bar = self.menu_bar.addMenu("Edit")
        self.view_bar = self.menu_bar.addMenu("View")
        self.window_bar = self.menu_bar.addMenu("Window")
        self.help_bar = self.menu_bar.addMenu("Help")
        self.setGeometry(50, 50, 1280, 100)
        self.user_interface()

    def user_interface(self):
        self.menu_bar.setNativeMenuBar(False)  # For macOS which treats menu bars differently

        # Add selections to the navigation menu
        self.add_file_bar_selections()
        self.add_edit_bar_selections()
        self.add_view_bar_selections()
        self.add_window_bar_selections()
        self.add_help_bar_selections()

        # Show the navigation menu
        self.show()


    def add_file_bar_selections(self):
        self.about_pybank = qt_widgets.QAction("About PyBank", self)
        self.about_pybank.setShortcut("Alt+I")
        self.file_bar.addAction(self.about_pybank)

        self.check_for_updates = qt_widgets.QAction("Check for Updates", self)
        self.check_for_updates.setShortcut("Alt+U")
        self.file_bar.addAction(self.check_for_updates)

        self.preferences = qt_widgets.QAction("Preferences", self)
        self.preferences.setShortcut("Alt+P")
        self.file_bar.addAction(self.preferences)

        self.hide_pybank = qt_widgets.QAction("Hide PyBank", self)
        self.hide_pybank.setShortcut("Alt+H")
        self.file_bar.addAction(self.hide_pybank)

        self.exit_app = qt_widgets.QAction("Exit", self)
        self.exit_app.setShortcut("Alt+F4")
        self.exit_app.setIcon(qt_gui.QIcon('./icons/exit.png'))
        self.exit_app.triggered.connect(self.exit_func)
        self.file_bar.addAction(self.exit_app)

    def add_edit_bar_selections(self):
        self.cut = qt_widgets.QAction("Cut", self)
        self.cut.setShortcut("Alt+X")
        self.edit_bar.addAction(self.cut)

        self.copy = qt_widgets.QAction("Copy", self)
        self.copy.setShortcut("Alt+C")
        self.edit_bar.addAction(self.copy)


        self.paste = qt_widgets.QAction("Paste", self)
        self.paste.setShortcut("Alt+V")
        self.edit_bar.addAction(self.paste)

        self.find = qt_widgets.QAction("Find", self)
        self.find.setShortcut("Alt+F")
        self.edit_bar.addAction(self.find)

    def add_view_bar_selections(self):
        self.view = qt_widgets.QAction("Appearance", self)
        self.view.setShortcut("Alt+A")
        self.view_bar.addAction(self.view)

    def add_window_bar_selections(self):
        self.minimize = qt_widgets.QAction("Minimize", self)
        self.minimize.setShortcut("Alt+-")
        self.window_bar.addAction(self.minimize)

        self.maximize = qt_widgets.QAction("Maximize", self)
        self.maximize.setShortcut("Alt++")
        self.window_bar.addAction(self.maximize)

        self.restore_default_layout = qt_widgets.QAction("Restore Default Layout", self)
        self.restore_default_layout.setShortcut("Alt+D")
        self.window_bar.addAction(self.restore_default_layout)

    def add_help_bar_selections(self):
        self.getting_started = qt_widgets.QAction("Getting Started", self)
        self.getting_started.setShortcut("Alt+G")
        self.help_bar.addAction(self.getting_started)

        self.contact_support = qt_widgets.QAction("Contact Support", self)
        self.contact_support.setShortcut("Alt+S")
        self.help_bar.addAction(self.contact_support)

        self.register_product = qt_widgets.QAction("Register Product", self)
        self.register_product.setShortcut("Alt+R")
        self.help_bar.addAction(self.register_product)


    def exit_func(self):
        msg_box = qt_widgets.QMessageBox.information(self,
                                                     "Warning",
                                                     "Are you sure you want to exit?",
                                                     qt_widgets.QMessageBox.Yes | qt_widgets.QMessageBox.No,
                                                     qt_widgets.QMessageBox.No)

        if msg_box == qt_widgets.QMessageBox.Yes:
            sys.exit()
