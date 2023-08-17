import sys
from GUI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class checkbox(QMainWindow):
    def __init__(self):
        super(checkbox, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.check_test.clicked.connect(self.set_out)

    def set_out(self):
        if self.ui.check_test.isChecked() == True:
            self.ui.lbl_out.setText("Checked")
        else:
            self.ui.lbl_out.setText("Not Checked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = checkbox()
    window.show()
    sys.exit(app.exec_())
