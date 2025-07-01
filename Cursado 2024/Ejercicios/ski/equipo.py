class Equipo:
    def __init__(self, codigo, entrenador):
        self.codigo = codigo
        self.entrenador = entrenador
        self.esquiadores = []  # Lista de esquiadores en el equipo

    def agregar_esquiador(self, esquiador):
        self.esquiadores.append(esquiador)

    def __repr__(self):
        return f"Equipo({self.codigo}, Entrenador={self.entrenador}, Miembros={len(self.esquiadores)})"
