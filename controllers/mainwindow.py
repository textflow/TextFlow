from PySide import QtCore, QtGui

from views.mainwindow import MainWindowView
from models.document import Document

class MainWindowController(object):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.view = MainWindowView()
        self.document = Document()
        
        QtCore.QObject.connect(self.view.actionOpen, QtCore.SIGNAL("triggered()"), self.open_button_clicked)
    
    def show_view(self):
        self.view.show()
        
    def open_button_clicked(self):
        filepath = QtGui.QFileDialog.getOpenFileName()
        self.document.open(filepath)
        self.view.textEdit.setPlainText(self.document.text)
