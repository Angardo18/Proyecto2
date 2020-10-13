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
        Ventana.resize(1200, 800)
        self.btnDibujar = QtWidgets.QPushButton(Ventana)
        self.btnDibujar.setGeometry(QtCore.QRect(40, 30, 93, 28))
        self.btnDibujar.setObjectName("btnDibujar")
        self.btnDetener = QtWidgets.QPushButton(Ventana)
        self.btnDetener.setGeometry(QtCore.QRect(40, 80, 93, 28))
        self.btnDetener.setObjectName("btnDetener")
        self.btnBorrar = QtWidgets.QPushButton(Ventana)
        self.btnBorrar.setGeometry(QtCore.QRect(40, 130, 93, 28))
        self.btnBorrar.setObjectName("btnBorrar")
        self.btnConectar = QtWidgets.QPushButton(Ventana)
        self.btnConectar.setGeometry(QtCore.QRect(30, 350, 93, 28))
        self.btnConectar.setObjectName("btnConectar")
        self.txtConectar = QtWidgets.QLineEdit(Ventana)
        self.txtConectar.setGeometry(QtCore.QRect(20, 320, 113, 22))
        self.txtConectar.setObjectName("txtConectar")
        self.lblConectar = QtWidgets.QLabel(Ventana)
        self.lblConectar.setGeometry(QtCore.QRect(20, 300, 121, 16))
        self.lblConectar.setObjectName("lblConectar")
        self.lblPaint = QtWidgets.QLabel(Ventana)
        self.lblPaint.setGeometry(QtCore.QRect(210, 40, 950, 750))
        self.lblPaint.setText("")
        self.lblPaint.setObjectName("lblPaint")

        self.retranslateUi(Ventana)
        QtCore.QMetaObject.connectSlotsByName(Ventana)

    def retranslateUi(self, Ventana):
        _translate = QtCore.QCoreApplication.translate
        Ventana.setWindowTitle(_translate("Ventana", "Form"))
        self.btnDibujar.setText(_translate("Ventana", "Dibujar"))
        self.btnDetener.setText(_translate("Ventana", "Detener"))
        self.btnBorrar.setText(_translate("Ventana", "Borrar"))
        self.btnConectar.setText(_translate("Ventana", "Conectar"))
        self.lblConectar.setText(_translate("Ventana", "nombre del puerto:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventana = QtWidgets.QWidget()
    ui = Ui_Ventana()
    ui.setupUi(Ventana)
    Ventana.show()
    sys.exit(app.exec_())
