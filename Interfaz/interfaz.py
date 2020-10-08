from gui    import Ui_Ventana
from PyQt5 import QtWidgets
class VentanaPrincipal (QtWidgets.QWidget,Ui_Ventana):
    def __init__(self):
        super.__init__()
        self.setupUi(self)
