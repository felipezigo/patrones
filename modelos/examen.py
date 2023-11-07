import datetime
from modelos.rangoHorario import RangoHorario


class Examen:
    def _init_(self, nombre, restriccionHoraria:RangoHorario=None):
        self.nombre = nombre
        self.restriccionHoraria = restriccionHoraria

    def esta_disponible_en(self, fecha:datetime):
        # Lógica para saber si el examen está disponible en una hora
        pass