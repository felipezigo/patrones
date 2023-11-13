# test_mi_modulo.py
import unittest
from utilidades.facade_reserva import FachadaReserva

class TestMiModulo(unittest.TestCase):

    def test_turno_es_horario_laboral(self):
        self.assertEqual(FachadaReserva.turno_horario_laboral(fecha='2023-11-13', hora='10:00' ),  True)

    def test_turno_no_es_horario_laboral(self):
        self.assertEqual(FachadaReserva.turno_horario_laboral(fecha='2023-11-13', hora='10:00' ),  False)

    def test_fecha_es_feriado(self):
        self.assertEqual(FachadaReserva.es_feriado(fecha='2023-11-03'),  True)
    
    def test_fecha_no_es_feriado(self):
        self.assertEqual(FachadaReserva.es_feriado(fecha='2023-11-13'),  False)


if __name__ == '__main__':
    unittest.main()
