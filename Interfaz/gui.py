# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana(object):
    def setupUi(self, Ventana):
        Ventana.setObjectName("Ventana")
        Ventana.resize(1200, 1050)
        self.frame = QtWidgets.QFrame(Ventana)
        self.frame.setGeometry(QtCore.QRect(190, 20, 1000, 1000))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnDibujar = QtWidgets.QPushButton(Ventana)
        self.btnDibujar.setGeometry(QtCore.QRect(40, 30, 93, 28))
        self.btnDibujar.setObjectName("btnDibujar")
        self.btnDetener = QtWidgets.QPushButton(Ventana)
        self.btnDetener.setGeometry(QtCore.QRect(40, 80, 93, 28))
        self.btnDetener.setObjectName("btnDetener")
        self.slAzul = QtWidgets.QSlider(Ventana)
        self.slAzul.setGeometry(QtCore.QRect(140, 180, 22, 160))
        self.slAzul.setMaximum(255)
        self.slAzul.setOrientation(QtCore.Qt.Vertical)
        self.slAzul.setObjectName("slAzul")
        self.label = QtWidgets.QLabel(Ventana)
        self.label.setGeometry(QtCore.QRect(70, 240, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Ventana)
        self.label_2.setGeometry(QtCore.QRect(70, 420, 55, 16))
        self.label_2.setObjectName("label_2")
        self.slRojo = QtWidgets.QSlider(Ventana)
        self.slRojo.setGeometry(QtCore.QRect(140, 370, 22, 160))
        self.slRojo.setMaximum(255)
        self.slRojo.setOrientation(QtCore.Qt.Vertical)
        self.slRojo.setObjectName("slRojo")
        self.slVerde = QtWidgets.QSlider(Ventana)
        self.slVerde.setGeometry(QtCore.QRect(140, 570, 22, 160))
        self.slVerde.setMaximum(255)
        self.slVerde.setOrientation(QtCore.Qt.Vertical)
        self.slVerde.setObjectName("slVerde")
        self.label_3 = QtWidgets.QLabel(Ventana)
        self.label_3.setGeometry(QtCore.QRect(70, 630, 55, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Ventana)
        QtCore.QMetaObject.connectSlotsByName(Ventana)

    def retranslateUi(self, Ventana):
        _translate = QtCore.QCoreApplication.translate
        Ventana.setWindowTitle(_translate("Ventana", "Form"))
        self.btnDibujar.setText(_translate("Ventana", "Dibujar"))
        self.btnDetener.setText(_translate("Ventana", "Detener"))
        self.label.setText(_translate("Ventana", "Azul"))
        self.label_2.setText(_translate("Ventana", "Rojo"))
        self.label_3.setText(_translate("Ventana", "Verde"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventana = QtWidgets.QWidget()
    ui = Ui_Ventana()
    ui.setupUi(Ventana)
    Ventana.show()
    sys.exit(app.exec_())
