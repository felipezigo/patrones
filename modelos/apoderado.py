class Apoderado:
    apoderado = []

    def __init__(self, nombreApoderado, tipoDocumentoApoderado, idDocumentoApoderado, fechaNacimientoApoderado, idRepresentado):
        self.nombreApoderado = nombreApoderado
        self.tipoDocumentoApoderado = tipoDocumentoApoderado
        self.idDocumentoApoderado = idDocumentoApoderado
        self.fechaNacimientoApoderado = fechaNacimientoApoderado
        self.idRepresentado = idRepresentado
        self.agregar_(self)

    @classmethod
    def agregar_apoderado(cls, nombreApoderado, tipoDocumentoApoderado, idDocumentoApoderado, fechaNacimientoApoderado, idRepresentado):
        apoderadoAgregar = Apoderado
        apoderadoAgregar.nombreApoderado = nombreApoderado
        apoderadoAgregar.tipoDocumentoApoderado = tipoDocumentoApoderado
        apoderadoAgregar.idDocumentoApoderado = idDocumentoApoderado
        apoderadoAgregar.fechaNacimientoApoderado = fechaNacimientoApoderado
        apoderadoAgregar.idRepresentado = idRepresentado
        cls.apoderado.append(apoderadoAgregar)

    @classmethod
    def obtener_apoderado(cls):
        return cls.apoderado

