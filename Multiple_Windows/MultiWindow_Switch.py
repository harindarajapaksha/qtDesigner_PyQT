import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi

class First(QWidget):
    def __init__(self):
        super(First, self).__init__()
        loadUi('1.ui', self)
        self.btn_1.clicked.connect(self.hide)

class Second(QWidget):
    def __init__(self):
        super(Second, self).__init__()
        loadUi('2.ui', self)
        self.btn_2.clicked.connect(self.hide)

class Thired(QWidget):
    def __init__(self):
        super(Thired, self).__init__()
        loadUi('3.ui', self)
        self.btn_back.clicked.connect(self.hide)


class Manager():
    def __init__(self):
        self.first = First()
        self.second = Second()
        self.Third = Thired()

        self.first.btn_1.clicked.connect(self.second.show)
        self.second.btn_2.clicked.connect(self.Third.show)
        self.Third.btn_back.clicked.connect(self.second.show)
        self.Third.btn_exit.clicked.connect(self.first.show)
        self.Third.btn_exit.clicked.connect(self.Third.hide)

        self.first.show()

app = QApplication(sys.argv)
window = Manager()
app.exit(app.exec_())