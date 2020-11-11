from serial import *

if __name__ == "__main__":
    name = input("Introduce el nombre del puerto:")
    rate = 9600
    pic = Serial(port=name, baudrate=rate)
    pic.flushInput()

    while True:
        lectura = pic.readline()
        print(lectura)











