from datetime import date
from modelos.infoContacto import InfoContacto
from modelos.representante import Representante


class Paciente:
    def _init_(self, id,cedula, nombre, apellido, fechaNacimiento:date, infoContacto:InfoContacto, representante:Representante=None):
        self.id = id
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.fechaNcimiento = fechaNacimiento
        self.infoContacto = infoContacto
        self.representante = representante