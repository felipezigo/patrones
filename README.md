# Sistema de Reserva de Citas para Laboratorio Clínico

Este proyecto es una aplicación de consola para la gestión de reservas de citas en un establecimiento médico que ofrece servicios de consulta médica y laboratorio clínico.

## Descripción

La aplicación permite agendar citas para exámenes de laboratorio. Las citas se gestionan mediante una interfaz de consola que interactúa con un sistema de programación de citas. Este sistema se encarga de asignar turnos de laboratorio a los pacientes, tomando en cuenta la disponibilidad y las restricciones de los exámenes.

## Funcionalidades

- Registro de pacientes con sus datos personales y de contacto.
- Reserva de turnos para diferentes exámenes de laboratorio.
- Validación de disponibilidad de turnos según el horario del laboratorio.
- Asignación de citas evitando conflictos de horario.

## Patrones de Diseño Implementados

En este proyecto, se han implementado varios patrones de diseño para mejorar la estructura y la mantenibilidad del código:

- **Factory (`FactoryExamen`)**: Este patrón se utiliza para crear instancias de `Examen` con propiedades específicas basadas en el tipo de examen. Facilita la adición de nuevos tipos de exámenes al sistema sin modificar el código existente.

- **Strategy (`EstrategiaReserva`)**: Implementamos diferentes estrategias de reserva que pueden ser extendidas o modificadas según las necesidades del laboratorio. Esto permite una mayor flexibilidad en cómo se manejan las reservas de citas.

- **Facade (`FachadaReserva`)**: Proporcionamos una interfaz simplificada para realizar reservas. Este patrón oculta la complejidad de las operaciones subyacentes relacionadas con la asignación y gestión de turnos, ofreciendo una interacción más sencilla para los usuarios.

Estos patrones ayudan a mantener nuestro código más organizado, flexible y fácil de mantener.

## Principios SOLID

- **Single Responsibility**: Cada clase tiene una única responsabilidad. Por ejemplo, `Paciente` solo mantiene información relacionada con los pacientes.
- **Open/Closed**: Las clases están abiertas para la extensión, pero cerradas para la modificación. Se pueden agregar nuevos tipos de exámenes sin modificar la `FabricaExamen`.
- **Liskov Substitution**: Las clases derivadas pueden ser utilizadas en lugar de sus clases base.
- **Interface Segregation**: Las interfaces son específicas a las necesidades de los clientes. Por ejemplo, `EstrategiaReserva` puede tener varias implementaciones que no afectan a los consumidores de la interfaz.
- **Dependency Inversion**: Los detalles de bajo nivel (como la creación de exámenes) dependen de las abstracciones, no al revés.

## Configuración del Entorno

Descripción de cómo configurar el entorno de desarrollo local, incluyendo la instalación de Python y cualquier dependencia necesaria.

