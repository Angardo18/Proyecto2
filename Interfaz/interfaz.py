from gui    import Ui_Ventana
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap,QColor
from  puertoSerial import *
import threading
import time
from PyQt5.QtCore import Qt


class VentanaPrincipal (QtWidgets.QMainWindow,Ui_Ventana):
    def __init__(self):
        super().__init__() #se inicializa el constructor de las clases padre
        self.setupUi(self)

        self.x = 0
        self.y = 0
        self.PIC = None #atributo que representa al pic
        mapa = QPixmap(950, 750)
        mapa.fill(QColor('#ffffff'))  # Fill entire canvas.
        self.lblPaint.setPixmap(mapa)
        self.lblPaint.setPixmap(mapa)
        self.btnConectar.clicked.connect(self.iniciarConexion)
        self.btnDibujar.clicked.connect(self.pintarLinea)
        self.btnBorrar.clicked.connect(self.borrar)

    def pintarLinea(self):
        painter = QPainter(self.lblPaint.pixmap())
        pen =QPen()
        pen.setWidth(1)
        pen.setColor(QColor('red'))
        painter.setPen(pen)
        painter.drawPoint(200, 150)
        painter.drawLine(2,2,50,50)
        painter.end()
        self.update()

    def pain(self):
        painter = QPainter(self.lblPaint.pixmap())
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor('red'))
        painter.setPen(pen)
        painter.drawPoint(self.x, self.y)
        painter.end()
        self.update()

    def borrar(self):
        mapa = QPixmap(950, 750)
        mapa.fill(QColor('#ffffff'))  # Fill entire canvas.
        self.lblPaint.setPixmap(mapa)

    def iniciarConexion(self):
        try:
            self.PIC = puertoPic(self.txtConectar.text(),10417) #
        except:
            print("error al conectar, nombre no reconocido")

def lecturaDePuerto():
    global ventana
    yaInicio = False
    while True:

        if yaInicio == False and ventana.PIC is not None:

            hilo1 = threading.Thread(daemon=True, target=incrementarx)
            hilo2 = threading.Thread(daemon=True, target=incrementarx)

            yaInicio = True

            hilo1.start()
            hilo2.start()

        if ventana.PIC is not None:

            ventana.PIC.establecerDireccion();
            ventana.pain()


def incrementarx():
    global ventana
    while True:
        if ventana.PIC.direccionX == True :
            ventana.x = ventana.x + 1
            if ventana.x == 1000:
                ventana.x = 0
            valor = (3/620)*ventana.PIC.valorX + 0.1
            time.sleep(valor)

        elif ventana.PIC.direccionX == False:
            ventana.x = ventana.x - 1
            if ventana.x == -1:
                ventana.x = 999

            valor = (1 / 205) * ( ventana.PIC.valorX - 132 ) + 0.1
            time.sleep(valor)
        #si no es falso y no es verdadero entonces es none

def incrementary():
    global ventana
    while True:
        if ventana.PIC.direccionY == True :
            ventana.y = ventana.y + 1
            if ventana.y == 1000:
                ventana.y = 0
            valor = (3/620)*ventana.PIC.valorX + 0.1
            time.sleep(valor)

        elif ventana.PIC.direccionY == False:
            ventana.y = ventana.y - 1
            if ventana.y == -1:
                ventana.y = 999

            valor = (1 / 205) * ( ventana.PIC.valorX - 132 ) + 0.1
            time.sleep(valor)
        #si no es falso y no es verdadero entonces es none

aplication = QtWidgets.QApplication([])
ventana = VentanaPrincipal()


ventana.show()
aplication.exec_()