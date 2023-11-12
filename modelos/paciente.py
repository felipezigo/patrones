class Paciente:
    pacientes = [] 

    def __init__(self, nombrePaciente, tipoPaciente, tipoDocumentoPaciente, idDocumentoPaciente, telefonoPaciente, fechaNacimientoPaciente, apoderado):
        self.nombrePaciente = nombrePaciente
        self.tipoPaciente = tipoPaciente
        self.tipoDocumentoPaciente = tipoDocumentoPaciente
        self.idDocumentoPaciente = idDocumentoPaciente
        self.telefonoPaciente = telefonoPaciente
        self.fechaNacimientoPaciente = fechaNacimientoPaciente
        self.apoderado = apoderado

        self.agregar_paciente(self)

    @classmethod
    def agregar_paciente(cls, nombrePaciente, tipoPaciente, tipoDocumentoPaciente, idDocumentoPaciente, telefonoPaciente, fechaNacimientoPaciente, apoderado):
        pacienteAgregar = Paciente
        pacienteAgregar.nombrePaciente = nombrePaciente
        pacienteAgregar.tipoPaciente = tipoPaciente
        pacienteAgregar.tipoDocumentoPaciente = tipoDocumentoPaciente
        pacienteAgregar.idDocumentoPaciente = idDocumentoPaciente
        pacienteAgregar.telefonoPaciente = telefonoPaciente
        pacienteAgregar.fechaNacimientoPaciente = fechaNacimientoPaciente
        pacienteAgregar.apoderado = apoderado
        
        cls.pacientes.append(pacienteAgregar)

    @classmethod
    def obtener_pacientes(cls):
        return cls.pacientes

    def tiene_cita_en_turno(self, turno):
        pass
