from PySide import QtGui, QtCore
from ui.mainwindow import Ui_MainWindow
from controllers.mainwindow import MainWindowController

class MainWindowView(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        self.setupUi(self)
        self.controller = MainWindowController()
        
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL("triggered()"), self.open_button_clicked)
        
    def open_button_clicked(self):
        filepath = QtGui.QFileDialog.getOpenFileName()
        status, document = self.controller.open(filepath)
        
        if status == "ok":
            self.textEdit.setPlainText(document.text)
        elif status == "fail":
            QtGui.QMessageBox.critical(self, "Error",
                                       "The file <b>%s</b> doesn't exists." % filepath,
                                       QtGui.QMessageBox.Ok)
