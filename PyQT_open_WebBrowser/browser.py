import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(531, 114)
        self.btn_url = QtWidgets.QPushButton(Dialog)
        self.btn_url.setGeometry(QtCore.QRect(410, 40, 90, 28))
        self.btn_url.setObjectName("btn_url")
        self.txt_url = QtWidgets.QLineEdit(Dialog)
        self.txt_url.setGeometry(QtCore.QRect(20, 40, 381, 28))
        self.txt_url.setObjectName("txt_url")
        self.txt_url.setText("Type your URL here ...")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btn_url.clicked.connect(self.go_url)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_url.setText(_translate("Dialog", "&Go"))

    def go_url(self):
        myurl = self.txt_url.text()
        webbrowser.open(myurl)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
