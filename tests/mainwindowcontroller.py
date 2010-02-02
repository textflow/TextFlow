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
        
        success, document = mainwindow_controller.open("test_file")
        
        self.assertTrue(success)
        self.assertEquals("test_file", document.path)
        
    def test_open_nonexistent_file(self):
        mainwindow_controller = MainWindowController()
        
        success, document = mainwindow_controller.open("afilethatnoexists")
        
        self.assertFalse(success)
        
    def test_content_save_existent_file(self):
        mainwindow_controller = MainWindowController()
        
        text_file = open("test_file", "w")
        text_file.close()
        
        mainwindow_controller.document.path = "test_file"
        save_status = mainwindow_controller.save("this is a test file")
        
        text_file = open("test_file", "r")
        text_file_content = text_file.read()
        text_file.close()
        
        self.assertEquals("ok", save_status)
        self.assertEquals("this is a test file", text_file_content)
        
    def test_save_inexistent_file(self):
        mainwindow_controller = MainWindowController()
        save_status = mainwindow_controller.save("this is a test file")

        self.assertEquals("fail", save_status)
        
    def test_create_save_as_file(self):
        mainwindow_controller = MainWindowController()
        save_status = mainwindow_controller.save("this is a test file", "test_file")
        
        self.assertEquals("ok", save_status)
        self.assertTrue(os.path.exists("test_file"))
        
    def test_content_save_as_file(self):
        mainwindow_controller = MainWindowController()
        
        save_status = mainwindow_controller.save("this is a test file", "test_file")
        
        text_file = open("test_file", "r")
        text_file_content = text_file.read()
        text_file.close()
        
        self.assertEquals("ok", save_status)
        self.assertEquals("this is a test file", text_file_content)
