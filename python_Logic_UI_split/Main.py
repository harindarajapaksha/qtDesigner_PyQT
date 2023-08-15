import sys
from GUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


class simpleGUI(QMainWindow):
    def __init__(self):
        super(simpleGUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the ui object with the function
        self.ui.btn_exit.clicked.connect(self.my_exit)

    def my_exit(self):
        sys.exit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = simpleGUI()
    window.show()
    sys.exit(app.exec_())

