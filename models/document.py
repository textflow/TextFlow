class Document(object):
    def __init__(self):
        super(Document, self).__init__()
        self.text = ""
        self.path = ""
    
    def open(self):
        if self.path:
            document = open(self.path, 'r')
            self.text = document.read()
    
    def save(self):
        if self.path:
            document = open(self.path, 'w')
            document.write(self.text)
    
