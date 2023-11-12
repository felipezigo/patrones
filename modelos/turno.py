class Turno:
    turnos = [] 
    def __init__(self, fecha, hora, disponible=None):
        self.fecha = fecha
        self.hora = hora
        self.disponible = disponible
        self.agregar_turno(self)
        
    @classmethod
    def agregar_turno(cls, fecha, hora, disponible=None):
        turnoAgregar = Turno
        turnoAgregar.fecha = fecha
        turnoAgregar.hora = hora
        turnoAgregar.disponible = disponible
        cls.turnos.append(turnoAgregar)

    @classmethod
    def obtener_turno(cls):
        return cls.turnos