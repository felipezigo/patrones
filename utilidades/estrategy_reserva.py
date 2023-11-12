from abc import ABC, abstractmethod

class EstrategiaReserva(ABC):
    @abstractmethod
    def reservar_cita(self, paciente, turno):
        pass

class ReservaExamenLaboratorio(EstrategiaReserva):
    def reservar_cita(self, paciente, turno, examen):
        # Lógica específica para reservar exámenes de laboratorio
        pass

class ReservaCitaMedica(EstrategiaReserva):
    def reservar_cita(self, paciente, turno):
        # Lógica específica para reservar citas médicas
        pass

