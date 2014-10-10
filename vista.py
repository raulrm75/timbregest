from ui_timbres import Ui_winTimbreGest
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon
from functools import wraps
from itemproperties import itemproperty
import os
from datetime import datetime
from reproductor import ReproductorTimbre
import audioread
import configuracion


def debug_slot_method(debug_mode):
    def debug_slot_method_(slot_method):
        @wraps(slot_method)
        def result(slf, *args, **kwargs):
            if debug_mode:
                args_str = ''
                kwargs_str = ''
                if args:
                    args_str = ', '.join(map(str, args))
                if kwargs:
                    kwargs_str = ', '.join('{}={}'.format(key, value)
                        for (key, value) in kwargs.items())
                arg_str = ''
                if args:
                    arg_str = args_str
                    if kwargs:
                        arg_str += ', {}'.format(kwargs_str)
                else:
                    if kwargs:
                        arg_str = kwargs_str
                call_str = '{}({})'.format(slot_method.__name__, arg_str)
                print(call_str)
            return slot_method(slf, *args, **kwargs)
        return result
    return debug_slot_method_


class WinTimbreGest(QtGui.QWidget, Ui_winTimbreGest):
    _modo_edicion = False
    _modo_creacion = False
    _sesion_seleccionada = None
    temporizador = None
    controlador = None
    _reproductor_prueba_timbre_inicial = None
    _reproductor_prueba_timbre_final = None
    _reproductor_prueba_timbre_melodia = None
    _reproductor_alarma = None

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.play_icon = QtGui.QIcon('{}/player_play.png'.format(
            configuracion.raiz_recursos))
        self.delete_icon = QtGui.QIcon('{}/delete.png'.format(
            configuracion.raiz_recursos))
        self.open_icon = QtGui.QIcon('{}/open_folder.png'.format(
            configuracion.raiz_recursos))
        self.pause_icon = QtGui.QIcon('{}/media_pause.png'.format(
            configuracion.raiz_recursos))
        self.btnPruebaTimbreInicial.setIcon(self.play_icon)
        self.btnPruebaTimbreFinal.setIcon(self.play_icon)
        self.btnPruebaTimbreMelodia.setIcon(self.play_icon)
        self.btnPruebaHiloMusical.setIcon(self.play_icon)
        self.btnBorrarTimbreInicial.setIcon(self.delete_icon)
        self.btnBorrarTimbreFinal.setIcon(self.delete_icon)
        self.btnBorrarTimbreMelodia.setIcon(self.delete_icon)
        self.btnBorrarHiloMusical.setIcon(self.delete_icon)
        self.btnCargarTimbreInicial.setIcon(self.open_icon)
        self.btnCargarTimbreFinal.setIcon(self.open_icon)
        self.btnCargarTimbreMelodia.setIcon(self.open_icon)
        self.btnCargarHiloMusical.setIcon(self.open_icon)
        self.modo_edicion = False
        self.temporizador = QtCore.QTimer(self)
        self.temporizador.timeout.connect(self.on_temporizador_timeout)
        self._reproductor_prueba_timbre_inicial = ReproductorTimbre(self)
        self._reproductor_prueba_timbre_final = ReproductorTimbre(self)
        self._reproductor_prueba_timbre_melodia = ReproductorTimbre(self)

        self._reproductor_prueba_timbre_inicial._medio.stateChanged.connect(
            self.on_prueba_timbre_inicial_stateChanged)

        self._reproductor_prueba_timbre_final._medio.stateChanged.connect(
            self.on_prueba_timbre_final_stateChanged)

        self._reproductor_prueba_timbre_melodia._medio.stateChanged.connect(
            self.on_prueba_timbre_melodia_stateChanged)

        self._reproductor_alarma = ReproductorTimbre(self)
        self.listaSesiones.setFocus()

        # Ocultar el editor de hilo musical. Será activado en nuevas versiones
        self.label_13.hide()
        self.listaHiloMusical.hide()
        self.btnCargarHiloMusical.hide()
        self.btnBorrarHiloMusical.hide()
        self.volumenHiloMusical.hide()
        self.lblVolumenHiloMusical.hide()
        self.label_14.hide()
        self.label_15.hide()
        self.tiempoInicioHiloMusical.hide()
        self.duracionHiloMusical.hide()
        self.btnPruebaHiloMusical.hide()
        self.chkModoAleatorio.hide()
        self.btnLanzarAhora.hide()

    def __iter__(self):
        for widget in self.findChildren(QtGui.QWidget):
            yield widget

    def __getitem__(self, name):
        if isinstance(name, str):
            if (name in self.__dict__ and
                    isinstance(self.__dict__[name], QtGui.QWidget)):
                return self.__dict__[name]
            else:
                raise IndexError('"{}" no es un nombre de widget válido'.format(
                    name))
        else:
            raise TypeError('Debe proporcionar un "str" no un {}.'.format(
                type(name)))

    @property
    def modo_edicion(self):
        return self._modo_edicion

    @modo_edicion.setter
    def modo_edicion(self, modo):
        assert isinstance(modo, bool)
        self._modo_edicion = modo
        self.btnEditarSesion.setVisible(not self.modo_edicion)
        self.btnGuardarCambios.setVisible(self.modo_edicion)
        self.btnDescartarCambios.setVisible(self.modo_edicion)
        self.btnCrearSesion.setVisible(not self.modo_edicion)
        self.btnBorrarSesion.setVisible(not self.modo_edicion)
        self.chkSesionActiva.setEnabled(modo)
        for control in self:
            if (isinstance(control.parent(), QtGui.QGroupBox) and
                    control.parent().title() == 'Propiedades de sesión'):
                control.setEnabled(modo)

    @property
    def modo_creacion(self):
        return self._modo_creacion

    @modo_creacion.setter
    def modo_creacion(self, modo):
        assert isinstance(modo, bool)
        self._modo_creacion = modo
        self.modo_edicion = modo
        self.controlador.sesion = None
        self.sesion_activa = True

    @property
    def modo_aleatorio(self):
        return self.chkModoAleatorio.checkState() == QtCore.Qt.Checked

    @modo_aleatorio.setter
    def modo_aleatorio(self, modo):
        assert isinstance(modo, bool)
        if modo:
            self.chkModoAleatorio.setCheckState(QtCore.Qt.Checked)
        else:
            self.chkModoAleatorio.setCheckState(QtCore.Qt.Unchecked)

    @property
    def sesion_activa(self):
        return self.chkSesionActiva.checkState() == QtCore.Qt.Checked

    @sesion_activa.setter
    def sesion_activa(self, modo):
        assert isinstance(modo, bool)
        if modo:
            self.chkSesionActiva.setCheckState(QtCore.Qt.Checked)
        else:
            self.chkSesionActiva.setCheckState(QtCore.Qt.Unchecked)

    @itemproperty
    def repetir(self, dia):
        dias = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes',
                    'Sabado', 'Domingo')
        if isinstance(dia, str):
            if dia in dias:
                nombre = 'chkRepetir{}'.format(dia)
                return self[nombre].checkState() == QtCore.Qt.Checked
            else:
                raise IndexError('Día fuera de rango.')
        elif isinstance(dia, int):
            if 0 <= dia <= 6:
                nombre = 'chkRepetir{}'.format(dias[dia])
                return self[nombre].checkState() == QtCore.Qt.Checked
            else:
                raise IndexError('Día fuera de rango.')

    @repetir.setter
    def repetir(self, dia, valor):
        assert isinstance(valor, bool)
        dias = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes',
                'Sabado', 'Domingo')
        if isinstance(dia, str):
            if dia in dias:
                nombre = 'chkRepetir{}'.format(dia)
                if valor:
                    self[nombre].setCheckState(QtCore.Qt.Checked)
                else:
                    self[nombre].setCheckState(QtCore.Qt.Unchecked)
            else:
                raise IndexError('Día fuera de rango.')
        elif isinstance(dia, int):
            if 0 <= dia <= 6:
                nombre = 'chkRepetir{}'.format(dias[dia])
                if valor:
                    self[nombre].setCheckState(QtCore.Qt.Checked)
                else:
                    self[nombre].setCheckState(QtCore.Qt.Unchecked)
            else:
                raise IndexError('Día fuera de rango.')

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnSalir_clicked(self):
        self.close()

    def closeEvent(self, event):
        if QtGui.QMessageBox.question(
                self, 'Confirmación', '¿Seguro que desea salir?',
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
            super(WinTimbreGest, self).closeEvent(event)
        else:
            event.ignore()

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnCrearSesion_clicked(self):
        self.modo_creacion = True

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnBorrarSesion_clicked(self):
        if (self.listaSesiones.currentItem() is not None and
                QtGui.QMessageBox.question(
                self, 'Confirmación',
                '¿Seguro que desea borrar la sesión "{}"?'.format(
                    self.listaSesiones.currentItem().text()),
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes):
            self.controlador.borrar_sesion(self.listaSesiones.currentItem())

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnEditarSesion_clicked(self):
        self.modo_edicion = not self.modo_edicion

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnLanzarAhora_clicked(self):
        self.controlador.lanzar_sesion(self.listaSesiones.currentItem())

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnGuardarCambios_clicked(self):
        if self.modo_creacion:
            self.controlador.guardar_cambios_sesion(None)
        else:
            self.controlador.guardar_cambios_sesion(
                self.listaSesiones.currentItem())
        self.modo_edicion = False
        self.modo_creacion = False

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnDescartarCambios_clicked(self):
        self.modo_edicion = False
        self.modo_creacion = False
        self.controlador.mostrar_detalles_sesion(
            self.listaSesiones.currentItem().text())

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnCargarTimbreInicial_clicked(self):
        archivo = self.abrir_archivo()
        if archivo:
            self.txtTimbreInicial.setText(archivo)
            duracion = 0
            with audioread.audio_open('{}/{}'.format(
                    configuracion.raiz_audio, archivo)) as f:
                duracion = int(f.duration)
            minuto, segundo = divmod(duracion, 60)
            hora, minuto = divmod(minuto, 60)
            self.duracionTimbreInicial.setTime(QtCore.QTime(hora, minuto,
                segundo))
            self.volumenTimbreInicial.setValue(80)

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnBorrarTimbreInicial_clicked(self):
        self.controlador.timbre_inicial = None

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnPruebaTimbreInicial_clicked(self):
        reproductor = self._reproductor_prueba_timbre_inicial
        if reproductor.reproduciendo:
            reproductor.parar()
            self.btnPruebaTimbreInicial.setIcon(self.play_icon)
        else:
            reproductor.archivo = self.txtTimbreInicial.text()
            reproductor.inicio = self.tiempoInicioTimbreInicial.time()
            reproductor.duracion = self.duracionTimbreInicial.time()
            reproductor.volumen = self.volumenTimbreInicial.value()
            self.btnPruebaTimbreInicial.setIcon(self.pause_icon)
            reproductor.reproducir()

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnCargarTimbreFinal_clicked(self):
        archivo = self.abrir_archivo()
        if archivo:
            self.txtTimbreFinal.setText(archivo)
            duracion = 0
            with audioread.audio_open('{}/{}'.format(
                    configuracion.raiz_audio, archivo)) as f:
                duracion = int(f.duration)
            minuto, segundo = divmod(duracion, 60)
            hora, minuto = divmod(minuto, 60)
            self.duracionTimbreFinal.setTime(QtCore.QTime(hora, minuto,
                segundo))
            self.volumenTimbreFinal.setValue(80)

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnBorrarTimbreFinal_clicked(self):
        self.controlador.timbre_final = None

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnPruebaTimbreFinal_clicked(self):
        reproductor = self._reproductor_prueba_timbre_final
        if reproductor.reproduciendo:
            reproductor.parar()
            self.btnPruebaTimbreFinal.setIcon(self.play_icon)
        else:
            reproductor.archivo = self.txtTimbreFinal.text()
            reproductor.inicio = self.tiempoInicioTimbreFinal.time()
            reproductor.duracion = self.duracionTimbreFinal.time()
            reproductor.volumen = self.volumenTimbreFinal.value()
            self.btnPruebaTimbreFinal.setIcon(self.pause_icon)
            reproductor.reproducir()

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnCargarTimbreMelodia_clicked(self):
        archivo = self.abrir_archivo()
        if archivo:
            self.txtTimbreMelodia.setText(archivo)
            duracion = 0
            with audioread.audio_open('{}/{}'.format(
                    configuracion.raiz_audio, archivo)) as f:
                duracion = int(f.duration)
            minuto, segundo = divmod(duracion, 60)
            hora, minuto = divmod(minuto, 60)
            self.duracionTimbreMelodia.setTime(QtCore.QTime(hora, minuto,
                segundo))
            self.volumenTimbreMelodia.setValue(80)

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnBorrarTimbreMelodia_clicked(self):
        self.controlador.timbre_melodia = None

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnPruebaTimbreMelodia_clicked(self):
        reproductor = self._reproductor_prueba_timbre_melodia
        if reproductor.reproduciendo:
            reproductor.parar()
            self.btnPruebaTimbreMelodia.setIcon(self.play_icon)
        else:
            reproductor.archivo = self.txtTimbreMelodia.text()
            reproductor.inicio = self.tiempoInicioTimbreMelodia.time()
            reproductor.duracion = self.duracionTimbreMelodia.time()
            reproductor.volumen = self.volumenTimbreMelodia.value()
            self.btnPruebaTimbreMelodia.setIcon(self.pause_icon)
            reproductor.reproducir()

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnCargarHiloMusical_clicked(self):
        pass

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnBorrarHiloMusical_clicked(self):
        pass

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_btnPruebaHiloMusical_clicked(self):
        pass

    @debug_slot_method(False)
    @QtCore.pyqtSlot(int)
    def on_volumenTimbreInicial_valueChanged(self, volumen):
        self.lblVolumenTimbreInicial.setNum(volumen)
        self._reproductor_prueba_timbre_inicial.volumen = volumen

    @debug_slot_method(False)
    @QtCore.pyqtSlot(int)
    def on_volumenTimbreFinal_valueChanged(self, volumen):
        self.lblVolumenTimbreFinal.setNum(volumen)
        self._reproductor_prueba_timbre_final.volumen = volumen

    @debug_slot_method(False)
    @QtCore.pyqtSlot(int)
    def on_volumenTimbreMelodia_valueChanged(self, volumen):
        self.lblVolumenTimbreMelodia.setNum(volumen)
        self._reproductor_prueba_timbre_melodia.volumen = volumen

    @debug_slot_method(False)
    @QtCore.pyqtSlot(int)
    def on_volumenHiloMusical_valueChanged(self, volumen):
        pass

    @debug_slot_method(False)
    @QtCore.pyqtSlot(bool)
    def on_chkHiloMusicalModoAleatorio_clicked(self, checked):
        pass

    @debug_slot_method(False)
    @QtCore.pyqtSlot(QtGui.QListWidgetItem, QtGui.QListWidgetItem)
    def on_listaSesiones_currentItemChanged(self, actual, anterior):
        #if actual is not None:
            #print('Sesión actual: {}'.format(actual.text()))
        if self.controlador is not None and actual is not None:
            nombre_sesion = actual.text()
            self.controlador.mostrar_detalles_sesion(nombre_sesion)

    def on_temporizador_timeout(self):
        if self.controlador is not None:
            self.controlador.comprobar_alarmas()
        self.setWindowTitle('TimbreGest - IES Almudeyne [{}]'.format(
            datetime.today().strftime('%d/%m/%Y - %H:%M:%S')))

    @debug_slot_method(False)
    def on_prueba_timbre_inicial_stateChanged(self, nuevo, antiguo):
        if nuevo in [Phonon.PlayingState]:
            self.btnPruebaTimbreInicial.setIcon(self.pause_icon)
        else:
            self.btnPruebaTimbreInicial.setIcon(self.play_icon)

    @debug_slot_method(False)
    def on_prueba_timbre_final_stateChanged(self, nuevo, antiguo):
        if nuevo in [Phonon.PlayingState]:
            self.btnPruebaTimbreFinal.setIcon(self.pause_icon)
        else:
            self.btnPruebaTimbreFinal.setIcon(self.play_icon)

    @debug_slot_method(False)
    def on_prueba_timbre_melodia_stateChanged(self, nuevo, antiguo):
        if nuevo in [Phonon.PlayingState]:
            self.btnPruebaTimbreMelodia.setIcon(self.pause_icon)
        else:
            self.btnPruebaTimbreMelodia.setIcon(self.play_icon)

    def abrir_archivo(self):
        archivo = QtGui.QFileDialog.getOpenFileName(
            self, 'Seleccionar archivo de audio',
            configuracion.raiz_audio, 'Archivos de audio (*.mp3 *.wav *.m4a)')
        if archivo is not None:
            return os.path.basename(archivo)
        else:
            return None


class Vista(object):
    winTimbreGest = None
    _controlador = None

    def __init__(self,):
        self._controlador = None
        self.winTimbreGest = WinTimbreGest()

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, controlador):
        self._controlador = controlador
        self.winTimbreGest.controlador = controlador
