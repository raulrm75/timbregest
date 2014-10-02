
from datetime import timedelta, date, datetime
from nptime import nptime
import audioread
import os.path
from itemproperties import itemproperty
import json
import configuracion
import os.path


class Timbre(object):
    _inicio = None
    _duracion = None
    _volumen = 0
    _archivo = ''
    _len = 0

    def __init__(self, archivo, **kwargs):
        self._inicio = None
        self._duracion = None
        self._volumen = 0
        self._archivo = ''
        self._len = 0
        archivo = '{}/{}'.format(configuracion.raiz_audio, archivo)
        if os.path.exists(archivo):
            self._archivo = archivo
        else:
            raise IOError('El archivo "{}" no existe'.format(archivo))

        with audioread.audio_open(archivo) as f:
            self._len = int(f.duration)

        if 'inicio' in kwargs:
            if isinstance(kwargs['inicio'], nptime):
                self._inicio = kwargs['inicio']
            else:
                self._inicio = nptime(kwargs['inicio'])
        else:
            self.inicio = nptime()

        if 'duracion' in kwargs:
            if isinstance(kwargs['duracion'], timedelta):
                self._duracion = kwargs['duracion']
            else:
                self._inicio = timedelta(kwargs['duracion'])
        else:
            self.duracion = self._len

        if 'volumen' in kwargs:
            self._volumen = min(100, abs(kwargs['volumen']))
        else:
            self._volumen = 50

    def __len__(self):
        return self._len

    def __str__(self):
        return '<Timbre: "{}" [{} --> {}] al {}%>'.format(
            self.archivo,
            str(self.inicio),
            str(self.inicio + self.duracion) if self.duracion is not None
                else 'final',
            self.volumen)

    @property
    def archivo(self):
        return os.path.basename(self._archivo)

    @archivo.setter
    def archivo(self, archivo):
        archivo = '{}/{}'.format(configuracion.raiz_audio, archivo)
        if os.path.exists(archivo):
            self._archivo = archivo
        else:
            raise IOError('El archivo "{}" no existe'.format(archivo))

    @property
    def inicio(self):
        if self._inicio is None:
            return nptime.nptime()
        else:
            return self._inicio

    @inicio.setter
    def inicio(self, inicio):
        if not isinstance(inicio, nptime):
            self._inicio = nptime(inicio)
        else:
            self._inicio = inicio

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        if isinstance(duracion, timedelta):
            duracion_segundos = duracion.total_seconds()
        elif isinstance(duracion, int) or isinstance(duracion, float):
            duracion_segundos = int(duracion)
        else:
            raise TypeError('La duración debe ser un "int", '
                '"float" o "timedelta"')

        duracion_segundos = min(self._len, duracion_segundos)
        if 0 < duracion_segundos:
            segundos = int(duracion_segundos) % 60
            minutos = (int(duracion_segundos - segundos) // 60) % 60
            horas = int(duracion_segundos - minutos * 60 - segundos) // 3600
            self._duracion = timedelta(
                hours=horas, minutes=minutos, seconds=segundos)
        else:
            self.duracion = self._len

    @property
    def volumen(self):
        return self._volumen

    @volumen.setter
    def volumen(self, volumen):
        self._volumen = min(100, abs(volumen))

    def __eq__(self, other):
        if isinstance(self, Timbre) and isinstance(other, Timbre):
            return all(map(lambda x: x[0] == x[1],
                zip(self.__dict__, other.__dict__)))
        else:
            return False

    def to_dict(self):
        return {
            'archivo': os.path.basename(self.archivo),
            'inicio': self.inicio.isoformat(),
            'duracion': self.duracion.total_seconds(),
            'volumen': self.volumen}

    @classmethod
    def from_dict(cls, timbre_json):
        if timbre_json is not None:
            timbre = Timbre(
                archivo=timbre_json['archivo'],
                inicio=nptime.from_time(datetime.strptime(timbre_json['inicio'],
                    '%H:%M:%S').time()),
                duracion=timedelta(seconds=timbre_json['duracion']),
                volumen=int(timbre_json['volumen']))
            #print('-' * 40)
            #print('Timbre cargado')
            #print(timbre)
            #print('-' * 40)
            return timbre
        else:
            return None


class Sesion(object):
    _descripcion = ''
    _activa = False
    _inicio = None
    _final = None
    _timbres = {'inicial': None, 'final': None, 'melodia': None}
    _hilo_musical = []
    _modo_aleatorio = False
    _repetir = []

    def __init__(self, descripcion, inicio, final, timbre_inicial, **kwargs):
        assert isinstance(descripcion, str)
        assert isinstance(inicio, nptime)
        assert isinstance(final, nptime)
        assert isinstance(timbre_inicial, Timbre)
        self._descripcion = descripcion
        self._inicio = inicio
        self._final = final
        self._timbres = {'inicial': None, 'final': None, 'melodia': None}
        self._timbres['inicial'] = timbre_inicial

        if 'timbre_final' in kwargs:
            assert (isinstance(kwargs['timbre_final'], Timbre) or
                kwargs['timbre_final'] is None)
            self._timbres['final'] = kwargs['timbre_final']
        else:
            self._timbres['final'] = None

        if 'timbre_melodia' in kwargs:
            assert (isinstance(kwargs['timbre_melodia'], Timbre) or
                kwargs['timbre_melodia'] is None)
            self._timbres['melodia'] = kwargs['timbre_melodia']
        else:
            self._timbres['melodia'] = None

        if 'hilo_musical' in kwargs:
            assert all(isinstance(timbre, Timbre) for timbre in
                kwargs['hilo_musical'])
            self._hilo_musical = list(kwargs['hilo_musical'])
        else:
            self._hilo_musical = []

        if 'modo_aleatorio' in kwargs:
            assert isinstance(kwargs['modo_aleatorio'], bool)
            self._modo_aleatorio = kwargs['modo_aleatorio']
        else:
            self._modo_aleatorio = False

        if 'repetir' in kwargs:
            assert all(0 <= d < 7 for d in kwargs['repetir'])
            self._repetir = list(set(kwargs['repetir']))
        else:
            self._repetir = [date.today().weekday()]    # 0 es lunes

        if 'activa' in kwargs:
            assert isinstance(kwargs['activa'], bool)
            self._activa = kwargs['activa']

    def __str__(self):
        return '''
    Sesión "{}" de {} a {}. Repetir: {}.
    Timbres:
        - inicial: {},
        - melodía: {},
        - final: {}.
    Hilo musical:
        - {}
        Modo de reproducción aleatorio: {}
    '''.format(
        self._descripcion,
        str(self._inicio),
        str(self._final),
        '[{}]'.format(', '.join(['L', 'M', 'X', 'J', 'V', 'S', 'D'][d] for d in
            self._repetir)),
        str(self._timbres['inicial']),
        str(self._timbres['melodia']) if self._timbres['melodia'] is not None
            else 'N/A',
        str(self._timbres['final']) if self._timbres['final'] is not None
            else 'N/A',
        '\n\t- '.join(str(pista) for pista in self._hilo_musical) if
            self._hilo_musical else 'N/A',
        str(self.modo_aleatorio))

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def inicio(self):
        return self._inicio

    @inicio.setter
    def inicio(self, inicio):
        assert isinstance(inicio, nptime)
        self._inicio = inicio

    @property
    def final(self):
        return self._final

    @final.setter
    def final(self, final):
        assert isinstance(final, nptime)
        self._final = final

    @property
    def duracion(self):
        return self._final - self._inicio

    @itemproperty
    def timbre(self, indice):
        if isinstance(indice, str) and indice.lower() in (
                'inicial', 'final', 'melodia'):
            return self._timbres[indice]
        else:
            raise IndexError('Índice erróneo de acceso a timbres. '
                '{}'.format(indice))

    @timbre.setter
    def timbre(self, indice, valor):
        assert isinstance(valor, Timbre)
        if isinstance(indice, str) and indice.lower() in (
                'inicial', 'final', 'melodia'):
            self._timbres[indice] = valor
        else:
            raise IndexError('Índice erróneo de acceso a timbres: '
                '{}.'.format(indice))

    @property
    def hilo_musical(self):
        return self._hilo_musical

    @property
    def repetir(self):
        return self._repetir

    @property
    def modo_aleatorio(self):
        return self._modo_aleatorio

    @modo_aleatorio.setter
    def modo_aleatorio(self, modo):
        assert isinstance(modo, bool)
        self._modo_aleatorio = modo

    @property
    def activa(self):
        return self._activa

    @activa.setter
    def activa(self, valor):
        assert isinstance(valor, bool)
        self._activa = valor

    def __eq__(self, other):
        if isinstance(self, Sesion) and isinstance(other, Sesion):
            return all(map(lambda x: x[0] == x[1],
                zip(self.__dict__, other.__dict__)))
        else:
            return False

    def to_dict(self):
        return {
            'descripcion': self.descripcion,
            'inicio': self.inicio.isoformat(),
            'final': self.final.isoformat(),
            'activa': self.activa,
            'repetir': self.repetir,
            'timbres': {
                'inicial': self.timbre['inicial'].to_dict(),
                'melodia': self.timbre['melodia'].to_dict() if
                    self.timbre['melodia'] is not None else None,
                'final': self.timbre['final'].to_dict() if
                    self.timbre['final'] is not None else None},
            'hilo_musical': [pista.to_dict() for pista in self.hilo_musical],
            'modo_aleatorio': self.modo_aleatorio
            }

    @classmethod
    def from_dict(cls, sesion_json):
        if sesion_json is not None:
            sesion = Sesion(
                descripcion=sesion_json['descripcion'],
                inicio=nptime.from_time(datetime.strptime(sesion_json['inicio'],
                    '%H:%M:%S').time()),
                final=nptime.from_time(datetime.strptime(sesion_json['final'],
                    '%H:%M:%S').time()),
                timbre_inicial=Timbre.from_dict(
                    sesion_json['timbres']['inicial']),
                timbre_final=Timbre.from_dict(
                    sesion_json['timbres']['final']),
                timbre_melodia=Timbre.from_dict(
                    sesion_json['timbres']['melodia']),
                repetir=sorted(sesion_json['repetir']),
                activa=sesion_json['activa'])
            return sesion
        else:
            return None


class Sesiones(object):
    _sesiones = []
    _indice_sesiones = {}

    def __init__(self):
        self._sesiones = []
        self._indice_sesiones = {}

    def append(self, sesion):
        assert isinstance(sesion, Sesion)
        #print('-' * 40)
        #print('Se va a añadir la seión')
        #print(sesion)
        #print('-' * 30)
        self._sesiones.append(sesion)
        #print('-' * 40)
        #print('Sesión añadida')
        #print(self._sesiones[-1])
        #print('-' * 40)
        self._sesiones.sort(key=lambda sesion: sesion.inicio)
        #print('-' * 40)
        #print('Índice se sesiones antes de añadir la sesión')
        #print(self._indice_sesiones)
        #print('-' * 40)
        self._indice_sesiones = {sesion.descripcion: indice for
            (indice, sesion) in enumerate(self._sesiones)}
        #print('-' * 40)
        #print('Índice se sesiones después de añadir la sesión')
        #print(self._indice_sesiones)
        #print('-' * 40)
        #print('Sesión añadida (accedida por descripción')
        #print(self[sesion.descripcion])
        #print('-' * 40)
        #print('Lista actual de sesiones')
        #for sesion in self:
            #print(sesion)
        #print('-' * 40)

    def buscar_sesion(self, inicio, final=None):
        if final is None:
            final = inicio
        assert isinstance(inicio, nptime)
        return [sesion for sesion in self._sesiones if
            inicio <= sesion.inicio <= final]

    def remove(self, sesion):
        self._sesiones.remove(sesion)

    def __iter__(self):
        for sesion in self._sesiones:
            yield sesion

    def __contains__(self, sesion):
        if isinstance(sesion, Sesion):
            return sesion in self._sesiones
        else:
            return False

    def __getitem__(self, indice):
        if isinstance(indice, int):
            return self._sesiones[indice]
        elif isinstance(indice, str):
            if indice in self._indice_sesiones:
                return self._sesiones[self._indice_sesiones[indice]]
            else:
                return None
        else:
            return None

    def __setitem__(self, indice, sesion):
        assert isinstance(sesion, Sesion) or sesion is None
        if isinstance(indice, int):
            if sesion is not None:
                self._sesiones[indice] = sesion
            else:
                del self._sesiones[indice]
        elif isinstance(indice, str):
            if indice in self._indice_sesiones:
                self[self._indice_sesiones[indice]] = sesion
            elif sesion is not None:
                self.append(sesion)
            else:
                raise ValueError('No se puede insertar una sesión nula.')
        else:
            raise IndexError('Sesión no existe: {}'.format(
                indice))

    def to_dict(self):
        return [sesion.to_dict() for sesion in self._sesiones]

    @classmethod
    def from_dict(cls, json_dict):
        if json_dict is not None:
            sesiones = Sesiones()
            for sesion in json_dict:
                sesiones.append(Sesion.from_dict(sesion))
            return sesiones
        else:
            return None

    def __len__(self):
        return len(self._sesiones)

    @property
    def sesiones(self):
        return self._sesiones

    def guardar(self, nombre_archivo):
        with open(nombre_archivo, 'w') as f:
            f.write(json.dumps(self.to_dict(), sort_keys=True, indent=4))

    def cargar(self, nombre_archivo):
        self._sesiones = []
        with open(nombre_archivo, 'r') as f:
            for sesion_json in json.loads(f.read()):
                sesion = Sesion.from_dict(sesion_json)
                #print('-' * 40)
                #print('Sesión cargada')
                #print(sesion)
                #print('-' * 40)
                # Aquí la sesión se ha cargado correctamente
                self.append(sesion)
                # Aquí la sesión ya no es correcta
        #print('-' * 40)
        #print('Sesiones cargadas')
        #for sesion in self._sesiones:
            #print(sesion)
        #print('-' * 40)

    def __eq__(self, other):
        if isinstance(other, Sesiones):
            key = lambda sesion: sesion.descripcion
            return sorted(self.sesiones, key=key) == sorted(other.sesiones,
                key=key)
        else:
            return False


class Modelo(object):
    sesiones = None
    controlador = None

    def __init__(self,):
        self.sesiones = Sesiones()

    def cargar_datos(self):
        path, _ = os.path.split(__file__)
        self.sesiones.cargar('{}/datos.json'.format(path))
        self.cargar_alarmas()
        #print('-' * 40)
        #print('Sesiones cargadas')
        #for sesion in self.sesiones:
            #print(sesion)
        #print('-' * 40)
        if self.controlador is not None:
            self.controlador.cargar_datos()

    def guardar_datos(self):
        path, _ = os.path.split(__file__)
        self.sesiones.guardar('{}/datos.json'.format(path))

    def cargar_alarmas(self):
        self._alarmas = {dia: {} for dia in range(7)}
        for sesion in self.sesiones:
            if sesion.activa:
                for dia in sesion.repetir:
                    T = sesion.timbre['inicial']
                    hora = sesion.inicio
                    self._alarmas[dia][hora.strftime('%H:%M:%S')] = T
                    hora = hora + T.duracion

                    T = sesion.timbre['melodia']
                    if T is not None:
                        self._alarmas[dia][hora.strftime('%H:%M:%S')] = T
                        hora = hora + T.duracion

                    T = sesion.timbre['final']
                    if T is not None:
                        self._alarmas[dia][hora.strftime('%H:%M:%S')] = T

    def sonar_alarma(self, dia, hora):
        return (self._alarmas and dia in self._alarmas and
            hora.strftime('%H:%M:%S') in self._alarmas[dia])

    @property
    def alarmas(self):
        return self._alarmas
