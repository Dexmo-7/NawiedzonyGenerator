import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

class MyGenerator(QDialog):
    def __init__(self):
        super(MyGenerator, self).__init__()
        self.setWindowTitle("Generator")
        self.startMain()

    def startMain(self):
        self.stackedLayout = QStackedLayout()
        self.setFixedSize(800, 600)
        self.label = QLabel(self)
        self.pixmap = QPixmap('background.png')
        self.label.setPixmap(self.pixmap)
        uic.loadUi('main.ui', self)
        self.setWindowTitle("Generator")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = MyGenerator()
    demo.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')