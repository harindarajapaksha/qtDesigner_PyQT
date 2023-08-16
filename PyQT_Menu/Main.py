import sys
from GUI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class gui(QMainWindow):
    def __init__(self):
        super(gui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_Exit.triggered.connect(self.my_exit)
        self.ui.action_Add.triggered.connect(self.add)

    def my_exit(self):
        sys.exit()

    def add(self):
        val1 = int(self.ui.lineEdit.text())
        val2 = int(self.ui.lineEdit_2.text())
        val3 = val1 + val2
        self.ui.label_3.setText(str(val3))


if __name__ == '__main__':
    app =QApplication(sys.argv)
    w = gui()
    w.show()
    sys.exit(app.exec_())