from PyQt4 import QtGui, QtCore
from ui.mainwindow import Ui_MainWindow
from controllers.mainwindow import MainWindowController
from views.texteditor import TFEditor
from views.documentlist import DocumentList

class MainWindowView(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        self.setupUi(self)

        self.editor_stack = QtGui.QStackedWidget()
        self.splitter = QtGui.QSplitter(self)
        self.list_view = DocumentList(self)
        self.new()
        
        self.splitter.addWidget(self.list_view)
        self.splitter.addWidget(self.editor_stack)
        self.splitter.setSizes((self.width()/3.0, 2*self.width()/3.0))
        
        self.horizontalLayout.addWidget(self.splitter)
        
        self.controller = MainWindowController()
        
        self.__connect_signals()
        
    def __connect_signals(self):
        QtCore.QObject.connect(self.actionNew_2, QtCore.SIGNAL("triggered()"), self.new)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL("triggered()"), self.open_menu_clicked)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL("triggered()"), self.save_menu_clicked)
        QtCore.QObject.connect(self.actionSave_As, QtCore.SIGNAL("triggered()"), self.save_as_menu_clicked)
        
        QtCore.QObject.connect(self.list_view, QtCore.SIGNAL("selection_changed"), self.listview_select)
        
        QtCore.QObject.connect(self.list_view, QtCore.SIGNAL("close"), self.listview_close)
    

    def new(self, filepath=None):
        new_editor = TFEditor(self.centralwidget)
        self.editor_stack.addWidget(new_editor)
        self.editor_stack.setCurrentWidget(new_editor)
        editor = self.editor_stack.currentWidget()
        
        if filepath is not None:
            self._open(editor, filepath)
        
        self.list_view.add(editor)
        
        return new_editor
    
    def save(self, document, filepath=None):
        editor = self._get_editor_from_document(document)
        success = editor.controller.save(editor.get_text(), filepath)
        
        if not success:
            filepath = QtGui.QFileDialog.getSaveFileName()
            
            if filepath:
                editor.controller.save(editor.get_text(), filepath)
        
        self.list_view.update(document)

    def close(self, document):
        editor = self._get_editor_from_document(document)
        self.editor_stack.removeWidget(editor)
        editor.destroy()
        
        if self.editor_stack.count() == 0:
            new_editor = self.new()

    def _open(self, editor, filepath):
        success, document = editor.controller.open(filepath)
        
        if success:
            editor.set_text(document.text)
        else:
            QtGui.QMessageBox.critical(self, "Error",
                                       "The file <b>%s</b> doesn't exists." % 
                                           filepath, QtGui.QMessageBox.Ok)
        return editor

    
    def _change_to_editor(self, editor):
        self.editor_stack.setCurrentWidget(editor)
        
    def _get_editor_from_document(self, document):
        selected_editor = None
        
        for editor_index in range(self.editor_stack.count()):
            editor = self.editor_stack.widget(editor_index) 
            if editor.controller.document == document:
                selected_editor = editor
        
        return selected_editor


    ### Callbacks ###
        
    def listview_select(self, document):
        editor = self._get_editor_from_document(document)
        self._change_to_editor(editor)
        
    def listview_close(self, document):
        self.close(document)        
        
    def open_menu_clicked(self):
        filepath = QtGui.QFileDialog.getOpenFileName()
        self.new(str(filepath))
                                       
    def save_menu_clicked(self):
        self.save(self.editor_stack.currentWidget().controller.document)
            
    def save_as_menu_clicked(self):
        filepath = QtGui.QFileDialog.getSaveFileName()
        
        if filepath:
            self.save(self.editor_stack.currentWidget().controller.document, filepath)            
