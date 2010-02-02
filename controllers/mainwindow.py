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
            success = False
        else:
            success = True
        
        return success, self.document
        
    def save(self, text, path=None):
        self.document.text = text
        
        if path is not None:
            self.document.path = path
        
        try:
            self.document.save()
        except IOError:
            return "fail"
        else:
            return "ok"
