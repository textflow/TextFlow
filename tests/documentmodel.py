import unittest

from models.document import Document

class DocumentModelTest(unittest.TestCase):
    
    def test_init_parameters(self):
        document = Document()
        self.assertEquals("", document.text)
        self.assertEquals("", document.path)
        
    def test_open_blank_file(self):
        document = Document()
        text_file = open("test_file", "w")
        text_file.close()
        document.open("test_file")
        
        self.assertEquals("test_file", document.path)
        
    def test_open_text_file(self):
        document = Document()
        text_file = open("test_file", "w")
        text_file.write("this is only a test")
        text_file.close()
        document.open("test_file")
        
        self.assertEquals("test_file", document.path)
        self.assertEquals("this is only a test", document.text)
        
