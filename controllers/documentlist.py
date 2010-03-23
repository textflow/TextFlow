import os
from PyQt4 import QtGui

class DocumentListController(object):

    def __init__(self):
        self.association = {}

    def add(self, document):
        if document.path is None:
            text = "New File"
        else:
            text = os.path.basename(document.path)
            
        item = QtGui.QStandardItem(text)
        self.association[item] = document
        
        return item
        
    def remove(self, document):
        for item in self.association.items():
            if document in item:
                self.association.pop(item[0])
                return item[0]
                
    def get_item_from_document(self, document):
        for item in self.association.items():
            if document in item:
                return item[0]
                
    def change_filename(self, document, new_filepath):
        item = self.get_item_from_document(document)
        item.setText(os.path.basename(new_filepath))
