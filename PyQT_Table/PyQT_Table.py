import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QTableWidgetItem
from PyQt5.uic import loadUi


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        loadUi('GUI.ui', self)
        self.btn_exit.clicked.connect(self.cliecked_exit)
        self.btn_load.clicked.connect(self.loadTable)

    def loadTable(self):
        df = pd.read_csv(QFileDialog.getOpenFileName()[0], sep='\t')
        self.table.setColumnCount(len(list(df)))
        self.table.setHorizontalHeaderLabels(list(df))

        for rowNumber, rowData in df.iterrows():
            self.table.insertRow(rowNumber)
            for colNumber, cellData in enumerate(rowData):
                self.table.setItem(rowNumber, colNumber, QTableWidgetItem(str(cellData)))

    def cliecked_exit(self):
        sys.exit()


application = QApplication(sys.argv)
Main = Window()
Main.show()
application.exit(application.exec_())
