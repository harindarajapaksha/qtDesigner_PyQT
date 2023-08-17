import sys
from a import Ui_MainWindow_a
from b import Ui_MainWindow_b
from PyQt5.QtWidgets import QApplication, QMainWindow

class first(QMainWindow):
    def __init__(self):
        super(first, self).__init__()
        self.uia = Ui_MainWindow_a()
        self.uia.setupUi(self)

class second(QMainWindow):
    def __init__(self):
        super(second, self).__init__()
        self.uib = Ui_MainWindow_b()
        self.uib.setupUi(self)

class manager():
    def __init__(self):
        self.first = first()
        self.second = second()
        self.first.uia.btn_window.clicked.connect(self.my_window)
        self.second.uib.btn_exit.clicked.connect(self.myexit)


    def my_window(self):
        self.second.show()

    def myexit(self):
        self.second.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = manager()
    w.first.show()
    app.exit(app.exec_())






