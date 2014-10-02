#!/usr/bin/python3
from PyQt4 import QtGui
from modelo import Modelo
from vista import Vista
from controlador import Controlador
import sys


class TimbreGestApp(QtGui.QApplication):
    modelo = None
    vista = None
    controlador = None

    def __init__(self, argv):
        super(TimbreGestApp, self).__init__(argv)
        self.modelo = Modelo()
        self.vista = Vista()
        self.controlador = Controlador()

        self.controlador.modelo = self.modelo
        self.controlador.vista = self.vista
        self.vista.controlador = self.controlador
        self.modelo.controlador = self.controlador

        self.modelo.cargar_datos()

    def run(self):
        self.vista.winTimbreGest.show()
        self.vista.winTimbreGest.temporizador.start(1000)
        sys.exit(self.exec_())


if __name__ == '__main__':
    app = TimbreGestApp(sys.argv)
    app.run()
