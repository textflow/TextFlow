from PySide import QtGui
from controllers.texteditor import TextEditorController

class TextEditor(QtGui.QTextEdit):
    """
    Text editor view.
    """    
    
    def __init__(self, parent):
        super(TextEditor, self).__init__(parent)
        self.setAcceptDrops(True)
        
        self.controller = TextEditorController()
        
    def dropEvent(self, event):
        filepath = str(event.mimeData().urls()[0].toLocalFile())

        success, document = self.controller.open(filepath)
            
        if success:
            self.setPlainText(document.text)
        else:
            QtGui.QMessageBox.critical(self, "Error",
                                       "The file <b>%s</b> doesn't exists." % 
                                       filepath, QtGui.QMessageBox.Ok)
