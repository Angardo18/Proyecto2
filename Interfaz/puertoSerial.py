from serial import *



class puertoPic(object):
    def __init__(self,nombre,baudrate):
    # se inicia la comunicacion devuelve null si hubo algun error
        self.puerto = None
        self.dataRead = None #datos recibidos
        self.dataWrite = None #datos a enviar
        self.valorX = 0
        self.valorY = 0
        self.direccionX = None #none no hace nada, true derecha  false izquierda
        self.direccionY = None  # none no hace nada, true derecha  false izquierda

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
        self.valorX = int(lista[0])
        self.valorY = int(lista[1])

        if 124 < self.valorX < 132:
           self.direccionX = 1
        elif self.valorX <= 124:
            self.direccionX = 2
        else:
            self.direccionX = 3

        if 124 < self.valorY < 132:
           self.direccionY = 1
        elif self.valorY <= 124:
            self.direccionY = 2
        else:
            self.direccionY = 3


    def enviar(self):
        self.puerto.write(self.dataWrite.encode("ascii")) # tirara error a menos que sea un string

    def recibir(self):
        self.dataRead = self.puerto.readline()

if __name__ == "__main__":
    name = input("Introduce el nombre del puerto:")
    rate =  10417

    pic = puertoPic(name, rate)

    while True:

        pic.recibir()
        print(pic.dataRead)










