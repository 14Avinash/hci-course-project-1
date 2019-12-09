import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import PyQt5.QtGui as qt_gui
import handlers.userhandler as user_handling
import pyqt5_global.variables as stack
import matplotlib.pyplot as plt
import matplotlib.figure as plt_fig
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


#Login window class and functionality
class Window_Graphs(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyBank')
        self.setGeometry(50, 50, 500, 500)
        self.setProperty('Main_Window', True)

    def user_interface(self):
        self.layout = qt_widgets.QVBoxLayout()

        graph_canvas = Graph_Canvas(self, width=5, height=3)


        # self.layout.addWidget(static_canvas)

        #Username Entry
        # self.textUser = qt_widgets.QLineEdit(self)
        # self.labelUser = qt_widgets.QLabel(self)
        # self.labelUser.setText('Username')
        # self.layout.addWidget(self.labelUser, 3, 1)
        # self.layout.addWidget(self.textUser, 4, 1, 1, 3)

        self.setLayout(self.layout)

        self.show()

class Graph_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        #Graph Canvas
        self.fig = plt_fig.Figure(figsize=(width, height))
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.figure_colors()
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], color="#bb86fc")
        self.axes.plot([0, 1, 2, 3], [2, 4, 3, 3], color="#8858c8")
        self.axes.plot([0, 1, 2, 3], [1, 4, 0, 6], color="#efb7ff")
    def figure_colors(self):
        self.fig.set_facecolor('#180f20')
        self.axes.set_facecolor('#3e3547')
        self.axes.spines["bottom"].set_color('#695f72')
        self.axes.spines["left"].set_color('#695f72')
        self.axes.tick_params(axis='x', colors='white')
        self.axes.tick_params(axis='y', colors='white')