```sh
# Clonar el repositorio
git clone [URL_DEL_REPOSITORIO]

# (Opcional) Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows usar: venv\Scripts\activate
Agregar el archivo lab_input.txt dentro de la carpeta input del proyecto.
```
## Diagrama de clases
!["Diseñado en Miro"](https://github.com/felipezigo/patrones/blob/main/DiagramaClases.jpg "Enlace")
Un diagrama de clases proporciona una representación visual de las clases, sus relaciones y cómo se estructura el proyecto. Esto facilita la comprensión de la arquitectura general del sistema, permite identificar las relaciones entre las clases, como la herencia, la asociación y la composición. Esto es fundamental para entender cómo interactúan las clases entre sí.

## Distinción de la estructura del proyecto
!["Estructura Carpetas"](https://github.com/felipezigo/patrones/blob/main/SeccionesCodigos.jpg "Enlace")

#Clases Relevantes

**FactoryExamen**: Esta clase implementa el patrón Factory para crear instancias de Examen basadas en el tipo de examen, permitiendo la creación de exámenes con propiedades específicas sin modificar el código existente.

**EstrategiaReserva**: Clase abstracta que define la interfaz para las estrategias de reserva. Las clases concretas ReservaExamenLaboratorio y ReservaCitaMedica implementan esta interfaz para las estrategias específicas de reserva.

**FachadaReserva**: Implementa el patrón Facade y proporciona una interfaz simplificada para realizar reservas y gestionar la asignación de turnos.

**ContextoLectura**: Esta clase coordina la lectura de datos desde un archivo, seleccionando y ejecutando la estrategia adecuada de lectura según el tipo de línea que se lee.
Clases como Turno, Paciente, Apoderado y Examen: Estas clases almacenan datos relevantes para el agendamiento de citas y gestionan la creación de instancias.

#Eventos Relevantes

**leer_linea_archivo** (método en EstrategiaLectura): Este evento se dispara al leer una línea del archivo, procesa los datos de las citas y crea instancias de Turno, Examen, Paciente y Apoderado, según sea necesario, para el agendamiento de citas.

**crear_turno** (método en FachadaReserva): Este evento coordina la creación de turnos, verifica su disponibilidad y aplica reglas de negocio, como horarios laborales y restricciones de cita repetida.

#Patrones de Diseño

**Factory Method** Se utiliza en FactoryExamen para crear instancias de Examen basadas en el tipo de examen.

**Strategy** El patrón Strategy se implementa con las clases EstrategiaReserva, ReservaExamenLaboratorio y ReservaCitaMedica, lo que permite flexibilidad en las estrategias de reserva.

**Facade** FachadaReserva se utiliza como una fachada que simplifica la reserva de citas y oculta la complejidad de las operaciones subyacentes.

## Trazas de código
Python tiene un modo resumido para recorrer listas en donde se puede refactorizar el código hasta quedar en una sola línea: 
<pre>
```python
# Implementar lógica para verificar si el paciente ya tiene cita en el mismo examen
def tiene_cita_repetida(self, fecha, idPaciente, examen):    
    return any(Turno.turnos[indice].fecha == fecha and Paciente.pacientes[indice].idDocumentoPaciente == idPaciente and Examen.examenes[indice].tipo == examen for indice in range(len(Paciente.pacientes)-2,0))

#Método abstracto que define la interfaz para leer el archivo y procesar los datos de las citas.
#Este archivo contiene las clases concretas que heredan de la clase abstracta EstrategiaLectura, e implementan el método leer_archivo de forma diferente, según el tipo de #lectura que se quiera realizar.
#Y después se define la clase concreta que hereda de la clase EstrategiaLectura, e implementa el método leer_archivo para leer las citas ya agendadas
class EstrategiaLectura(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def leer_linea_archivo(self, fecha, datos_cita, fabrica, fachada):
class EstrategiaLecturaAgendadas(EstrategiaLectura):

# Clase concreta que hereda de la clase EstrategiaLectura, e implementa el método leer_archivo para leer las citas nuevas
class EstrategiaLecturaNuevas(EstrategiaLectura):

#Patrón creacional fachada donde se encapsula parte de la lógca de la lectura del archivo txt
class FachadaReserva:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(FachadaReserva, cls).__new__(cls)
            cls._instance.citas = []
            cls._instance.fecha = []
        return cls._instance

#Archivo main.py
#Este es el archivo principal que ejecuta la aplicación.
#Importamos las clases y funciones que vamos a usar desde los otros archivos.
#Creamos instancia de la clase FactoryExamen, FachadaReserva y ContextoLectura para poderlos usar en la implementación de la solución
from utilidades.factory_examen import FactoryExamen
from utilidades.facade_reserva import FachadaReserva
from utilidades.strategy_lectura import EstrategiaLecturaAgendadas, EstrategiaLecturaNuevas
from utilidades.contexto_lectura import ContextoLectura
factory = FactoryExamen()
facade = FachadaReserva()
contexto = ContextoLectura(None)
pathArchivoInput = 'patrones\input\lab_input.txt'
try:
    contexto.ejecutar_lectura(pathArchivoInput,factory, facade)
except Exception as e:
  facade.imprimir_citas_y_fechas(-1)
  print(e)
```
