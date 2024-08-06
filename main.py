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
        self.setFixedSize(800, 600)
        self.label = QLabel(self)
        self.pixmap = QPixmap('background.png')
        self.label.setPixmap(self.pixmap)
        uic.loadUi('main.ui', self)
        self.setWindowTitle("Generator")
        #Label.setText('Cosik')

with open("udzielenie.txt", encoding='UTF-8') as u:
    udzielenie = [line.rstrip() for line in u]

with open("pomoc.txt", encoding='UTF-8') as u:
    pomoc = [line.rstrip() for line in u]

with open("beznadziejne.txt", encoding='UTF-8') as u:
    beznadziejne = [line.rstrip() for line in u]

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = MyGenerator()
    demo.show()

    print(udzielenie)
    print(pomoc)
    print(beznadziejne)

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')