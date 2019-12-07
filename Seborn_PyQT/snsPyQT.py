import sys
import pandas as pd
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib import pylab as plb

from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout
from PyQt5.uic import loadUi


class Mywindow(QDialog):
    def __init__(self):
        super(Mywindow, self).__init__()
        loadUi('GUI.ui', self)
        self.btn_exit.clicked.connect(self.exitapp)
        self.btn_plot.clicked.connect(self.plotting)

    def exitapp(self):
        sys.exit()

    def plotting(self):
        df = pd.read_csv(filepath_or_buffer="Sample_file.txt", sep="\t")
        figure, ax = plb.subplots()
        sns.violinplot(x='cyl', y='mpg', data=df, hue='gear')

        self.myplot = FigureCanvas(figure)
        layout = QVBoxLayout(self.pltWidget)
        layout.addWidget(self.myplot)



application = QApplication(sys.argv)
window = Mywindow()
window.show()
application.exit(application.exec_())
