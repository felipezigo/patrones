from programador_laboratorio import ProgramadorLaboratorio
from utilidades.fabrica_examen import FabricaExamen
from modelos.paciente import Paciente
from datetime import datetime

class FachadaReserva:
    def __init__(self):
        # Obtener la instancia del Singleton del programador de laboratorio
        self.programador = ProgramadorLaboratorio.obtener_instancia()

    def realizar_reserva(self, id_paciente, nombre, apellido, fecha_nacimiento, email, telefono, nombre_examen, fecha_hora_examen):
        # Crear un objeto paciente con la información proporcionada
        info_contacto = {'email': email, 'telefono': telefono}
        paciente = Paciente(id_paciente, nombre, apellido, fecha_nacimiento, info_contacto)
        
        # Utilizar la fábrica de exámenes para obtener la instancia correcta de un examen
        examen = FabricaExamen.crear_examen(nombre_examen)
        
        # Convertir la cadena de fecha y hora en un objeto datetime
        fecha_hora = datetime.strptime(fecha_hora_examen, '%Y-%m-%d %H:%M:%S')
        
        # Verificar si el examen puede realizarse en el horario indicado
        if not examen.esta_disponible_en(fecha_hora):
            raise ValueError(f"El examen {nombre_examen} no se puede realizar en el horario indicado.")
        
        # Intentar reservar el turno en el programador de laboratorio
        exito = self.programador.reservar_turno(paciente, examen, fecha_hora)
        
        # Devolver un mensaje de éxito o de error según corresponda
        if exito:
            return f"Reserva confirmada para el paciente {nombre} {apellido} para el examen {nombre_examen} en la fecha y hora {fecha_hora_examen}."
        else:
            return "No se pudo realizar la reserva. Por favor, intente con otro horario o verifique la disponibilidad."
