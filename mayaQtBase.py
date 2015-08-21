from PyQt4 import QtCore, QtGui
import sip
from maya import OpenMayaUI as omui
from maya import cmds

def getMayaMainWindow():
    mainWin = omui.MQtUtil.mainWindow()
    return sip.wrapinstance(long(mainWin), 
                            QtCore.QObject)

def dockUI(iUI):
    if (cmds.dockControl(str(iUI.windowTitle()), q = True, exists = True)):
        cmds.deleteUI(str(iUI.windowTitle()))

    allowedAreas = ["left", "right"]
    cmds.dockControl(str(iUI.windowTitle()), area = "left", 
                     content = str(iUI.objectName()),
                     allowedArea = allowedAreas, width = 400,
                     vcc = lambda *x: iUI.close(), sizeable = True)
    iUI.show()
    

class MayaQtWindowBase(QtGui.QMainWindow):
    def __init__(self, parent = getMayaMainWindow(),
                 uniqueHandle = "QtMayaWindowBase"):
        #
        super(MayaQtWindowBase, self).__init__(parent)
        self.setWindowTitle("MayaQtWindow")
        self.setObjectName(uniqueHandle)
        self.resize(400, 200)
        #
        self.dockButton = QtGui.QPushButton("Dock", self)
        self.undockButton = QtGui.QPushButton("Undock", self)
        #
        mainWidget = QtGui.QWidget(self)
        layout = QtGui.QVBoxLayout(self)
        self.setCentralWidget(mainWidget)
        mainWidget.setLayout(layout)
        mainWidget.setVisible(True)
        layout.addWidget(self.dockButton)
        layout.addWidget(self.undockButton)
        #
        self.dockButton.clicked.connect(self.dockMe)
        self.undockButton.clicked.connect(self.undockMe)
        #
        self.show()
        
    def dockMe(self):
        #add PyQt window controls here
        dockUI(self)

    def undockMe(self):
        self.close()
        self.show()


class MayaQtDialogBase(QtGui.QDialog):
    def __init__(self, parent):
        super(MayaQtDialogBase, self).__init__(parent)
        #
        self.setWindowTitle("MayaQtDialogBase")
        self.resize(400,100)
        
        self.button = QtGui.QPushButton("Print", self)
        self.quit = QtGui.QPushButton("Quit", self)
        self.combo = QtGui.QComboBox()
        self.combo.addItems([str(x + 1) for x in range(10)])
        
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.combo)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.quit)

        self.button.clicked.connect(self.output)
        self.quit.clicked.connect(self.close)
        self.show()
        self.raise_()

    def output(self):
        print self.combo.currentText()

    def clickedClose(self):
        self.close()
        

