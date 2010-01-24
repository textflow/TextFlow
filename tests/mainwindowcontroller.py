import unittest
import sys
from PySide import QtGui

from controllers.mainwindow import MainWindowController

class DocumentModelTest(unittest.TestCase):
    
    def test_open_existent_file(self):
        mainwindow_controller = MainWindowController()
        
        text_file = open("test_file", "w")
        text_file.close()
        
        open_status, document = mainwindow_controller.open("test_file")
        
        self.assertEquals("ok", open_status)
        self.assertEquals("test_file", document.path)
        self.assertEquals("", document.text)
        
    def test_open_nonexistent_file(self):
        mainwindow_controller = MainWindowController()
        
        open_status, document = mainwindow_controller.open("afilethatnoexists")
        
        self.assertEquals("fail", open_status)
        self.assertEquals("", document.path)
        self.assertEquals("", document.text)        
        
