import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUi

class main(QDialog):
    def __init__(self):
        super(main, self).__init__()
        loadUi('gui.ui', self)
        self.btn_run.clicked.connect(self.rungif)

    def rungif(self):
        self.gif = QMovie('gear.gif')
        self.label.setMovie(self.gif)
        self.gif.start()


app = QApplication(sys.argv)
window = main()
window.show()
app.exit(app.exec_())