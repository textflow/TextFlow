from PySide import QtGui

class TextEditor(QtGui.QTextEdit):
    """
    Text editor view.
    """    
    
    def __init__(self, parent):
        super(TextEditor, self).__init__(parent)
        self.setAcceptDrops(True)
        
    def dropEvent(self, event):
        print str(event.mimeData().urls()[0].toLocalFile())
