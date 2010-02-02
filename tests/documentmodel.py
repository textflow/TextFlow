import unittest
import os

from models.document import Document

class DocumentModelTest(unittest.TestCase):
    
    def tearDown(self):
        test_filepath =  os.path.join(os.getcwd(), "test_file")
        if os.path.exists(test_filepath):
            os.remove(test_filepath)
    
    def test_init_parameters(self):
        document = Document()
        self.assertEquals("", document.text)
        self.assertEquals(None, document.path)
        
    def test_open_blank_file(self):
        document = Document()
        text_file = open("test_file", "w")
        text_file.close()
        document.open("test_file")
        
        self.assertEquals("test_file", document.path)
        self.assertEquals("", document.text)
        
    def test_open_text_file(self):
        document = Document()
        text_file = open("test_file", "w")
        text_file.write("this is only a test")
        text_file.close()
        document.open("test_file")
        
        self.assertEquals("test_file", document.path)
        self.assertEquals("this is only a test", document.text)
        
    def test_open_inexistent_file(self):
        document = Document()
        self.assertRaises(IOError, document.open, "test_file")
        
    def test_save_inexistent_file(self):
        document = Document()
        document.text = "this is only a test of save file"
        document.path = "test_file"
        
        document.save()
        
        self.assertTrue(os.path.exists(document.path))
        self.assertEquals("this is only a test of save file", document.text)
        
    def test_save_no_defined_path(self):
        document = Document() # document.path is None
        self.assertRaises(IOError, document.save)
    
    def test_text_save_file(self):
        document = Document()
        document.text = "this is only a test of save file"
        document.path = "test_file"
        
        document.save()
        
        text_file = open(document.path, "r")
        self.assertEquals(document.text, text_file.read())
        
    def test_replace_text_save_file(self):
        text_file = open("test_file", "w")
        text_file.write("this is only a test file")
        text_file.close()
        
        document = Document()
        document.text = "I changed the text"
        document.path = "test_file"
        
        document.save()
        
        text_file = open ("test_file", "r")
        self.assertEquals(document.text, text_file.read())
        
