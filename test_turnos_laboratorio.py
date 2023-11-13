# test_turnos_laboratorio.py
import unittest
from utilidades.facade_reserva import FachadaReserva
from modelos.paciente import Paciente
from modelos.examen import Examen
from modelos.turno import Turno

class TestRestricciones(unittest.TestCase):

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
        Paciente.agregar_paciente("Ana Gomez", "Tipo2", "DNI", "87654321", "987654321", "1990-01-01", None)
        self.assertTrue(Paciente.obtener_pacientes())

class TestExamen(unittest.TestCase):

    def test_agregar_examen(self):
        Examen.agregar_examen("CREATININA", "STANDARD")
        self.assertTrue(Examen.obtener_examen())
        
class TestTurno(unittest.TestCase):

    def test_agregar_turno(self):
        Turno.agregar_turno("2023-10-24", "09:00")
        self.assertTrue(Turno.obtener_turno())

class TestFachadaReserva(unittest.TestCase):

    def setUp(self):
        self.fachada = FachadaReserva()

    def test_crear_turno_dia_laboral(self):
        fecha = "2023-10-23"  
        hora = "10:00"
        id_paciente = "123" 
        examen = "GLUCOSA"

        self.fachada.crear_turno(fecha, hora, id_paciente, examen)

    def test_crear_turno_dia_no_laboral(self):
        fecha = "2023-11-12"  
        hora = "10:00"
        id_paciente = "123"
        examen = "GLUCOSA"

        with self.assertRaises(ValueError):
            self.fachada.crear_turno(fecha, hora, id_paciente, examen)


if __name__ == '__main__':
    unittest.main()
