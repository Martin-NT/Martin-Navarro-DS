class Persona:
    def __init__(self, nss, nombre, direccion, telefono):
        self.nss = nss
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __repr__(self):
        return f"({self.nombre}, NSS={self.nss})"
