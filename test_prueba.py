# test_mi_modulo.py
import unittest
from utilidades.facade_reserva import FachadaReserva
from modelos.paciente import Paciente
from modelos.examen import Examen

class TestMiModulo(unittest.TestCase):

    def test_turno_es_horario_laboral(self):
        self.assertTrue(FachadaReserva.turno_horario_laboral(fecha='2023-11-13', hora='10:00' , self=self))

    def test_turno_no_es_horario_laboral(self):
        self.assertFalse(FachadaReserva.turno_horario_laboral(fecha='2023-11-12', hora='10:00' , self=self))

    def test_fecha_es_feriado(self):
        self.assertTrue(FachadaReserva.es_feriado(fecha='2023-11-03', self=self))
    
    def test_fecha_no_es_feriado(self):
        self.assertFalse(FachadaReserva.es_feriado(fecha='2023-11-13', self=self))
        
class TestPaciente(unittest.TestCase):
    
    def test_agregar_paciente(self):
        """Prueba el método de clase para agregar un paciente."""
        Paciente.agregar_paciente("Ana Gomez", "Tipo2", "DNI", "87654321", "987654321", "1990-01-01", None)
        self.assertTrue(Paciente.obtener_pacientes())

class TestExamen(unittest.TestCase):

    def test_agregar_examen(self):
        """Prueba el método de clase para agregar un examen."""
        Examen.agregar_examen("CREATININA", "STANDARD")
        self.assertTrue(Examen.obtener_examen())

if __name__ == '__main__':
    unittest.main()
