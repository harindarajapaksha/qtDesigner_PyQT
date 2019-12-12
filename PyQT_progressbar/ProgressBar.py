import sys
import time
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('gui.ui', self)
        self.btn_exit.clicked.connect(self.close)
        self.btn_go.clicked.connect(self.progress)

    def progress(self):
        maxpgBar = self.pgBar.maximum() + 1
        for i in range(maxpgBar):
            self.pgBar.setValue(i)
            time.sleep(1)

app = QApplication(sys.argv)
window = Main()
window.show()
app.exit(app.exec_())