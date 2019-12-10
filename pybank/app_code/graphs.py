import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import PyQt5.QtGui as qt_gui
from PyQt5.QtWidgets import QGridLayout, QRadioButton

import handlers.userhandler as user_handling
import pyqt5_global.variables as stack
import matplotlib.pyplot as plt
import matplotlib.figure as plt_fig
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import app_code.nav_menu as nav_menu


#Login window class and functionality
class Window_Graphs(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = qt_widgets.QVBoxLayout()
        self.nav_h_layout = qt_widgets.QHBoxLayout()
        self.graph_layout = qt_widgets.QVBoxLayout()
        self.setWindowTitle('Show Graphs')
        self.setGeometry(50, 50, 500, 500)
        self.setProperty('Main_Window', True)

    def user_interface(self):
        # Create the navigation menu layout
        self.nav_h_layout.addWidget(nav_menu.Window())
        self.nav_h_layout.setContentsMargins(1, 0, 0, 0)
        self.nav_h_layout.setSpacing(0)

        graph_canvas = Graph_Canvas(self, width=5, height=4)
        self.graph_layout.addWidget(graph_canvas)

        close_window_btn = qt_widgets.QPushButton("Close Window", self)
        close_window_btn.clicked.connect(self.close_window)
        self.graph_layout.addWidget(close_window_btn)

        # Add the navigation menu and tabs to the main layout
        self.main_layout.addLayout(self.nav_h_layout)
        self.main_layout.addLayout(self.graph_layout, stretch=5)

        self.setLayout(self.main_layout)
        self.show()

    def close_window(self):
        self.close()


class Graph_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=6, height=10, dpi=100):
        #Graph Canvas
        self.fig = plt_fig.Figure(figsize=(width, height))
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.figure_colors()
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], color="#bb86fc")
        self.axes.plot([0, 1, 2, 3], [2, 4, 3, 3], color="#8858c8")
        self.axes.plot([0, 1, 2, 3], [1, 4, 0, 6], color="#efb7ff")
        self.axes.set_ylabel("Spending")
        self.axes.set_xlabel("Time")
        self.axes.xaxis.label.set_color('white')
        self.axes.yaxis.label.set_color('white')
        self.fig.subplots_adjust(left=0.2, right=0.9, bottom=0.3, top=0.9)

    def figure_colors(self):
        self.fig.set_facecolor('#180f20')
        self.axes.set_facecolor('#3e3547')
        self.axes.spines["bottom"].set_color('#695f72')
        self.axes.spines["left"].set_color('#695f72')
        self.axes.tick_params(axis='x', colors='white')
        self.axes.tick_params(axis='y', colors='white')
