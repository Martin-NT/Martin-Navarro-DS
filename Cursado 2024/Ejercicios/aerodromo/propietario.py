from persona import Persona


class Propietario(Persona):
    def __init__(self, nss, nombre, direccion, telefono):
        super().__init__(nss, nombre, direccion, telefono)
        self.aviones = []  # Lista de aviones que posee

    def agregar_avion(self, avion):
        self.aviones.append(avion)

    def __repr__(self):
        return super().__repr__() + f", Aviones={len(self.aviones)}"
