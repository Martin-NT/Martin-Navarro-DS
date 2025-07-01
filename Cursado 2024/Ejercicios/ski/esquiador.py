class Esquiador:
    def __init__(self, dni, nombre, fecha_nacimiento, edad):
        self.dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad

    def __repr__(self):
        return f"Esquiador({self.nombre}, DNI={self.dni}, Edad={self.edad}, Federación={self.federacion.nombre})"
