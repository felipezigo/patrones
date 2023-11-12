from datetime import datetime, timedelta
from modelos.paciente import Paciente
from modelos.examen import Examen
from modelos.turno  import Turno
from datetime import datetime, timedelta
from operator import itemgetter

class FachadaReserva:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(FachadaReserva, cls).__new__(cls)
            cls._instance.citas = []
            cls._instance.fecha = []
        return cls._instance

    def crear_turno(self, fecha, hora, id_paciente, examen):
        if not self.turno_horario_laboral(fecha, hora):
            raise ValueError(f"EL horario planteado se encuentra fuera del horario laboral")
        
        if self.turno_20_minutos_libre(fecha,hora,examen):
            raise ValueError(f"No existe espacio en la agenda en el horario que plantea")
        
        if self.es_feriado(fecha):
            raise ValueError("No se han realizado cambios, es día feriado")

        if self.tiene_cita_repetida(fecha,id_paciente, examen):
            raise ValueError("Ya tiene cita en el mismo examen")

        if self.turno_disponible(fecha,hora,examen):
            raise ValueError(f"No hay disponibilidad del examen de {examen} en ese horario")
        
        datos_combinados = list(zip(self.citas, self.fecha))
        datos_ordenados = sorted(datos_combinados, key=itemgetter(1, 0))

        datos_ordenados_separados = [list(x) for x in zip(*datos_ordenados)]

        citas_agrupadas = {}
        for fecha, cita in zip(datos_ordenados_separados[1], datos_ordenados_separados[0]):
            if fecha in citas_agrupadas:
                citas_agrupadas[fecha].append(cita)
            else:
                citas_agrupadas[fecha] = [cita]

        for fecha, citas_en_fecha in citas_agrupadas.items():
            print(fecha)
            for cita in citas_en_fecha:
                print(cita)
                
    def es_feriado(self, fecha):
        fecha_a_verificar = fecha[5:]
        if fecha_a_verificar=='08-10' or fecha_a_verificar=='11-03':
            return True
        else:
            return False

    def tiene_cita_repetida(self, fecha, idPaciente, examen):
        return any(Turno.turnos[indice].fecha == fecha and Paciente.pacientes[indice].idDocumentoPaciente == idPaciente and Examen.examenes[indice].tipo == examen for indice in range(len(Paciente.pacientes)-2,0))

    def turno_disponible(self, fecha, hora, examen):
        return any(Turno.turnos[indice].fecha == fecha and Turno.turnos[indice].hora == hora and Examen.examenes[indice].tipo==examen for indice in range(len(Turno.turnos)-2,0))

    def turno_20_minutos_libre(self, fecha, hora, examen):
        hora_inicio = datetime.strptime(hora, "%H:%M").time()

        hora_fin = (datetime.strptime(hora, "%H:%M") + timedelta(minutes=20)).time()

        for indice in range(len(Turno.turnos)):
            hora_turno = datetime.strptime(Turno.turnos[indice].hora, "%H:%M").time()
            if (
                Turno.turnos[indice].fecha == fecha
                and Examen.examenes[indice].tipo == examen
                and hora_turno >= hora_inicio
                and hora_turno < hora_fin
            ):
                break    
    
    def turno_horario_laboral(self, fecha, hora):
        hora_laboral_inicio = datetime.strptime("07:00", "%H:%M")
        hora_laboral_fin = datetime.strptime("16:00", "%H:%M")
        fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
        hora_turno = datetime.strptime(hora, "%H:%M")

        dia_semana = fecha_obj.weekday()

        return (
            dia_semana >= 0 and  # Lunes (0)
            dia_semana <= 4 and  # Viernes (4)
            hora_laboral_inicio <= hora_turno <= hora_laboral_fin
        )
 
    def imprimir_citas_y_fechas(self,indice):
        if (indice==-1):
            self.fecha.pop()
            self.citas.pop() 
        citas_agrupadas = {}
        for fecha, cita in zip(self.fecha, self.citas):
            if fecha in citas_agrupadas:
                citas_agrupadas[fecha].append(cita)
            else:
                citas_agrupadas[fecha] = [cita]

        for fecha, citas_en_fecha in citas_agrupadas.items():
            print(fecha)
            for cita in citas_en_fecha:
                print(cita)