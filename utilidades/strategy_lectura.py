# Archivo estrategia_lectura.py
# Este archivo contiene la clase abstracta EstrategiaLectura, que define la interfaz para las diferentes estrategias de lectura del archivo.
# Importamos el módulo abc de Python, que nos permite crear clases abstractas
from datetime import datetime, timedelta
import abc
import datetime 
# Importamos las clases que vamos a usar desde los otros archivos
from modelos.turno import Turno
from modelos.paciente import Paciente
from modelos.apoderado import Apoderado
from modelos.examen import Examen
from utilidades.facade_reserva import FachadaReserva

class EstrategiaLectura(metaclass=abc.ABCMeta):
  # Método abstracto que define la interfaz para leer el archivo y procesar los datos de las citas
  @abc.abstractmethod
  def leer_linea_archivo(self, fecha, datos_cita, fabrica, fachada):
    pass

# Este archivo contiene las clases concretas que heredan de la clase abstracta EstrategiaLectura, e implementan el método leer_archivo de forma diferente, según el tipo de lectura que se quiera realizar.
# Clase concreta que hereda de la clase EstrategiaLectura, e implementa el método leer_archivo para leer las citas ya agendadas
class EstrategiaLecturaAgendadas(EstrategiaLectura):
  # Método que lee el archivo y procesa los datos de las citas ya agendadas
  def leer_linea_archivo(self, fechaExamen, datos_cita, fabrica, fachada):
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
    
    # Creamos una instancia de la clase Turno con los datos de la fecha y la hora
    Turno.agregar_turno(fechaExamen, horaExamen, False)
    # Creamos una instancia de la clase Examen con los datos del tipo y la forma, usando el método crear_examen de la fábrica
    Examen.agregar_examen(tipoExamenLaboratorio, categoriaExamenLaboratorio)
   
    FachadaReserva()._instance.fecha.append(fechaExamen)
    FachadaReserva()._instance.citas.append(datos_cita)

    if len(divisionDatossinEspacios)>9:
        tipoApoderado = divisionDatossinEspacios[10]
        nombreApoderado = divisionDatossinEspacios[11]
        tipoDocumentoApoderado = divisionDatossinEspacios[12]
        fechaNacimientoApoderado = divisionDatossinEspacios[13]
        # Creamos una instancia de la clase Paciente con los datos del nombre, el tipo de persona, el tipo de documento, el id, el teléfono y la fecha de nacimiento
        Paciente.agregar_paciente(nombrePaciente, tipoPaciente, tipoDocumentoPaciente, idDocumentoPaciente, telefonoPaciente, fechaNacimientoPaciente, True)
        Apoderado.agregar_apoderado(tipoApoderado,nombreApoderado,tipoDocumentoApoderado,fechaNacimientoApoderado,idDocumentoPaciente)
    else:
        # Creamos una instancia de la clase Paciente con los datos del nombre, el tipo de persona, el tipo de documento, el id, el teléfono y la fecha de nacimiento
        Paciente.agregar_paciente(nombrePaciente, tipoPaciente, tipoDocumentoPaciente, idDocumentoPaciente, telefonoPaciente, fechaNacimientoPaciente, False)
        
        # Creamos una instancia de la clase Paciente con los datos del apoderado, que están después de la fecha de nacimiento del paciente
        #apoderado = Paciente(datos[11], datos[12], datos[13], datos[14], datos[15], datos[16])
        # Asignamos el apoderado al paciente, usando el método set_apoderado de la clase Paciente
        #paciente.set_apoderado(apoderado)
    # Usamos el método agregar_turno de la clase ProgramadorLaboratorio para registrar el turno en el sistema, pasando como argumentos el turno, el examen y el paciente
    #programador.agregar_turno(turno, examen, paciente)

# Clase concreta que hereda de la clase EstrategiaLectura, e implementa el método leer_archivo para leer las citas nuevas
class EstrategiaLecturaNuevas(EstrategiaLectura):
 # Método que lee el archivo y procesa los datos de las citas ya agendadas
  def leer_linea_archivo(self, datos_cita, fabrica, fachada):
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
    
    # # Creamos una instancia de la clase Turno con los datos de la fecha y la hora
    Turno.agregar_turno(fechaExamen, horaExamen, False)
    # # Creamos una instancia de la clase Examen con los datos del tipo y la forma, usando el método crear_examen de la fábrica
    Examen.agregar_examen(tipoExamenLaboratorio, categoriaExamenLaboratorio)
   
    FachadaReserva()._instance.fecha.append(fechaExamen)
    FachadaReserva()._instance.citas.append(datos_cita[11:])

    if len(divisionDatossinEspacios)>10:
        tipoApoderado = divisionDatossinEspacios[11]
        nombreApoderado = divisionDatossinEspacios[12]
        tipoDocumentoApoderado = divisionDatossinEspacios[13]
        fechaNacimientoApoderado = divisionDatossinEspacios[14]
        # Creamos una instancia de la clase Paciente con los datos del nombre, el tipo de persona, el tipo de documento, el id, el teléfono y la fecha de nacimiento
        Paciente.agregar_paciente(nombrePaciente, tipoPaciente, tipoDocumentoPaciente, idDocumentoPaciente, telefonoPaciente, fechaNacimientoPaciente, True)
        Apoderado.agregar_apoderado(tipoApoderado,nombreApoderado,tipoDocumentoApoderado,fechaNacimientoApoderado,idDocumentoPaciente)
    else:
        # Creamos una instancia de la clase Paciente con los datos del nombre, el tipo de persona, el tipo de documento, el id, el teléfono y la fecha de nacimiento
        Paciente.agregar_paciente(nombrePaciente, tipoPaciente, tipoDocumentoPaciente, idDocumentoPaciente, telefonoPaciente, fechaNacimientoPaciente, False)
    FachadaReserva().crear_turno(fechaExamen, horaExamen, idDocumentoPaciente, tipoExamenLaboratorio )    