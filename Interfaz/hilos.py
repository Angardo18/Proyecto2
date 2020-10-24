import threading
import time

def funcion1():
    while True:
        print("Este es 1")
        time.sleep(0.3)

def funcion2():
    while True:
        print("Este es 2")
        time.sleep(0.6)


hilo = threading.Thread(target=funcion1)
hilo2 = threading.Thread(target=funcion2)



hilo.start()
hilo2.start()

hilo.join()