class Excursion:
    def __init__(self, codigo, dia, hora):
        self.codigo = codigo
        self.dia = dia
        self.hora = hora
        self.visitantes = []  # Visitantes inscritos

    def agregar_visitante(self, visitante):
        self.visitantes.append(visitante)

    def __repr__(self):
        return f"Excursion(Código={self.codigo}, Día={self.dia}, Hora={self.hora}, Visitantes={len(self.visitantes)})"
