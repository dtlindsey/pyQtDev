from PyQt4 import QtCore, QtGui
import sip
from maya import OpenMayaUI as omui

def getMayaMainWindow():
    mainWin = omui.MQtUtil.mainWindow()
    return sip.wrapinstance(long(mainWin), 
                            QtCore.QObject)

class QtMayaWindowBase(QtGui.QMainWindow):
    def __init__(self, parent = getMayaMainWindow(),
                 uniqueHandle = "QtMayaWindowBase"):
        #QtGui.QMainWindow.__init__(self, parent)
        super(QtMayaWindowBase, self).__init__(parent)
        self.setWindowTitle("QtMayaWin")
        self.setObjectName(uniqueHandle)
        #
        self.resize(400, 200)
        self.setWindow()
        self.show()
        
    def setWindow(self):
        #add PyQt window controls here
        btn = QtGui.QPushButton("Quit", self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
