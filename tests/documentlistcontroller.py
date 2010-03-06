import unittest
from PyQt4 import QtGui

from models.document import Document
from controllers.documentlist import DocumentListController

class DocumentListControllerTest(unittest.TestCase):

    def add_dict_test(self):
        controller = DocumentListController()
        document = Document()
        
        controller.add(document)
        
        self.assertEquals(document, controller.association.values()[0])
        self.assertTrue(type(controller.association.keys()[0]) == QtGui.QStandardItem)
        
    def add_item_name_test(self):
        controller = DocumentListController()
        document = Document()
        document.path = "/path/to/test.tf"
        
        
        controller.add(document)
        item = controller.association.keys()[0]
        
        self.assertEquals("test.tf", item.text())
        
        
    def add_item_name2_test(self):
        controller = DocumentListController()
        
        document = Document()
        document.path = "/path/to/othertest.tf"
        
        controller.add(document)
        item = controller.association.keys()[0]
        
        self.assertEquals("othertest.tf", item.text())
