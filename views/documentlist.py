from PyQt4 import QtGui

class DocumentList(QtGui.QListView):
    def __init__(self, parent):
        super(DocumentList, self).__init__(parent)
        self.setFrameShape(QtGui.QFrame.NoFrame)
        self.setFrameShadow(QtGui.QFrame.Plain)
        
        self.model = QtGui.QStandardItemModel()
        self.setModel(self.model)
        
        #TODEL
        item = QtGui.QStandardItem("opa")
        item2 = QtGui.QStandardItem("awesome")
        item3 = QtGui.QStandardItem("cool")
        self.model.appendRow(item)
        self.model.appendRow(item2)
        self.model.appendRow(item3)
        
        print type(item)

