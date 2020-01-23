import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic  import loadUi

"""
SPECIAL NOTE:

Use the QAbstractItemViewer in the QT Designer 
to set the drag and drop properties of the QlistsWidgets

"""


class main(QDialog):
    def __init__(self):
        super(main, self).__init__()
        loadUi('gui.ui', self)

        for i in range(10):
            self.list1.insertItem(i, str(i))

        self.btn_print.clicked.connect(self.show_list)
        self.btn_clear.clicked.connect(self.clear_list2)
        self.btn_remove.clicked.connect(self.remove_selected)

    def show_list(self):
        for index in range(self.list2.count()):
            i = self.list2.item(index).text()
            self.cmb1.addItem(i)

    def clear_list2(self):
        self.list2.clear()

    def remove_selected(self):
        item = self.list2.selectedItems()
        if item != []:
            for i in item:
                self.list2.takeItem(self.list2.row(i))



app = QApplication(sys.argv)
window = main()
window.show()
app.exit(app.exec_())