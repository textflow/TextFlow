class Document(object):
    def __init__(self):
        self.text = ""
        self.path = None
    
    def open(self, path):
        text_file = open(path, "r")
        self.text = text_file.read()
        self.path = path
    
    def save(self):
        if self.path is None:
            raise IOError
        else:
            text_file = open(self.path, "w")
            text_file.write(self.text)
