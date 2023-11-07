from datetime import date


class Representante:
    def _init_(self, cedula, nombre, fechaNacimiento:date):
        self.nombre = nombre
        self.cedula = cedula
        self.fechaNacimiento = fechaNacimiento