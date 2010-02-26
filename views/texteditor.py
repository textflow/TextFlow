from PyQt4 import QtGui
from PyQt4.QtCore import QSize, Qt
from controllers.texteditor import TextEditorController

class TFEditor(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.text_editor = TextEditor(parent)
        self.line_numbers = LineNumbers(self.text_editor, parent)
        
        hbox = QtGui.QHBoxLayout()
        hbox.setSpacing(0)
        hbox.addWidget(self.line_numbers)
        hbox.addWidget(self.text_editor)
        self.setLayout(hbox)

class TextEditor(QtGui.QTextEdit):
    """
    Text editor view.
    """    
    
    def __init__(self, parent):
        super(TextEditor, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setFrameShape(QtGui.QFrame.NoFrame)
        
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
                                       
class LineNumbers(QtGui.QWidget):
    def __init__(self, text_editor, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.text_editor = text_editor
        self.text_editor.installEventFilter(self)
    
    def paintEvent(self, event):
        # paint background
        back_brush = QtGui.QBrush(QtGui.QColor("#6699FF"))
        painter = QtGui.QPainter(self)
        painter.fillRect(event.rect(), back_brush)
        
        
        document = self.text_editor.document()
        block = document.begin()
        
        line_number = 1
        while block.isValid():
            position = document.documentLayout().blockBoundingRect(block).topLeft()
            
            #write a line
            pen = QtGui.QPen(QtGui.QColor("#000000"))
            painter.setPen(pen)
            painter.setFont(painter.font())
            align_right = Qt.AlignRight
            painter.drawText(0, position.y(), self.width()-6, 30,
                             align_right, str(line_number))
                             
            
            block = block.next()
            line_number += 1
            
        painter.end()
                
    def sizeHint(self):
        return QSize(50, 0)
    
    def eventFilter(self, object, event):
        # Update the line numbers for all events on the text edit and the viewport.
        # This is easier than connecting all necessary singals.
        self.update()
        return False
