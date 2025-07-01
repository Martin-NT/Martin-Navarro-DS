class Prueba:
    def __init__(self, nombre, tipo):  # tipo: "Individual" o "Equipo"
        self.nombre = nombre
        self.tipo = tipo
        self.participantes = []  # Lista de participantes (esquiadores o equipos)

    def agregar_participante(self, participante, dorsal):
        codigo = f"{self.nombre}-{dorsal}"
        self.participantes.append((participante, codigo))

    def __repr__(self):
        return f"Prueba({self.nombre}, Tipo={self.tipo}, Participantes={len(self.participantes)})"
