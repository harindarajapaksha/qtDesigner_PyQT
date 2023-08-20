import sys
from gui import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog

class test(QDialog):
    def __init__(self):
        super(test, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btn_ok.clicked.connect(self.setcombo)
        self.ui.combo_list.currentIndexChanged.connect(self.updatelbl)

    def setcombo(self):
        val = self.ui.txt_input.text()
        self.ui.combo_list.addItem(val)

    def updatelbl(self):
        val = self.ui.combo_list.currentText()
        self.ui.lbl_val.setText(val)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = test()
    w.show()
    sys.exit(app.exec_())

    