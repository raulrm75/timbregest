from PyQt4.phonon import Phonon
from PyQt4 import QtCore, QtGui
import audioread
from modelo import Timbre
from nptime import nptime
from datetime import timedelta
from functools import wraps
import configuracion
import os.path


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


class ReproductorTimbre(QtCore.QObject):
    _avanzado = False
    _archivo = None
    _inicio = 0
    _duracion = 0
    _timbres = []
    _timbre_actual = -1

    def __init__(self, parent):
        assert isinstance(parent, QtGui.QWidget)
        super(QtCore.QObject, self).__init__

        self._salida = Phonon.AudioOutput(Phonon.MusicCategory, parent)
        self._medio = Phonon.MediaObject(parent)
        Phonon.createPath(self._medio, self._salida)
        self._medio.setTickInterval(1000)
        self._medio.seekableChanged.connect(self.on_medio_seekableChanged)
        self._medio.tick.connect(self.on_medio_tick)
        self._medio.finished.connect(self.on_medio_finished)

        self._avanzado = False
        self._archivo = None
        self._inicio = 0
        self._duracion = 0
        self._timbres = []
        self._timbre_actual = -1

    @debug_slot_method(False)
    @QtCore.pyqtSlot(bool)
    def on_medio_seekableChanged(self, estado):
        if estado:
            if not self._avanzado:
                self._medio.seek(self.inicio)
                self._avanzado = True

    @debug_slot_method(False)
    @QtCore.pyqtSlot(int)
    def on_medio_tick(self, tiempo):
        if tiempo >= self.final:
            self._medio.stop()

    @debug_slot_method(False)
    @QtCore.pyqtSlot()
    def on_medio_finished(self):
        self._timbre_actual += 1
        try:
            self.timbre = self._timbres[self._timbre_actual]
            print('Siguiente timbre')
            print(self._timbres[self._timbre_actual])
            print('Frente a')
            print(self.timbre)
            self._medio.play()
        except IndexError:
            pass

    def reproducir(self):
        self._medio.play()

    def parar(self):
        self._medio.stop()
        self._avanzado = False

    @property
    def volumen(self):
        return int(self._salida.volume() * 100)

    @volumen.setter
    def volumen(self, valor):
        assert isinstance(valor, int) and 0 <= valor <= 100
        self._salida.setVolume(valor / 100)

    @property
    def inicio(self):
        return self._inicio

    @inicio.setter
    def inicio(self, inicio):
        self._avanzado = False
        if isinstance(inicio, int):
            self._inicio = inicio
        elif isinstance(inicio, nptime):
            self._inicio = (inicio.minute * 60 + inicio.second) * 1000
        elif isinstance(inicio, QtCore.QTime):
            self._inicio = (inicio.minute() * 60 + inicio.second()) * 1000
        else:
            raise ValueError('avance debe ser un "int", un "nptime", '
                'o un "QTime".')

    @property
    def final(self):
        return self._inicio + self._duracion

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        if isinstance(duracion, int):
            self._duracion = duracion
        elif isinstance(duracion, timedelta):
            self._duracion = duracion.seconds * 1000
        elif isinstance(duracion, QtCore.QTime):
            self._duracion = (duracion.minute() * 60 + duracion.second()) * 1000
        else:
            raise ValueError('duracion debe ser un "int", un "timedelta" o '
                'un "QTime".')

    @property
    def archivo(self):
        return self._archivo

    @archivo.setter
    def archivo(self, nombre_archivo):
        assert isinstance(nombre_archivo, str)
        self._archivo = '{}/{}'.format(configuracion.raiz_audio, nombre_archivo)
        self._medio.setCurrentSource(Phonon.MediaSource(self._archivo))
        with audioread.audio_open(self._archivo) as f:
            self._duracion = int(f.duration * 1000)
        self.inicio = 0
        self._avanzado = False

    @property
    def reproduciendo(self):
        return self._medio.state() == Phonon.PlayingState

    @property
    def estado(self):
        return self._medio.state()

    @property
    def timbre(self):
        return Timbre(
            archivo=os.path.basename(self._archivo),
            inicio=nptime(
                hour=self._inicio // 3600000,
                minute=(self.inicio // 60000) % 60,
                second=(self.inicio // 1000) % 60),
            duracion=timedelta(seconds=self.duracion // 1000))

    @timbre.setter
    def timbre(self, timbre):
        assert isinstance(timbre, Timbre)
        self.archivo = timbre.archivo
        self.inicio = timbre.inicio
        self.duracion = timbre.duracion
        self.volumen = timbre.volumen

    def __str__(self):
        return '<Reproductor: "{}" [{} ms --> {} ms] al {}%>{}'.format(
            self.archivo,
            str(self.inicio),
            str(self.inicio + self.duracion) if self.duracion is not None
                else 'final',
            self.volumen,
            ' Reproduciendo.' if self.reproduciendo else '')

    def append(self, timbre):
        if timbre is not None:
            self._timbres.append(timbre)

    @property
    def timbres(self):
        return self._timbres

    @timbres.setter
    def timbres(self, cola):
        self._timbres = cola

    def reproducir_todo(self):
        print('Se van a reproducir')
        for timbre in self._timbres:
            print(timbre)
        self._timbre_actual = 0
        self.timbre = self._timbres[self._timbre_actual]
        self._medio.play()
