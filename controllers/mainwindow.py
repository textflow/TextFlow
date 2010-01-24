from PySide import QtGui

from models.document import Document

class MainWindowController(object):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.document = Document()
        
    def open(self, path):
        try:
            self.document.open(path)
        except IOError:
            status = "fail"
        else:
            status = "ok"
        
        return status, self.document
