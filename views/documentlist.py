from PyQt4 import QtGui, QtCore

from controllers.documentlist import DocumentListController

class DocumentList(QtGui.QTreeView):
    def __init__(self, parent):
        super(DocumentList, self).__init__(parent)
        self.setFrameShape(QtGui.QFrame.NoFrame)
        self.setFrameShadow(QtGui.QFrame.Plain)
        self.setHeaderHidden(True)
        self.setIndentation(0)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setItemDelegate(LineStyleDelegate())
        
        self.controller = DocumentListController()
        self.model = QtGui.QStandardItemModel()
        self.setModel(self.model)
        
        QtCore.QObject.connect(self.selectionModel(), QtCore.SIGNAL("selectionChanged(QItemSelection, QItemSelection)"), self.select)
        
        QtCore.QObject.connect(self, QtCore.SIGNAL("clicked(QModelIndex)"), self.clicked)
    
    def add(self, editor):
        document = editor.controller.document
        item = self.controller.add(document)
        item.setEditable(False)
        
        icon_item = QtGui.QStandardItem()
        icon_item.setEditable(False)
        icon = QtGui.QIcon("ui/close.png")
        icon_item.setData(icon, QtCore.Qt.DecorationRole)
        icon_item.setIcon(icon)
        
        row_count = self.model.rowCount()
        self.model.setItem(row_count, 0, item)
        self.model.setItem(row_count, 1, icon_item)
        
        self.select_document(document)

    def remove(self, document):
        item = self.controller.remove(document)
        index = self.model.indexFromItem(item)
        self.model.removeRow(index.row())
        
    def select_document(self, document):
        item = self.controller.get_item_from_document(document)
        index = self.model.indexFromItem(item)
        self.setCurrentIndex(index)
        
    def update(self, document):
        self.controller.change_filename(document, str(document.path))

    ### Callbacks ###
    
    def select(self, selected, deselected):
        if len(selected.indexes()) == 0:
            return
            
        row_index = selected.indexes()[0].row()
        item = self.model.item(row_index)
        document = self.controller.association[item]
        
        self.emit(QtCore.SIGNAL("selection_changed"), document)
        
    def clicked(self, index):
        item = self.model.itemFromIndex(index)
        row = index.row()
        first_col_item = self.model.item(row, 0)
        
        #detecting de click position to get only the icon.
        #the close icon column minimum possible size is bigger
        #than the close icon, so we need this workaround to get
        #the click only in the icon.
        cursor_pos = self.mapFromGlobal(QtGui.QCursor.pos())
        
        icon_size = 15
        icon_x = self.visualRect(index).x() + self.columnWidth(1) - icon_size
        if item.column() == 1:
            cell_rect = self.visualRect(index)
            if cursor_pos.x() >= icon_x and \
               cursor_pos.x() < icon_x + icon_size:
               document = self.controller.association[first_col_item] 
               self.emit(QtCore.SIGNAL("close"), document)
               self.remove(document)
        
        
    def resizeEvent(self, event):
        close_icon_width = 27
        self.setColumnWidth(0, self.width() - close_icon_width)
        self.setColumnWidth(1, close_icon_width)

class LineStyleDelegate(QtGui.QStyledItemDelegate):

    def __init__(self, parent = None):
        QtGui.QItemDelegate.__init__(self, parent)

    def paint(self, painter, option, index):
        data = index.model().data(index, QtCore.Qt.DecorationRole)
        rect = option.rect
        
        if data.isValid():
            painter.save()
            
            #workaround to fix the selection background problem.
            options = QtGui.QStyleOptionViewItemV4(option)
            options.widget.style().drawControl(QtGui.QStyle.CE_ItemViewItem, options, painter)
            
            painter.drawImage(QtCore.QRect(rect.left()+11, rect.top()+3, 12, 12),
                              QtGui.QImage("ui/close.png"));
            painter.restore()

        else:
            QtGui.QStyledItemDelegate.paint(self, painter, option, index)
