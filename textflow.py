from PySide import QtGui
import sys
from controllers.mainwindow import MainWindowController

def main(argv):
    application = QtGui.QApplication(argv)
    
    main_window = MainWindowController()
    main_window.show_view()
    
    sys.exit(application.exec_())

if __name__ == '__main__':
    main(sys.argv)