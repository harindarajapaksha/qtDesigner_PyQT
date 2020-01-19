from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import sys
from PyQt5.QtCore import QThread, pyqtSignal
import time




class mythread(QThread):
    value_return = pyqtSignal(int)

# run is a function available in the Qthread library. Here we are over riding it.
    def run(self):
        c = 0
        while True:
            if c <100:
                self.value_return.emit(c)
                time.sleep(0.01)
                c +=1
            else:
                c = 0
                self.value_return.emit(c)
                time.sleep(0.3)


class main(QDialog):
    def __init__(self):
        super(main, self).__init__()
        loadUi('gui.ui', self)
        self.btn_run.clicked.connect(self.runpgbar)

    def runpgbar(self):
        self.thread = mythread()
        self.thread.value_return.connect(self.pgbarset)
        self.thread.start()

    def pgbarset(self, val):
        self.pgbar.setValue(val)


app = QApplication(sys.argv)
window = main()
window.show()
app.exit(app.exec_())
