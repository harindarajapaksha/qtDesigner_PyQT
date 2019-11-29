import sys
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
        a = [1,2,3,4,5,6,7,8,9,10]
        b = [12,23,34,45,56,67,78,89,90,10]

        fig, ax2 = plt.subplots()
        ax2.boxplot([a,b])

        self.mlp2 = FigureCanvas(fig)
        lay = QHBoxLayout(self.widget_2)
        lay.addWidget(self.mlp2)

    def clicked_exit(self):
        sys.exit()


application = QApplication(sys.argv)
widget = Window()
widget.show()
application.exit(application.exec_())