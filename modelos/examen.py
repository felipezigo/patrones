class Examen:
    examenes = [] 
    def __init__(self, tipo, categoria):
        self.tipo = tipo
        self.categoria= categoria
        self.agregar_examen(self)
        
    @classmethod
    def agregar_examen(cls, tipo, categoria):
        examenAgregar = Examen
        examenAgregar.tipo = tipo
        examenAgregar.categoria = categoria
        cls.examenes.append(examenAgregar)

    @classmethod
    def obtener_examen(cls):
        return cls.examenes