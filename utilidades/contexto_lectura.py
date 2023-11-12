from utilidades.strategy_lectura import EstrategiaLecturaAgendadas,EstrategiaLecturaNuevas

class ContextoLectura:
  def __init__(self, estrategia):
    self.estrategia = estrategia

  def ejecutar_lectura(self, path):
    
    
    estrategia_agendadas = EstrategiaLecturaAgendadas()
    estrategia_nuevas = EstrategiaLecturaNuevas()
    datos_dict = {}

    with open(path, "r") as archivo:
        clave_actual = None
        datos_clave = []

        for linea in archivo:
            linea = linea.strip()

            if "|" not in linea:
                if clave_actual:
                    datos_dict[clave_actual] = datos_clave
                    clave_actual = None
                    datos_clave = []
                clave_actual = linea
                datos_clave = []
            elif clave_actual:
                datos_clave.append(linea)

        if clave_actual:
            datos_dict[clave_actual] = datos_clave

    for fecha, datos in datos_dict.items():
      for cita in datos:
        if fecha not in "NUEVA CITA":            
            estrategia_agendadas.leer_linea_archivo(fecha, cita)            
        else:
            estrategia_nuevas.leer_linea_archivo(cita)
            


