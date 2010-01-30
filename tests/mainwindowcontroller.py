import unittest
import sys
import os
from PySide import QtGui

from controllers.mainwindow import MainWindowController

class DocumentModelTest(unittest.TestCase):
    
    def tearDown(self):
        test_filepath =  os.path.join(os.getcwd(), "test_file")
        if os.path.exists(test_filepath):
            os.remove(test_filepath)
    
    def test_open_existent_file(self):
        mainwindow_controller = MainWindowController()
        
        text_file = open("test_file", "w")
        text_file.close()
        
        open_status, document = mainwindow_controller.open("test_file")
        
        self.assertEquals("ok", open_status)
        self.assertEquals("test_file", document.path)
        
    def test_open_nonexistent_file(self):
        mainwindow_controller = MainWindowController()
        
        open_status, document = mainwindow_controller.open("afilethatnoexists")
        
        self.assertEquals("fail", open_status)
        
