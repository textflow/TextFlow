from models.document import Document

class TextEditorController(object):
        
    def __init__(self):
        self.document = Document()
        
    def open(self, path):
        try:
            self.document.open(path)
        except IOError:
            success = False
        else:
            success = True
        
        return success, self.document
        
    def save(self, text, path=None):
        self.document.text = text
        
        if path is not None:
            self.document.path = path
        
        try:
            self.document.save()
        except IOError:
            return False
        else:
            return True
