from PyQt4 import QtGui
from PyQt4.QtCore import QSize, Qt
from controllers.texteditor import TextEditorController

import math

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
    #TODO
    # 1 - auto resize (x)
    # 2 - melhor mais o desempenho (fazer o for apenas entre as linhas que aparecerao) (x)
    # 3 - refactoring
    # 4 - bug com blocos com mais de uma linha
    
    def __init__(self, text_editor, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.text_editor = text_editor
        self.text_editor.installEventFilter(self)
        self.back_brush = QtGui.QBrush(QtGui.QColor("#d8e0f9"))
    
    def paintEvent(self, event):
        # paint background
        
        painter = QtGui.QPainter(self)
        painter.fillRect(event.rect(), self.back_brush)
        
        document = self.text_editor.document()        
        
        contents_y = self.text_editor.verticalScrollBar().value()
        text_editor_height = self.text_editor.height()
        line_height = document.documentLayout().blockBoundingRect(document.firstBlock()).height()
        
        top_line = int(math.ceil(contents_y / line_height))
        total_lines = int((text_editor_height / line_height))
        
        
        pen = QtGui.QPen(QtGui.QColor("#000000"))
        painter.setPen(pen)
        painter.setFont(painter.font())

        
        if document.blockCount() < total_lines:
            end_range_line = document.blockCount()
        else:
            end_range_line = top_line + total_lines
        
        
        for line in range(max(1, top_line), end_range_line + 2):
            
            if not line in range(1, document.blockCount() + 1):
                continue
            
            block = document.findBlockByNumber(line - 1)
            position = document.documentLayout().blockBoundingRect(block).topLeft()
#            
            painter.drawText(self.width() - self.fontMetrics().width(str(line)) - 6, position.y() - contents_y + self.fontMetrics().ascent(), str(line))
        
        painter.end()
                
    
    def update(self, *args):
        document = self.text_editor.document()
        width = self.fontMetrics().width(str(document.blockCount())) + 12
        
        if self.width() != width:
            self.setFixedWidth(width)
            
        QtGui.QWidget.update(self, *args)
    
    def eventFilter(self, object, event):
        # Update the line numbers for all events on the text edit and the viewport.
        # This is easier than connecting all necessary singals.
        self.update()
        return False
