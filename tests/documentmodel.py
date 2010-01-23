import unittest

from models.document import Document

class DocumentModelTest(unittest.TestCase):
    
    def test_init_parameters(self):
        document = Document()
        self.assertEquals("", document.text)
        self.assertEquals("", document.path)
