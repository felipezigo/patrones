# Archivo main.py
# Este es el archivo principal que ejecuta la aplicación.
# Importamos las clases y funciones que vamos a usar desde los otros archivos.
from utilidades.factory_examen import FactoryExamen
from utilidades.facade_reserva import FachadaReserva
from utilidades.strategy_lectura import EstrategiaLecturaAgendadas, EstrategiaLecturaNuevas
from utilidades.contexto_lectura import ContextoLectura

# Creamos una instancia de la clase FactoryExamen, que se encarga de crear instancias de exámenes según el tipo solicitado.
factory = FactoryExamen()

# Creamos una instancia de la clase FacadeReserva, que se encarga de simplificar la reserva de turnos usando la fachada y la estrategia adecuadas.
facade = FachadaReserva()

# Creamos una instancia de la clase ContextoLectura, que se encarga de seleccionar y ejecutar la estrategia de lectura adecuada según el tipo de línea que se lea del archivo.
contexto = ContextoLectura(None)

pathArchivoInput = 'input\lab_input.txt'
try:
    contexto.ejecutar_lectura(pathArchivoInput,factory, facade)
except Exception as e:
  # Si ocurre un error de valor, significa que el usuario no ingresó un número válido
  facade.imprimir_citas_y_fechas(-1)
  print(e)