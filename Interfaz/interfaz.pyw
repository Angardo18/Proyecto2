from gui    import Ui_Ventana
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QPen, QPixmap, QColor
import threading
import time
from PyQt5.QtCore import Qt
from serial import Serial


class VentanaPrincipal (QtWidgets.QMainWindow, Ui_Ventana):
    def __init__(self):
        super().__init__() # se inicializa el constructor de las clases padre
        self.setupUi(self)
        self.estaDibujando = False

        self.mapa = QPixmap(950, 750)
        self.mapa.fill(QColor('#ffffff'))  # Fill entire canvas.
        self.lblPaint.setPixmap(self.mapa)
        self.painter = QPainter(self.lblPaint.pixmap())
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor('red'))
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.setPen(pen)

        self.bloquear = threading.Lock()

        self.btnConectar.clicked.connect(self.iniciarConexion)
        self.btnDibujar.clicked.connect(self.obtenerDatos)
        self.btnBorrar.clicked.connect(self.borrar)
        self.btnDetener.clicked.connect(self.detener)

    def detener(self):
        global  bandera
        bandera = False

    def exportar(self):
        mapa = self.lblPaint.pixmap()
        imagen = self.lblPaint.pixmap().toImage()

    def obtenerDatos(self):
        global bandera
        if not bandera:
            try:
                hiloMod1 = threading.Thread(target=moverX, daemon=True)
                hiloMod2 = threading.Thread(target=moverY, daemon=True)

                bandera = True

                hiloMod1.start()
                hiloMod2.start()

            except:
                pass

    def paint(self, x, y):
        try:

         # self.bloquear.acquire() #se bloquea para que solo 1 hilo entre a la vez
            self.estaDibujando = True # se indica que se esta habilitando

            self.painter.drawPoint(x,y)
            self.update()
            self.estaDibujando = False # se indica que no se esta dibujanto
            # self.bloquear.release() #se libera
        except:
            print("error")

        # print("se esta pintando")
    def borrar(self):
        global bandera
        flag = True  # bandera usada para mantener en el bucle

        while flag:
            if not self.estaDibujando:
                try:
                    flag = False
                    self.painter.eraseRect(0,0,950,750)
                    self.update()
                    print("dibujando")
                    #self.bloquear.release()
                except :
                    print("error fatal")

    def iniciarConexion(self):
        global  pic
        try:
            pic = Serial(port=self.txtConectar.text(), baudrate=9615, writeTimeout=0)
            pic.flushInput()
            pic.flushOutput()
            mantener = True #esta bandera se usa para mantener dentro de un bucle, hasta que se detecte que se estan
            #recibiendo bien los datos

            hiloDatos = threading.Thread(name="lectura", target=obtenerDatos, daemon=True)
            hiloDatos.start()
        except:
            print("error al conectar, nombre no reconocido")

# Funcion que se ejecutara en segundo plano


def obtenerDatos():
    global pic, potx, poty, x, y
    pic.flushOutput()
    while 1:
        #try:

        leer = pic.readline()
        print(leer)
        lectura = leer.decode("ascii")# deberia venir un string en formato x,y \n
        pic.flushInput()
        print(leer)

        lista = lectura.split(",")

        stringx = str(x)
        stringy = str(y)

        # esto es para que se verifique que los numeros enviados siempre tengan 3 caracteres
        if len(stringx) == 1:
            stringx = "00" + stringx
        elif len(stringx) == 2:
            stringx = "0" + stringx
        if len(stringy) == 1:
            stringy = "00" + stringy
        elif len(stringy) == 2:
            stringy = "0" +stringy

        print((stringx+","+stringy).encode("ascii"))
        pic.write((stringx+","+stringy+chr(0)).encode("ascii"))

        print(lectura)
        #except:
        #lista = []
         #   print("Erroue")
        if len(lista) == 2: # si no es 2 hubo una lectura erronea
            # se colocan mas filtros de forma que los unicos datos que se reciben son los que cumplen los
            # formatos de envio, es decir un numero de 3 cifras para  x, un numero de 4 cifras para y, y salto
            try:
                if len(lista[0]) == 3 and int(lista[0])<=255 :
                    potx = int(lista[0])
            except:
                pass
                #print(potx, poty)
            try:
                if len(lista[1]) == 4 and int(lista[1]) <= 255:
                    poty = int(lista[1])
            except:
                pass

            #print(potx,poty)


def moverX():
    global x, potx,  bandera
    while bandera:
        try:
            if potx <=100:
                x = x - 1
                if x == -1:
                    x = 950
                delay = (9/10000) * potx + 0.01
                time.sleep(delay)
                ventana.paint(x, y)
            if 155<=potx:
                x = x + 1
                if x == 951:
                    x = 0
                delay = (-9/10000) * (potx - 155) +0.1
                time.sleep(delay)
                ventana.paint(x, y)
        except:
            print("error en moverx")


def moverY():
    global y, poty, bandera
    while bandera:
        try:
            if poty <= 100:
                y = y + 1
                if y == 751:
                    y = 0
                delay = (9/12400) * poty +0.01
                time.sleep(delay)
                ventana.paint(x, y)
            if 155 <= poty:
                y = y - 1
                if y == -1:
                    y = 750
                delay = (-9/10000) * (poty - 155) + 0.1
                time.sleep(delay)
                ventana.paint(x, y)
            #print("y")
        except:
            print("error en movery")


bandera = False

potx,poty = 128, 128
x, y = 0, 0
pic = None

aplication = QtWidgets.QApplication([])
ventana = VentanaPrincipal()


ventana.show()
aplication.exec_()

print(x,y)
if not pic is None:
    pic.close()
    #print("ta")