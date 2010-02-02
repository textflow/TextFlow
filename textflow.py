import sys
from PySide import QtGui

from views.mainwindow import MainWindowView

def main(argv):
    application = QtGui.QApplication(argv)
    
    main_window = MainWindowView()
    main_window.show()
    
    sys.exit(application.exec_())

if __name__ == '__main__':
    main(sys.argv)
