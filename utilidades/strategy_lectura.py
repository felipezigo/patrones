import abc
from modelos.turno import Turno
from modelos.paciente import Paciente
from modelos.apoderado import Apoderado
from modelos.examen import Examen
from utilidades.facade_reserva import FachadaReserva

class EstrategiaLectura(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def leer_linea_archivo(self, fecha, datos_cita):
    pass
class EstrategiaLecturaAgendadas(EstrategiaLectura):
  def leer_linea_archivo(self, fechaExamen, datos_cita):
    divisionDatos = datos_cita.strip().split("|")
    divisionDatossinEspacios = [elemento for elemento in divisionDatos if elemento is not None and elemento != ""]
    horaExamen = divisionDatossinEspacios[0]
    tipoExamenLaboratorio = divisionDatossinEspacios[1].strip()
    categoriaExamenLaboratorio = divisionDatossinEspacios[2]
    nombrePaciente = divisionDatossinEspacios[3]
    tipoPaciente = divisionDatossinEspacios[4]
    tipoDocumentoPaciente = divisionDatossinEspacios[5]
    idDocumentoPaciente = divisionDatossinEspacios[6]
    telefonoPaciente = divisionDatossinEspacios[7]
    fechaNacimientoPaciente = divisionDatossinEspacios[8]
    
    Turno.agregar_turno(fechaExamen, horaExamen, False)
    Examen.agregar_examen(tipoExamenLaboratorio, categoriaExamenLaboratorio)
   
    FachadaReserva()._instance.fecha.append(fechaExamen)
    FachadaReserva()._instance.citas.append(datos_cita)

    if len(divisionDatossinEspacios)>9:
        tipoApoderado = divisionDatossinEspacios[10]
        nombreApoderado = divisionDatossinEspacios[11]
        tipoDocumentoApoderado = divisionDatossinEspacios[12]
        fechaNacimientoApoderado = divisionDatossinEspacios[13]
        Paciente.agregar_paciente(nombrePaciente, tipoPaciente, tipoDocumentoPaciente, idDocumentoPaciente, telefonoPaciente, fechaNacimientoPaciente, True)
        Apoderado.agregar_apoderado(tipoApoderado,nombreApoderado,tipoDocumentoApoderado,fechaNacimientoApoderado,idDocumentoPaciente)
    else:
        Paciente.agregar_paciente(nombrePaciente, tipoPaciente, tipoDocumentoPaciente, idDocumentoPaciente, telefonoPaciente, fechaNacimientoPaciente, False)
        
       
class EstrategiaLecturaNuevas(EstrategiaLectura):
  def leer_linea_archivo(self, datos_cita):
    divisionDatos = datos_cita.strip().split("|")
    divisionDatossinEspacios = [elemento for elemento in divisionDatos if elemento is not None and elemento != ""]
    fechaExamen = divisionDatossinEspacios[0]
    horaExamen = divisionDatossinEspacios[1]
    tipoExamenLaboratorio = divisionDatossinEspacios[2].strip()
    categoriaExamenLaboratorio = divisionDatossinEspacios[3]
    nombrePaciente = divisionDatossinEspacios[4]
    tipoPaciente = divisionDatossinEspacios[5]
    tipoDocumentoPaciente = divisionDatossinEspacios[6]
    idDocumentoPaciente = divisionDatossinEspacios[7]
    telefonoPaciente = divisionDatossinEspacios[8]
    fechaNacimientoPaciente = divisionDatossinEspacios[9]
    
    Turno.agregar_turno(fechaExamen, horaExamen, False)
    Examen.agregar_examen(tipoExamenLaboratorio, categoriaExamenLaboratorio)
   
    FachadaReserva()._instance.fecha.append(fechaExamen)
    FachadaReserva()._instance.citas.append(datos_cita[11:])

    if len(divisionDatossinEspacios)>10:
        tipoApoderado = divisionDatossinEspacios[11]
        nombreApoderado = divisionDatossinEspacios[12]
        tipoDocumentoApoderado = divisionDatossinEspacios[13]
        fechaNacimientoApoderado = divisionDatossinEspacios[14]
        Paciente.agregar_paciente(nombrePaciente, tipoPaciente, tipoDocumentoPaciente, idDocumentoPaciente, telefonoPaciente, fechaNacimientoPaciente, True)
        Apoderado.agregar_apoderado(tipoApoderado,nombreApoderado,tipoDocumentoApoderado,fechaNacimientoApoderado,idDocumentoPaciente)
    else:
        Paciente.agregar_paciente(nombrePaciente, tipoPaciente, tipoDocumentoPaciente, idDocumentoPaciente, telefonoPaciente, fechaNacimientoPaciente, False)
    FachadaReserva().crear_turno(fechaExamen, horaExamen, idDocumentoPaciente, tipoExamenLaboratorio )    