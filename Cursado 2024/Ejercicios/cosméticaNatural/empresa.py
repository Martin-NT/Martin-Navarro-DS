class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.representantes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_representante(self, representante):
        self.representantes.append(representante)

    def __repr__(self):
        return f"Empresa({self.nombre}, Productos={len(self.productos)}, Representantes={len(self.representantes)})"
