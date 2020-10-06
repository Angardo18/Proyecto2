from PyQt5.QtWidgets import QApplication, QWidget
import os
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 300)
    w.move(0, 0)
    w.setWindowTitle('Hola, Mundo')
    w.show()

    sys.exit(app.exec_())