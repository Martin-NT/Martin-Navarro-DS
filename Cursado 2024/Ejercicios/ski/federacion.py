class Federacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.esquiadores = []  # Lista de esquiadores en la federación

    def agregar_esquiador(self, esquiador):
        self.esquiadores.append(esquiador)

    def __repr__(self):
        return f"Federacion({self.nombre}, Federados={len(self.esquiadores)})"
