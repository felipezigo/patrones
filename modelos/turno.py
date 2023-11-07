class Turno:
    def _init_(self, hora, paciente=None):
        self.hora = hora
        self.esta_disponible = paciente is None
        self.paciente = paciente

    def reservar(self, paciente):
        # Lógica para reservar el turno
        pass
