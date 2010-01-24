class Document(object):
    def __init__(self):
        super(Document, self).__init__()
        self.text = ""
        self.path = ""
    
    def open(self, path):
        text_file = open(path, "r")
        self.text = text_file.read()
        self.path = path
    
    def save(self):
        if self.path:
            document = open(self.path, 'w')
            document.write(self.text)
    
