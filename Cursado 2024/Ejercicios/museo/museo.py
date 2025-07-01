class Museo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.objetos = []  # Lista de objetos de arte

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def __repr__(self):
        return f"Museo({self.nombre}, Objetos={len(self.objetos)})"
