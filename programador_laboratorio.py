from threading import Lock
from modelos.turno import Turno
from datetime import timedelta

class ProgramadorLaboratorio:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ProgramadorLaboratorio, cls).__new__(cls)
                cls._instance.turnos = []
                cls._instance.inicializar_turnos()
        return cls._instance

    def inicializar_turnos(self):
        # Este método inicializa los turnos para el día. Se debe llamar una vez al día.
        # Aquí se podrían cargar turnos desde una base de datos o crearlos si es la primera vez.
        # Por ahora, crearemos turnos de ejemplo para las horas de operación del laboratorio.
        horas_de_operacion = range(7, 16)  # De 7 a.m. a 4 p.m. (última cita a las 3:40 p.m.)
        for hora in horas_de_operacion:
            for minuto in (0, 20, 40):  # Turnos cada 20 minutos
                self.turnos.append(Turno(hora=hora, minuto=minuto))

    def reservar_turno(self, paciente, examen, fecha_hora):
        # Busca un turno disponible que coincida con la fecha y hora solicitadas.
        for turno in self.turnos:
            if turno.esta_disponible and turno.coincide_con(fecha_hora) and examen.esta_disponible_en(fecha_hora):
                turno.reservar(paciente)
                return True
        return False

    def obtener_turnos_disponibles(self, examen, fecha):
        # Retorna una lista de turnos disponibles para un examen en una fecha específica.
        turnos_disponibles = []
        for turno in self.turnos:
            if turno.esta_disponible and turno.es_en_fecha(fecha) and examen.esta_disponible_en(turno.hora):
                turnos_disponibles.append(turno)
        return turnos_disponibles
