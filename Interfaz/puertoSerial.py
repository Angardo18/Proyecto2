from serial import *

class puertoPic(object):
    def __init__(self,nombre,baudrate):
    # se inicia la comunicacion devuelve null si hubo algun error
        self.puerto = None
        self.dataRead = None #datos recibidos
        self.dataWrite = None #datos a enviar
        self.valorX = 0
        self.valorY = 0
        self.direcccionX = None #none no hace nada, true derecha  false izquierda
        self.direcccionY = None  # none no hace nada, true derecha  false izquierda

        try:
            self.puerto = Serial(port=nombre,baudrate=baudrate, writeTimeout=1)
        except ValueError:
            raise ValueError
        except SerialException:
            raise SerialException

    def establecerDireccion(self):
        self.recibir()
        lista = self.dataRead.split(",");
        # desde el pic se enviara el primer dato como la velocidad en x y otro como la velocidad en y
        x = lista[0]
        y = lista[1]

        if 124 < x < 132:
           self.direcccionX = None
        elif x <= 124:
            self.direcccionX = True
        else:
            self.direcccionX = False

        if 124 < y < 132:
           self.direcccionY = None
        elif y <= 124:
            self.direcccionY = True
        else:
            self.direcccionY = False


    def enviar(self):
        self.puerto.write(self.dataWrite.encode("ascii")) # tirara error a menos que sea un string

    def recibir(self):
        self.dataRead = self.puerto.readline()

if __name__ == "__main__":
    name = input("Introduce el nombre del puerto:")
    rate =  10417










