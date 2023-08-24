from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow
from w1 import Ui_Dialog
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 164)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 90, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 50, 90, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "&Exit"))
        self.pushButton_2.setText(_translate("MainWindow", "&Window"))

class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class win(QDialog):
    def __init__(self):
        super(win, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class manager():
    def __init__(self):
        self.first = main()
        self.second = win()
        self.first.ui.pushButton_2.clicked.connect(self.show_win2)
        self.first.ui.pushButton.clicked.connect(self.myexit)

    def show_win2(self):
        self.second.show()

    def myexit(self):
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = manager()
    w.first.show()
    app.exit(app.exec_())
