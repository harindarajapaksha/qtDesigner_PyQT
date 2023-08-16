import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from GUI import Ui_MainWindow

class file(QMainWindow):
    def __init__(self):
        super(file, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_file.clicked.connect(self.browser)

    def browser(self):
        fname = QFileDialog.getOpenFileNames(self, "open file", ".", "Python files (*.py)")
        self.ui.txt_file.setText(fname[0][0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = file()
    window.show()
    sys.exit(app.exec_())