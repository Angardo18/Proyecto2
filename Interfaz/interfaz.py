from gui    import Ui_Ventana
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt


class VentanaPrincipal (QtWidgets.QMainWindow,Ui_Ventana):
    def __init__(self):
        super().__init__() #se inicializa el constructor de las clases padre
        self.setupUi(self)

        mapa = QPixmap(950,750)
        self.lblPaint.setPixmap(mapa)
        self.btnConectar.clicked.connect(self.editarLabel)
        self.btnDibujar.clicked.connect(self.pintarLinea)


    def editarLabel(self):
        self.lblConectar.setText("Este es un string cambiado")

    def pintarLinea(self):
        painter = QPainter(self.lblPaint.pixmap())
        painter.drawLine(10, 10, 300, 200)
        painter.end()
        self.lblPaint.update()

aplication = QtWidgets.QApplication([])
ventana = VentanaPrincipal()
ventana.show()
aplication.exec_()