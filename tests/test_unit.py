# test_mi_modulo.py
import unittest
from utilidades.facade_reserva import FachadaReserva

class TestMiModulo(unittest.TestCase):

    def test_resta(self):
        self.assertEqual(FachadaReserva.turno_horario_laboral(fecha='2023-11-12', hora='17:00' ),  False)


# if __name__ == '__main__':
#     unittest.main()
