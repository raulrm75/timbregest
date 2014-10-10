from PyQt4 import QtCore
#from PyQt4.phonon import Phonon
import modelo
from nptime import nptime
from datetime import timedelta, datetime
#from reproductor import ReproductorTimbre
import dbus
import configuracion


def QTime_to_nptime(valor):
    return nptime(hour=valor.hour(), minute=valor.minute(),
        second=valor.second())


def nptime_to_QTime(valor):
    return QtCore.QTime(valor.hour, valor.minute, valor.second)


def QTime_to_timedelta(valor):
    return timedelta(hours=valor.hour(), minutes=valor.minute(),
        seconds=valor.second())


def timedelta_to_QTime(valor):
    return QtCore.QTime(0, *divmod(valor.seconds, 60))


class Controlador(object):
    modelo = None
    vista = None
    #_hilo_musical = []

    def __init__(self):
        self.modelo = None
        self.vista = None
        self.dia_creacion = None
        self.alarmas = {}

    def cargar_datos(self):
        if self.modelo is not None and self.vista is not None:
            self.vista.winTimbreGest.listaSesiones.clear()
            sesiones = sorted([sesion.descripcion for sesion in
                self.modelo.sesiones])
            self.vista.winTimbreGest.listaSesiones.addItems(sesiones)

    @property
    def timbre_inicial(self):
        form = self.vista.winTimbreGest
        archivo = form.txtTimbreInicial.text()
        if archivo:
            inicio = QTime_to_nptime(form.tiempoInicioTimbreInicial.time())
            duracion = QTime_to_timedelta(form.duracionTimbreInicial.time())
            volumen = form.volumenTimbreInicial.value()
            return modelo.Timbre(
                archivo=archivo,
                inicio=inicio,
                duracion=duracion,
                volumen=volumen)
        else:
            return None

    @timbre_inicial.setter
    def timbre_inicial(self, timbre):
        assert isinstance(timbre, modelo.Timbre) or timbre is None
        if timbre is not None:
            form = self.vista.winTimbreGest
            form.txtTimbreInicial.setText(timbre.archivo)
            form.tiempoInicioTimbreInicial.setTime(
                nptime_to_QTime(timbre.inicio))
            form.duracionTimbreInicial.setTime(
                timedelta_to_QTime(timbre.duracion))
            form.volumenTimbreInicial.setValue(timbre.volumen)
        else:
            form = self.vista.winTimbreGest
            form.txtTimbreInicial.setText('')
            form.tiempoInicioTimbreInicial.setTime(QtCore.QTime(0, 0, 0))
            form.duracionTimbreInicial.setTime(QtCore.QTime(0, 0, 0))
            form.volumenTimbreInicial.setValue(0)

    @property
    def timbre_final(self):
        form = self.vista.winTimbreGest
        archivo = form.txtTimbreFinal.text()
        if archivo:
            inicio = QTime_to_nptime(form.tiempoInicioTimbreFinal.time())
            duracion = QTime_to_timedelta(form.duracionTimbreFinal.time())
            volumen = form.volumenTimbreFinal.value()
            return modelo.Timbre(
                archivo=archivo,
                inicio=inicio,
                duracion=duracion,
                volumen=volumen)
        else:
            return None

    @timbre_final.setter
    def timbre_final(self, timbre):
        assert isinstance(timbre, modelo.Timbre) or timbre is None
        if timbre is not None:
            form = self.vista.winTimbreGest
            form.txtTimbreFinal.setText(timbre.archivo)
            form.tiempoInicioTimbreFinal.setTime(
                nptime_to_QTime(timbre.inicio))
            form.duracionTimbreFinal.setTime(
                timedelta_to_QTime(timbre.duracion))
            form.volumenTimbreFinal.setValue(timbre.volumen)
        else:
            form = self.vista.winTimbreGest
            form.txtTimbreFinal.setText('')
            form.tiempoInicioTimbreFinal.setTime(QtCore.QTime(0, 0, 0))
            form.duracionTimbreFinal.setTime(QtCore.QTime(0, 0, 0))
            form.volumenTimbreFinal.setValue(0)

    @property
    def timbre_melodia(self):
        form = self.vista.winTimbreGest
        archivo = form.txtTimbreMelodia.text()
        if archivo:
            inicio = QTime_to_nptime(form.tiempoInicioTimbreMelodia.time())
            duracion = QTime_to_timedelta(form.duracionTimbreMelodia.time())
            volumen = form.volumenTimbreMelodia.value()
            return modelo.Timbre(
                archivo=archivo,
                inicio=inicio,
                duracion=duracion,
                volumen=volumen)
        else:
            return None

    @timbre_melodia.setter
    def timbre_melodia(self, timbre):
        assert isinstance(timbre, modelo.Timbre) or timbre is None
        if timbre is not None:
            form = self.vista.winTimbreGest
            form.txtTimbreMelodia.setText(timbre.archivo)
            form.tiempoInicioTimbreMelodia.setTime(
                nptime_to_QTime(timbre.inicio))
            form.duracionTimbreMelodia.setTime(
                timedelta_to_QTime(timbre.duracion))
            form.volumenTimbreMelodia.setValue(timbre.volumen)
        else:
            form = self.vista.winTimbreGest
            form.txtTimbreMelodia.setText('')
            form.tiempoInicioTimbreMelodia.setTime(QtCore.QTime(0, 0, 0))
            form.duracionTimbreMelodia.setTime(QtCore.QTime(0, 0, 0))
            form.volumenTimbreMelodia.setValue(0)


    @property
    def sesion(self):
        form = self.vista.winTimbreGest
        descripcion = form.txtDescripcion.text()
        inicio = QTime_to_nptime(form.horaInicioSesion.time())
        final = QTime_to_nptime(form.horaFinalSesion.time())
        timbre_inicial = self.timbre_inicial
        timbre_final = self.timbre_final
        timbre_melodia = self.timbre_melodia
        activa = form.sesion_activa
        repetir = [dia for dia in range(7) if form.repetir[dia]]
        modo_aleatorio = form.modo_aleatorio
        #hilo_musical = self.hilo_musical
        return modelo.Sesion(
            descripcion=descripcion,
            inicio=inicio,
            final=final,
            timbre_inicial=timbre_inicial,
            timbre_melodia=timbre_melodia,
            timbre_final=timbre_final,
            modo_aleatorio=modo_aleatorio,
            repetir=repetir,
            activa=activa)

    @sesion.setter
    def sesion(self, sesion):
        assert isinstance(sesion, modelo.Sesion) or sesion is None
        form = self.vista.winTimbreGest
        if sesion is not None:
            form.txtDescripcion.setText(sesion.descripcion)
            form.horaInicioSesion.setTime(nptime_to_QTime(
                sesion.inicio))
            form.horaFinalSesion.setTime(nptime_to_QTime(
                sesion.final))
            for dia in range(7):
                form.repetir[dia] = (dia in sesion.repetir)
            self.timbre_inicial = sesion.timbre['inicial']
            self.timbre_final = sesion.timbre['final']
            self.timbre_melodia = sesion.timbre['melodia']
            #self.hilo_musical = sesion.hilo_musical
            form.modo_aleatorio = sesion.modo_aleatorio
            form.sesion_activa = sesion.activa
        else:
            form.txtDescripcion.setText('')
            form.horaInicioSesion.setTime(QtCore.QTime(0, 0))
            form.horaFinalSesion.setTime(QtCore.QTime(0, 0))
            for dia in range(7):
                form.repetir[dia] = False
            self.timbre_inicial = None
            self.timbre_melodia = None
            self.timbre_final = None
            #self.hilo_musical = []
            form.modo_aleatorio = False
            form.sesion_activa = False

    def mostrar_detalles_sesion(self, nombre_sesion):
        self.sesion = None
        self.sesion = self.modelo.sesiones[nombre_sesion]
        #print(self.sesion)

    def guardar_cambios_sesion(self, item_actual=None):
        if self.modelo is not None and self.vista is not None:
            if item_actual is None:
                self.modelo.sesiones[self.sesion.descripcion] = self.sesion
            else:
                self.modelo.sesiones[item_actual.text()] = self.sesion
            self.modelo.guardar_datos()
            self.modelo.cargar_datos()

    def borrar_sesion(self, item_actual):
        if self.modelo is not None and self.vista is not None:
            if item_actual is not None:
                self.modelo.sesiones[item_actual.text()] = None
            self.modelo.guardar_datos()
            self.modelo.cargar_datos()

    def comprobar_alarmas(self):
        hora_actual = nptime.from_time(datetime.today().time())
        dia_actual = datetime.today().weekday()
        fecha_actual = datetime.today().strftime('%d/%m/%Y')
        if self.modelo.sonar_alarma(dia_actual, hora_actual):
            reproductor = self.vista.winTimbreGest._reproductor_alarma
            reproductor.timbre = self.modelo.alarmas[dia_actual][
                hora_actual.strftime('%H:%M:%S')]
            reproductor.reproducir()
        if hora_actual.strftime('%H:%M:%S') == configuracion.hora_apagado:
            self.apagar('apagado ordinario')
        if not self.modelo.alarmas[dia_actual]:
            self.apagar('no hay alarmas definidas')
        if fecha_actual in configuracion.dias_libres:
            self.apagar('día libre')

    def lanzar_sesion(self, item_actual):
        if item_actual is not None:
            sesion = self.modelo.sesiones[item_actual.text()]
            reproductor = self.vista.winTimbreGest._reproductor_alarma
            reproductor.timbres = []
            reproductor.append(sesion.timbre['inicial'])
            reproductor.append(sesion.timbre['melodia'])
            reproductor.append(sesion.timbre['final'])
            reproductor.reproducir_todo()

    def apagar(self, msg=''):
        sys_bus = dbus.SystemBus()
        ck_srv = sys_bus.get_object('org.freedesktop.ConsoleKit',
            '/org/freedesktop/ConsoleKit/Manager')
        ck_iface = dbus.Interface(ck_srv, 
            'org.freedesktop.ConsoleKit.Manager')
        stop_method = ck_iface.get_dbus_method("Stop")
        print('Apagando el sistema por {}...'.format(msg))
        stop_method()
