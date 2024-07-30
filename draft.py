import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

class AppDemo(QDialog):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        self.pixmap = QPixmap('background.png')
        self.label.setPixmap(self.pixmap)
        uic.loadUi('draft.ui', self)
        self.setWindowTitle("Generator")
        self.setGeometry(0, 0, 600, 400)
        self.label.resize(self.pixmap.width(), self.pixmap.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')