# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timbres.ui'
#
# Created: Wed Sep 24 20:47:34 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_winTimbreGest(object):
    def setupUi(self, winTimbreGest):
        winTimbreGest.setObjectName(_fromUtf8("winTimbreGest"))
        winTimbreGest.resize(861, 594)
        self.gridLayout = QtGui.QGridLayout(winTimbreGest)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(winTimbreGest)
        self.groupBox.setMaximumSize(QtCore.QSize(301, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.listaSesiones = QtGui.QListWidget(self.groupBox)
        self.listaSesiones.setMaximumSize(QtCore.QSize(161, 16777215))
        self.listaSesiones.setObjectName(_fromUtf8("listaSesiones"))
        self.gridLayout_3.addWidget(self.listaSesiones, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnCrearSesion = QtGui.QPushButton(self.groupBox)
        self.btnCrearSesion.setMaximumSize(QtCore.QSize(96, 16777215))
        self.btnCrearSesion.setObjectName(_fromUtf8("btnCrearSesion"))
        self.verticalLayout.addWidget(self.btnCrearSesion)
        self.btnBorrarSesion = QtGui.QPushButton(self.groupBox)
        self.btnBorrarSesion.setMaximumSize(QtCore.QSize(96, 16777215))
        self.btnBorrarSesion.setObjectName(_fromUtf8("btnBorrarSesion"))
        self.verticalLayout.addWidget(self.btnBorrarSesion)
        self.btnLanzarAhora = QtGui.QPushButton(self.groupBox)
        self.btnLanzarAhora.setObjectName(_fromUtf8("btnLanzarAhora"))
        self.verticalLayout.addWidget(self.btnLanzarAhora)
        self.btnEditarSesion = QtGui.QPushButton(self.groupBox)
        self.btnEditarSesion.setMaximumSize(QtCore.QSize(96, 16777215))
        self.btnEditarSesion.setObjectName(_fromUtf8("btnEditarSesion"))
        self.verticalLayout.addWidget(self.btnEditarSesion)
        self.btnGuardarCambios = QtGui.QPushButton(self.groupBox)
        self.btnGuardarCambios.setMaximumSize(QtCore.QSize(96, 16777215))
        self.btnGuardarCambios.setObjectName(_fromUtf8("btnGuardarCambios"))
        self.verticalLayout.addWidget(self.btnGuardarCambios)
        self.btnDescartarCambios = QtGui.QPushButton(self.groupBox)
        self.btnDescartarCambios.setMaximumSize(QtCore.QSize(96, 16777215))
        self.btnDescartarCambios.setObjectName(_fromUtf8("btnDescartarCambios"))
        self.verticalLayout.addWidget(self.btnDescartarCambios)
        self.chkSesionActiva = QtGui.QCheckBox(self.groupBox)
        self.chkSesionActiva.setObjectName(_fromUtf8("chkSesionActiva"))
        self.verticalLayout.addWidget(self.chkSesionActiva)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.btnSalir = QtGui.QPushButton(self.groupBox)
        self.btnSalir.setMaximumSize(QtCore.QSize(85, 16777215))
        self.btnSalir.setObjectName(_fromUtf8("btnSalir"))
        self.gridLayout_3.addWidget(self.btnSalir, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.propiedadesSesion = QtGui.QGroupBox(winTimbreGest)
        self.propiedadesSesion.setObjectName(_fromUtf8("propiedadesSesion"))
        self.gridLayout_2 = QtGui.QGridLayout(self.propiedadesSesion)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.propiedadesSesion)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.horaInicioSesion = QtGui.QTimeEdit(self.propiedadesSesion)
        self.horaInicioSesion.setMaximumSize(QtCore.QSize(67, 16777215))
        self.horaInicioSesion.setObjectName(_fromUtf8("horaInicioSesion"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.horaInicioSesion)
        self.label_2 = QtGui.QLabel(self.propiedadesSesion)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horaFinalSesion = QtGui.QTimeEdit(self.propiedadesSesion)
        self.horaFinalSesion.setMaximumSize(QtCore.QSize(67, 16777215))
        self.horaFinalSesion.setObjectName(_fromUtf8("horaFinalSesion"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.horaFinalSesion)
        self.descripcionLabel = QtGui.QLabel(self.propiedadesSesion)
        self.descripcionLabel.setObjectName(_fromUtf8("descripcionLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.descripcionLabel)
        self.txtDescripcion = QtGui.QLineEdit(self.propiedadesSesion)
        self.txtDescripcion.setObjectName(_fromUtf8("txtDescripcion"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtDescripcion)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.propiedadesSesion)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.chkRepetirLunes = QtGui.QCheckBox(self.propiedadesSesion)
        self.chkRepetirLunes.setObjectName(_fromUtf8("chkRepetirLunes"))
        self.horizontalLayout.addWidget(self.chkRepetirLunes)
        self.chkRepetirMartes = QtGui.QCheckBox(self.propiedadesSesion)
        self.chkRepetirMartes.setObjectName(_fromUtf8("chkRepetirMartes"))
        self.horizontalLayout.addWidget(self.chkRepetirMartes)
        self.chkRepetirMiercoles = QtGui.QCheckBox(self.propiedadesSesion)
        self.chkRepetirMiercoles.setObjectName(_fromUtf8("chkRepetirMiercoles"))
        self.horizontalLayout.addWidget(self.chkRepetirMiercoles)
        self.chkRepetirJueves = QtGui.QCheckBox(self.propiedadesSesion)
        self.chkRepetirJueves.setObjectName(_fromUtf8("chkRepetirJueves"))
        self.horizontalLayout.addWidget(self.chkRepetirJueves)
        self.chkRepetirViernes = QtGui.QCheckBox(self.propiedadesSesion)
        self.chkRepetirViernes.setObjectName(_fromUtf8("chkRepetirViernes"))
        self.horizontalLayout.addWidget(self.chkRepetirViernes)
        self.chkRepetirSabado = QtGui.QCheckBox(self.propiedadesSesion)
        self.chkRepetirSabado.setObjectName(_fromUtf8("chkRepetirSabado"))
        self.horizontalLayout.addWidget(self.chkRepetirSabado)
        self.chkRepetirDomingo = QtGui.QCheckBox(self.propiedadesSesion)
        self.chkRepetirDomingo.setObjectName(_fromUtf8("chkRepetirDomingo"))
        self.horizontalLayout.addWidget(self.chkRepetirDomingo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.propiedadesSesion)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.txtTimbreInicial = QtGui.QLineEdit(self.propiedadesSesion)
        self.txtTimbreInicial.setObjectName(_fromUtf8("txtTimbreInicial"))
        self.horizontalLayout_2.addWidget(self.txtTimbreInicial)
        self.btnCargarTimbreInicial = QtGui.QToolButton(self.propiedadesSesion)
        self.btnCargarTimbreInicial.setObjectName(_fromUtf8("btnCargarTimbreInicial"))
        self.horizontalLayout_2.addWidget(self.btnCargarTimbreInicial)
        self.btnBorrarTimbreInicial = QtGui.QToolButton(self.propiedadesSesion)
        self.btnBorrarTimbreInicial.setObjectName(_fromUtf8("btnBorrarTimbreInicial"))
        self.horizontalLayout_2.addWidget(self.btnBorrarTimbreInicial)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.propiedadesSesion)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.tiempoInicioTimbreInicial = QtGui.QTimeEdit(self.propiedadesSesion)
        self.tiempoInicioTimbreInicial.setObjectName(_fromUtf8("tiempoInicioTimbreInicial"))
        self.horizontalLayout_3.addWidget(self.tiempoInicioTimbreInicial)
        self.label_6 = QtGui.QLabel(self.propiedadesSesion)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.duracionTimbreInicial = QtGui.QTimeEdit(self.propiedadesSesion)
        self.duracionTimbreInicial.setObjectName(_fromUtf8("duracionTimbreInicial"))
        self.horizontalLayout_3.addWidget(self.duracionTimbreInicial)
        self.btnPruebaTimbreInicial = QtGui.QToolButton(self.propiedadesSesion)
        self.btnPruebaTimbreInicial.setObjectName(_fromUtf8("btnPruebaTimbreInicial"))
        self.horizontalLayout_3.addWidget(self.btnPruebaTimbreInicial)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.volumenTimbreInicial = QtGui.QDial(self.propiedadesSesion)
        self.volumenTimbreInicial.setWrapping(False)
        self.volumenTimbreInicial.setObjectName(_fromUtf8("volumenTimbreInicial"))
        self.horizontalLayout_4.addWidget(self.volumenTimbreInicial)
        self.lblVolumenTimbreInicial = QtGui.QLabel(self.propiedadesSesion)
        self.lblVolumenTimbreInicial.setObjectName(_fromUtf8("lblVolumenTimbreInicial"))
        self.horizontalLayout_4.addWidget(self.lblVolumenTimbreInicial)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_7 = QtGui.QLabel(self.propiedadesSesion)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.txtTimbreFinal = QtGui.QLineEdit(self.propiedadesSesion)
        self.txtTimbreFinal.setObjectName(_fromUtf8("txtTimbreFinal"))
        self.horizontalLayout_6.addWidget(self.txtTimbreFinal)
        self.btnCargarTimbreFinal = QtGui.QToolButton(self.propiedadesSesion)
        self.btnCargarTimbreFinal.setObjectName(_fromUtf8("btnCargarTimbreFinal"))
        self.horizontalLayout_6.addWidget(self.btnCargarTimbreFinal)
        self.btnBorrarTimbreFinal = QtGui.QToolButton(self.propiedadesSesion)
        self.btnBorrarTimbreFinal.setObjectName(_fromUtf8("btnBorrarTimbreFinal"))
        self.horizontalLayout_6.addWidget(self.btnBorrarTimbreFinal)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_8 = QtGui.QLabel(self.propiedadesSesion)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_7.addWidget(self.label_8)
        self.tiempoInicioTimbreFinal = QtGui.QTimeEdit(self.propiedadesSesion)
        self.tiempoInicioTimbreFinal.setObjectName(_fromUtf8("tiempoInicioTimbreFinal"))
        self.horizontalLayout_7.addWidget(self.tiempoInicioTimbreFinal)
        self.label_9 = QtGui.QLabel(self.propiedadesSesion)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_7.addWidget(self.label_9)
        self.duracionTimbreFinal = QtGui.QTimeEdit(self.propiedadesSesion)
        self.duracionTimbreFinal.setObjectName(_fromUtf8("duracionTimbreFinal"))
        self.horizontalLayout_7.addWidget(self.duracionTimbreFinal)
        self.btnPruebaTimbreFinal = QtGui.QToolButton(self.propiedadesSesion)
        self.btnPruebaTimbreFinal.setObjectName(_fromUtf8("btnPruebaTimbreFinal"))
        self.horizontalLayout_7.addWidget(self.btnPruebaTimbreFinal)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.volumenTimbreFinal = QtGui.QDial(self.propiedadesSesion)
        self.volumenTimbreFinal.setObjectName(_fromUtf8("volumenTimbreFinal"))
        self.horizontalLayout_5.addWidget(self.volumenTimbreFinal)
        self.lblVolumenTimbreFinal = QtGui.QLabel(self.propiedadesSesion)
        self.lblVolumenTimbreFinal.setObjectName(_fromUtf8("lblVolumenTimbreFinal"))
        self.horizontalLayout_5.addWidget(self.lblVolumenTimbreFinal)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_13 = QtGui.QLabel(self.propiedadesSesion)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_12.addWidget(self.label_13)
        self.listaHiloMusical = QtGui.QListWidget(self.propiedadesSesion)
        self.listaHiloMusical.setObjectName(_fromUtf8("listaHiloMusical"))
        self.horizontalLayout_12.addWidget(self.listaHiloMusical)
        self.btnCargarHiloMusical = QtGui.QToolButton(self.propiedadesSesion)
        self.btnCargarHiloMusical.setObjectName(_fromUtf8("btnCargarHiloMusical"))
        self.horizontalLayout_12.addWidget(self.btnCargarHiloMusical)
        self.btnBorrarHiloMusical = QtGui.QToolButton(self.propiedadesSesion)
        self.btnBorrarHiloMusical.setObjectName(_fromUtf8("btnBorrarHiloMusical"))
        self.horizontalLayout_12.addWidget(self.btnBorrarHiloMusical)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_14 = QtGui.QLabel(self.propiedadesSesion)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_13.addWidget(self.label_14)
        self.tiempoInicioHiloMusical = QtGui.QTimeEdit(self.propiedadesSesion)
        self.tiempoInicioHiloMusical.setObjectName(_fromUtf8("tiempoInicioHiloMusical"))
        self.horizontalLayout_13.addWidget(self.tiempoInicioHiloMusical)
        self.label_15 = QtGui.QLabel(self.propiedadesSesion)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_13.addWidget(self.label_15)
        self.duracionHiloMusical = QtGui.QTimeEdit(self.propiedadesSesion)
        self.duracionHiloMusical.setObjectName(_fromUtf8("duracionHiloMusical"))
        self.horizontalLayout_13.addWidget(self.duracionHiloMusical)
        self.btnPruebaHiloMusical = QtGui.QToolButton(self.propiedadesSesion)
        self.btnPruebaHiloMusical.setObjectName(_fromUtf8("btnPruebaHiloMusical"))
        self.horizontalLayout_13.addWidget(self.btnPruebaHiloMusical)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_11.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.volumenHiloMusical = QtGui.QDial(self.propiedadesSesion)
        self.volumenHiloMusical.setObjectName(_fromUtf8("volumenHiloMusical"))
        self.verticalLayout_7.addWidget(self.volumenHiloMusical)
        self.lblVolumenHiloMusical = QtGui.QLabel(self.propiedadesSesion)
        self.lblVolumenHiloMusical.setObjectName(_fromUtf8("lblVolumenHiloMusical"))
        self.verticalLayout_7.addWidget(self.lblVolumenHiloMusical)
        self.chkModoAleatorio = QtGui.QCheckBox(self.propiedadesSesion)
        self.chkModoAleatorio.setObjectName(_fromUtf8("chkModoAleatorio"))
        self.verticalLayout_7.addWidget(self.chkModoAleatorio)
        self.horizontalLayout_11.addLayout(self.verticalLayout_7)
        self.gridLayout_2.addLayout(self.horizontalLayout_11, 6, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_10 = QtGui.QLabel(self.propiedadesSesion)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_9.addWidget(self.label_10)
        self.txtTimbreMelodia = QtGui.QLineEdit(self.propiedadesSesion)
        self.txtTimbreMelodia.setObjectName(_fromUtf8("txtTimbreMelodia"))
        self.horizontalLayout_9.addWidget(self.txtTimbreMelodia)
        self.btnCargarTimbreMelodia = QtGui.QToolButton(self.propiedadesSesion)
        self.btnCargarTimbreMelodia.setObjectName(_fromUtf8("btnCargarTimbreMelodia"))
        self.horizontalLayout_9.addWidget(self.btnCargarTimbreMelodia)
        self.btnBorrarTimbreMelodia = QtGui.QToolButton(self.propiedadesSesion)
        self.btnBorrarTimbreMelodia.setObjectName(_fromUtf8("btnBorrarTimbreMelodia"))
        self.horizontalLayout_9.addWidget(self.btnBorrarTimbreMelodia)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_11 = QtGui.QLabel(self.propiedadesSesion)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_10.addWidget(self.label_11)
        self.tiempoInicioTimbreMelodia = QtGui.QTimeEdit(self.propiedadesSesion)
        self.tiempoInicioTimbreMelodia.setObjectName(_fromUtf8("tiempoInicioTimbreMelodia"))
        self.horizontalLayout_10.addWidget(self.tiempoInicioTimbreMelodia)
        self.label_12 = QtGui.QLabel(self.propiedadesSesion)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_10.addWidget(self.label_12)
        self.duracionTimbreMelodia = QtGui.QTimeEdit(self.propiedadesSesion)
        self.duracionTimbreMelodia.setObjectName(_fromUtf8("duracionTimbreMelodia"))
        self.horizontalLayout_10.addWidget(self.duracionTimbreMelodia)
        self.btnPruebaTimbreMelodia = QtGui.QToolButton(self.propiedadesSesion)
        self.btnPruebaTimbreMelodia.setObjectName(_fromUtf8("btnPruebaTimbreMelodia"))
        self.horizontalLayout_10.addWidget(self.btnPruebaTimbreMelodia)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.volumenTimbreMelodia = QtGui.QDial(self.propiedadesSesion)
        self.volumenTimbreMelodia.setObjectName(_fromUtf8("volumenTimbreMelodia"))
        self.horizontalLayout_8.addWidget(self.volumenTimbreMelodia)
        self.lblVolumenTimbreMelodia = QtGui.QLabel(self.propiedadesSesion)
        self.lblVolumenTimbreMelodia.setObjectName(_fromUtf8("lblVolumenTimbreMelodia"))
        self.horizontalLayout_8.addWidget(self.lblVolumenTimbreMelodia)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.propiedadesSesion, 0, 1, 1, 1)

        self.retranslateUi(winTimbreGest)
        QtCore.QMetaObject.connectSlotsByName(winTimbreGest)

    def retranslateUi(self, winTimbreGest):
        winTimbreGest.setWindowTitle(_translate("winTimbreGest", "TimbreGest", None))
        self.groupBox.setTitle(_translate("winTimbreGest", "Sesiones", None))
        self.btnCrearSesion.setText(_translate("winTimbreGest", "Crear sesión", None))
        self.btnBorrarSesion.setText(_translate("winTimbreGest", "Borrar sesión", None))
        self.btnLanzarAhora.setText(_translate("winTimbreGest", "Lanzar ahora", None))
        self.btnEditarSesion.setText(_translate("winTimbreGest", "Editar sesión", None))
        self.btnGuardarCambios.setText(_translate("winTimbreGest", "Guardar", None))
        self.btnDescartarCambios.setText(_translate("winTimbreGest", "Descartar", None))
        self.chkSesionActiva.setText(_translate("winTimbreGest", "Sesión activa", None))
        self.btnSalir.setText(_translate("winTimbreGest", "Salir", None))
        self.propiedadesSesion.setTitle(_translate("winTimbreGest", "Propiedades de sesión", None))
        self.label.setText(_translate("winTimbreGest", "Hora de inicio", None))
        self.label_2.setText(_translate("winTimbreGest", "Hora de finalización", None))
        self.descripcionLabel.setText(_translate("winTimbreGest", "Descripción", None))
        self.label_3.setText(_translate("winTimbreGest", "<b>Repeticiones</b>", None))
        self.chkRepetirLunes.setText(_translate("winTimbreGest", "L", None))
        self.chkRepetirMartes.setText(_translate("winTimbreGest", "M", None))
        self.chkRepetirMiercoles.setText(_translate("winTimbreGest", "X", None))
        self.chkRepetirJueves.setText(_translate("winTimbreGest", "J", None))
        self.chkRepetirViernes.setText(_translate("winTimbreGest", "V", None))
        self.chkRepetirSabado.setText(_translate("winTimbreGest", "S", None))
        self.chkRepetirDomingo.setText(_translate("winTimbreGest", "D", None))
        self.label_4.setText(_translate("winTimbreGest", "<b>Timbre inicial</b>", None))
        self.btnCargarTimbreInicial.setText(_translate("winTimbreGest", "...", None))
        self.btnBorrarTimbreInicial.setText(_translate("winTimbreGest", "...", None))
        self.label_5.setText(_translate("winTimbreGest", "Inicio", None))
        self.tiempoInicioTimbreInicial.setDisplayFormat(_translate("winTimbreGest", "mm:ss", None))
        self.label_6.setText(_translate("winTimbreGest", "Duración", None))
        self.duracionTimbreInicial.setDisplayFormat(_translate("winTimbreGest", "mm:ss", None))
        self.btnPruebaTimbreInicial.setText(_translate("winTimbreGest", "...", None))
        self.lblVolumenTimbreInicial.setText(_translate("winTimbreGest", "0", None))
        self.label_7.setText(_translate("winTimbreGest", "<b>Timbre final</b>", None))
        self.btnCargarTimbreFinal.setText(_translate("winTimbreGest", "...", None))
        self.btnBorrarTimbreFinal.setText(_translate("winTimbreGest", "...", None))
        self.label_8.setText(_translate("winTimbreGest", "Inicio", None))
        self.tiempoInicioTimbreFinal.setDisplayFormat(_translate("winTimbreGest", "mm:ss", None))
        self.label_9.setText(_translate("winTimbreGest", "Duración", None))
        self.duracionTimbreFinal.setDisplayFormat(_translate("winTimbreGest", "mm:ss", None))
        self.btnPruebaTimbreFinal.setText(_translate("winTimbreGest", "...", None))
        self.lblVolumenTimbreFinal.setText(_translate("winTimbreGest", "0", None))
        self.label_13.setText(_translate("winTimbreGest", "<b>Hilo musical</b>", None))
        self.btnCargarHiloMusical.setText(_translate("winTimbreGest", "...", None))
        self.btnBorrarHiloMusical.setText(_translate("winTimbreGest", "...", None))
        self.label_14.setText(_translate("winTimbreGest", "Inicio", None))
        self.tiempoInicioHiloMusical.setDisplayFormat(_translate("winTimbreGest", "mm:ss", None))
        self.label_15.setText(_translate("winTimbreGest", "Duración", None))
        self.duracionHiloMusical.setDisplayFormat(_translate("winTimbreGest", "mm:ss", None))
        self.btnPruebaHiloMusical.setText(_translate("winTimbreGest", "...", None))
        self.lblVolumenHiloMusical.setText(_translate("winTimbreGest", "0", None))
        self.chkModoAleatorio.setText(_translate("winTimbreGest", "Modo aleatorio", None))
        self.label_10.setText(_translate("winTimbreGest", "<b>Melodía entre timbres</b>", None))
        self.btnCargarTimbreMelodia.setText(_translate("winTimbreGest", "...", None))
        self.btnBorrarTimbreMelodia.setText(_translate("winTimbreGest", "...", None))
        self.label_11.setText(_translate("winTimbreGest", "Inicio", None))
        self.tiempoInicioTimbreMelodia.setDisplayFormat(_translate("winTimbreGest", "mm:ss", None))
        self.label_12.setText(_translate("winTimbreGest", "Duración", None))
        self.duracionTimbreMelodia.setDisplayFormat(_translate("winTimbreGest", "mm:ss", None))
        self.btnPruebaTimbreMelodia.setText(_translate("winTimbreGest", "...", None))
        self.lblVolumenTimbreMelodia.setText(_translate("winTimbreGest", "0", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    winTimbreGest = QtGui.QWidget()
    ui = Ui_winTimbreGest()
    ui.setupUi(winTimbreGest)
    winTimbreGest.show()
    sys.exit(app.exec_())
