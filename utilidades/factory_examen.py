from modelos.examen import Examen

class FactoryExamen:
    @staticmethod
    def crear_examen(tipoExamenLaboratorio,categoriaExamenLaboratorio):
        return Examen(tipoExamenLaboratorio,categoriaExamenLaboratorio)