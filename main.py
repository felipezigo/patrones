from utilidades.factory_examen import FactoryExamen
from utilidades.facade_reserva import FachadaReserva
from utilidades.contexto_lectura import ContextoLectura


factory = FactoryExamen()

facade = FachadaReserva()

contexto = ContextoLectura(None)

pathArchivoInput = 'input\lab_input.txt'
try:
    contexto.ejecutar_lectura(pathArchivoInput)
except Exception as e:
  facade.imprimir_citas_y_fechas(-1)
  print(e)