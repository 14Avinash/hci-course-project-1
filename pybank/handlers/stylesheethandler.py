import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtCore as qt_core
import globalvars.variables as globalvars


def readQSS():
    globalvars.stylesheetPath = "globalvars/stylesheet.qss"

    with open(globalvars.stylesheetPath, "r") as sheetFile:
        globalvars.stylesheet = sheetFile.read()
