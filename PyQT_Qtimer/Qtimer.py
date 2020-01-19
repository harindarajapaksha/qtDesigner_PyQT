import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi

class main(QDialog):
    def __init__(self):
        super(main, self).__init__()
        loadUi('gui.ui', self)
        self.btn_run.clicked.connect(self.runtimer)

    def runtimer(self):
        self.my_timer = QTimer()
        self.my_timer.timeout.connect(self.change_txt)
        self.my_timer.start(5000) # time is in microseconds

    def change_txt(self):
        self.label.setText("This is after 5 seconds")


app = QApplication(sys.argv)
window = main()
window.show()
app.exit(app.exec_())