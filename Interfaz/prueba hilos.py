import threading
import time



def lecturaDePuerto():
    global x
    while True:
        print(x)


def incrementarx():
    global x
    while True:
        x = x+ 1
        time.sleep(0.1)
def incrementary():
    global x
    while True:
        x = 2*x
        time.sleep(0.5)

x = 0

hiloMain = threading.Thread(target=lecturaDePuerto, daemon=True)
hilo1 = threading.Thread(target=incrementarx,daemon=True)
hilo2 = threading.Thread(target=incrementary, daemon=True)
hiloMain.start()
hilo1.start()
hilo2.start()
#
while 1:
    pass