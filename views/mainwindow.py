from PySide import QtGui
from ui.mainwindow import Ui_MainWindow

class MainWindowView(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        self.setupUi(self)
        
