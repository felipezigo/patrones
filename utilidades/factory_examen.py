from modelos.examen import Examen

class FactoryExamen:
    @staticmethod
    def crear_examen(tipoExamenLaboratorio,categoriaExamenLaboratorio):
        # Lógica para crear un examen basado en el nombre
        return Examen(tipoExamenLaboratorio,categoriaExamenLaboratorio)