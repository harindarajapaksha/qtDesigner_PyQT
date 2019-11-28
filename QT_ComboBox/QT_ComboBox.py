import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class ComboBox(QDialog):
    def __init__(self):
        super(ComboBox, self).__init__()
        loadUi('ComboBox.ui', self)
        for i in range(10):
            self.cmb1.addItem(str(i))
        self.btn_update.clicked.connect(self.update_lbl)
        self.btn_exit.clicked.connect(self.click_exit)

    def update_lbl(self):
        self.lbl_out.setText(self.cmb1.currentText())

    def click_exit(self):
        sys.exit()

application = QApplication(sys.argv)
window = ComboBox()
window.show()
application.exit(application.exec_())