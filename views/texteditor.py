from PyQt4 import QtGui
from PyQt4.QtCore import QSize, Qt
from controllers.texteditor import TextEditorController

import math

class TFEditor(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.text_area = TextEditor(parent)
        
        self.line_numbers = LineNumbers(self.text_area, parent)
        self.controller = self.text_area.controller
        
        hbox = QtGui.QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        hbox.setSpacing(0)
        hbox.addWidget(self.line_numbers)
        hbox.addWidget(self.text_area)
        self.setLayout(hbox)
        
    def get_text(self):
        return self.text_area.toPlainText()
        
    def set_text(self, text):
        self.text_area.setPlainText(text)
        

class TextEditor(QtGui.QTextEdit):
    """
    Text editor view.
    """    
    
    def __init__(self, parent):
        super(TextEditor, self).__init__(parent)
        self.controller = TextEditorController()
        
        self.setAcceptDrops(True)
        self.setFrameShape(QtGui.QFrame.NoFrame)
        self.setFrameShadow(QtGui.QFrame.Plain)
        
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
        self.back_color = QtGui.QColor("#d8e0f9")
        self.text_color = QtGui.QColor("#000000") 
    
    def paintEvent(self, event):
        # getting important data
        document = self.text_editor.document() 
        contents_y = self.text_editor.verticalScrollBar().value()
        text_editor_height = self.text_editor.height()
        line_height = self.fontMetrics().height()
        visible_lines_number = self.__get_visible_lines_number()
        top_line = self.__get_visible_top_line()
        layout = document.documentLayout()
        
        # pen settings
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen(self.text_color)
        painter.setPen(pen)
        painter.setFont(painter.font())
        
        # paint background
        painter.fillRect(event.rect(), QtGui.QBrush(self.back_color))
            
        # get the end range to write the numbers
        if document.blockCount() < visible_lines_number:
            end_range_line = document.blockCount()
        else:
            end_range_line = top_line + visible_lines_number - 1
        
        # write the numbers
        for line in xrange(max(1, top_line), min(end_range_line + 1, document.blockCount() + 1)):
            
            block = document.findBlockByNumber(line - 1)
            position = layout.blockBoundingRect(block).topLeft()
            
            painter.drawText(self.width() - self.fontMetrics().width(str(line)) - 6, position.y() - contents_y + self.fontMetrics().ascent(), str(line))
        
        
        painter.end()
                
    
    def update(self, *args):
        document = self.text_editor.document()
        width = self.fontMetrics().width(str(document.blockCount())) + 12
        
        if self.width() != width:
            self.setFixedWidth(width)
            
        QtGui.QWidget.update(self, *args)
    
    def eventFilter(self, object, event):
        self.update()
        return False

    def __get_visible_lines_number(self):
        text_editor_height = self.text_editor.height()
        line_height = self.fontMetrics().height()
        
        return int(math.ceil((text_editor_height / float(line_height))))
    
    def __get_visible_top_line(self):
        document = self.text_editor.document()
        contents_y = self.text_editor.verticalScrollBar().value()
        line_height = self.fontMetrics().height()
        
        guess_top_line = min(int(math.ceil(contents_y / line_height)) + 1, document.blockCount())
        
        block = document.findBlockByNumber(guess_top_line -1)
        position = document.documentLayout().blockBoundingRect(block).topLeft()
        guess_top_line
        
        while (guess_top_line > 1) and (position.y() >= contents_y):
            guess_top_line -= 1
            block = document.findBlockByNumber(guess_top_line -1)
            position = document.documentLayout().blockBoundingRect(block).topLeft()
        
        return guess_top_line
