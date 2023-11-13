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

## Bloques de código
<pre>
```python
def saludar(nombre):
    print("Hola, " + nombre)
```
source venv/bin/activate  # En Windows usar: venv\Scripts\activate
