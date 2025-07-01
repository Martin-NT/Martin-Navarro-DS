from persona import Persona


class Piloto(Persona):
    def __init__(self, nss, nombre, direccion, telefono, licencia, restricciones):
        super().__init__(nss, nombre, direccion, telefono)
        self.licencia = licencia
        self.restricciones = restricciones
        self.aviones_autorizados = [] 

    def agregar_avion_autorizado(self, tipo_avion):
        self.aviones_autorizados.append(tipo_avion)

    def __repr__(self):
        return super().__repr__() + f", Piloto , Licencia={self.licencia}"
