from views.mainwindow import MainWindowView

class MainWindowController(object):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.view = MainWindowView()
    
    def show_view(self):
        self.view.show()