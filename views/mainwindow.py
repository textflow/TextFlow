from PySide import QtGui, QtCore
from ui.mainwindow import Ui_MainWindow
from controllers.mainwindow import MainWindowController

class MainWindowView(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        self.setupUi(self)
        self.controller = MainWindowController()
        
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL("triggered()"), self.open_menu_clicked)
        
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL("triggered()"), self.save_menu_clicked)
        
    def open_menu_clicked(self):
        filepath = QtGui.QFileDialog.getOpenFileName()
        status, document = self.controller.open(filepath)
        
        if status == "ok":
            self.textEdit.setPlainText(document.text)
        elif status == "fail":
            QtGui.QMessageBox.critical(self, "Error",
                                       "The file <b>%s</b> doesn't exists." % filepath,
                                       QtGui.QMessageBox.Ok)
                                       
    def save_menu_clicked(self):
        status = self.controller.save(self.textEdit.toPlainText())
        
        if status == "fail":
            filepath = QtGui.QFileDialog.getSaveFileName()
            self.controller.save(self.textEdit.toPlainText(), filepath)
            
