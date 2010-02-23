import unittest
import sys
import os
from PySide import QtGui

from controllers.texteditor import TextEditorController

class DocumentModelTest(unittest.TestCase):
    
    def setUp(self):
        self.texteditor_controller = TextEditorController()
    
    def tearDown(self):
        test_filepath =  os.path.join(os.getcwd(), "test_file")
        if os.path.exists(test_filepath):
            os.remove(test_filepath)
    
    def test_open_existent_file(self):
        text_file = open("test_file", "w")
        text_file.close()
        
        success, document = self.texteditor_controller.open("test_file")
        
        self.assertTrue(success)
        self.assertEquals("test_file", document.path)
        
    def test_open_nonexistent_file(self):
        success, document = self.texteditor_controller.open("afilethatnoexists")
        self.assertFalse(success)
        
    def test_content_save_existent_file(self):
        text_file = open("test_file", "w")
        text_file.close()
        
        success = self.texteditor_controller.save("this is a test file", "test_file")
        
        text_file = open("test_file", "r")
        text_file_content = text_file.read()
        text_file.close()
        
        self.assertTrue(success)
        self.assertEquals("this is a test file", text_file_content)
        
    def test_save_inexistent_file(self):
        #path isn't defined
        success = self.texteditor_controller.save("this is a test file")

        self.assertFalse(success)
        
    def test_create_save_as_file(self):
        save_status = self.texteditor_controller.save("this is a test file", "test_file")
        
        self.assertTrue(save_status)
        self.assertTrue(os.path.exists("test_file"))
        self.assertEquals("test_file", self.texteditor_controller.document.path)
        
    def test_content_save_as_file(self):
        success = self.texteditor_controller.save("this is a test file", "test_file")
        
        text_file = open("test_file", "r")
        text_file_content = text_file.read()
        text_file.close()
        
        self.assertTrue(success)
        self.assertEquals("this is a test file", text_file_content)
        self.assertEquals("this is a test file", self.texteditor_controller.document.text)
