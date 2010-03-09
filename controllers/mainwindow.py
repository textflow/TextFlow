from models.document import Document

class MainWindowController(object):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.documents = []
        
    def new(self):
        document = Document()
        self.documents.append(document)
        
        return document
        
    

