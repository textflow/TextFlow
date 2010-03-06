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
