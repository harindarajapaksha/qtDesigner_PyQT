import sys
from GUI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class slide(QMainWindow):
    def __init__(self):
        super(slide, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.slider.valueChanged.connect(self.set_lbl)

    def set_lbl(self):
        val = self.ui.slider.value()
        self.ui.lbl_out.setText(str(val))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = slide()
    w.show()
    sys.exit(app.exec_())

    