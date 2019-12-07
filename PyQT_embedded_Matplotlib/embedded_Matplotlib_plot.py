import sys
import venn
from matplotlib import pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas

from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout
from PyQt5.uic import loadUi

class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        loadUi('myGUI.ui', self)
        self.btn_plot.clicked.connect(self.myplot)
        self.btn_exit.clicked.connect(self.clicked_exit)
        self.btn_2.clicked.connect(self.myplot2)


    def myplot(self):
        xdata = [1,2,3,4,5,6,7,8,9,10]
        ydata = [12,34,23,12,34,56,78,90,45,23]

        figure, ax = plt.subplots()
        ax.plot(xdata, ydata)

        self.mlp = FigureCanvas(figure)
        layout = QHBoxLayout(self.widget)
        layout.addWidget(self.mlp)


    def myplot2(self):
        a = set([1,2,3,4,5,6,7,8,9])
        b = set([3,4,3,4,5,6,7,8,9])
        c = set([12,4,5,4,34,6,7,67,8,5])


        lables = venn.get_labels([a,b,c], fill=['number'])
        fig, ax2 = venn.venn3(lables, names=['list 1', 'list 2', 'list 3'])


        self.mlp2 = FigureCanvas(fig)
        lay = QHBoxLayout(self.widget_2)
        lay.addWidget(self.mlp2)

    def clicked_exit(self):
        sys.exit()


application = QApplication(sys.argv)
widget = Window()
widget.show()
application.exit(application.exec_())