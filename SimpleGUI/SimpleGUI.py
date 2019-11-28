import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class SimpleGUI(QDialog):
    def __init__(self):
        super(SimpleGUI, self).__init__()
        loadUi('SimpleGUI/simpleGUI.ui', self)
        self.btn_exit.clicked.connect(self.click_exit)
        self.btn_cal.clicked.connect(self.calculate)

    def calculate(self):
        val1 = int(self.txt1.text())
        val2 = int(self.txt2.text())
        self.lbl_out.setText(str(val1+val2))

    def click_exit(self):
        sys.exit()


application = QApplication(sys.argv)
window = SimpleGUI()
window.show()
application.exit(application.exec_())