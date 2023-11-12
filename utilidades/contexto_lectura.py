# Archivo contexto_lectura.py
# Este archivo contiene la clase ContextoLectura, que tiene un atributo llamado estrategia, que es una instancia de la clase EstrategiaLectura, y que tiene un método llamado ejecutar_lectura, que llama al método leer_linea de la estrategia, pasando los argumentos correspondientes.

# Importamos la clase EstrategiaLectura desde el archivo estrategia_lectura.py
from utilidades.strategy_lectura import EstrategiaLecturaAgendadas,EstrategiaLecturaNuevas

class ContextoLectura:
  # Constructor de la clase
  def __init__(self, estrategia):
    # Asignamos la estrategia al atributo correspondiente
    self.estrategia = estrategia

  # Método que llama al método leer_linea de la estrategia, pasando los argumentos correspondientes
  def ejecutar_lectura(self, path, fabrica, fachada):
    # Llamamos al método leer_linea de la estrategia, pasando como argumentos la línea, el programador, la fábrica y la fachada
    # self.estrategia.leer_linea(linea, programador, fabrica, fachada)
    
    
    estrategia_agendadas = EstrategiaLecturaAgendadas()
    estrategia_nuevas = EstrategiaLecturaNuevas()
    # Define un diccionario para almacenar los datos
    datos_dict = {}

    # Abre el archivo y lee línea por línea
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

        # Agrega los datos del último bloque
        if clave_actual:
            datos_dict[clave_actual] = datos_clave

    for fecha, datos in datos_dict.items():
      for cita in datos:
        if fecha not in "NUEVA CITA":            
            estrategia_agendadas.leer_linea_archivo(fecha, cita, fabrica, fachada)            
        else:
            estrategia_nuevas.leer_linea_archivo(cita, fabrica, fachada)
            
            
    # Imprime el diccionario con los datos
    #print(datos_dict)

