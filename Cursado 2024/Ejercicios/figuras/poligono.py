from figura import Figura


class Poligono(Figura):
    def __init__(self, numero_de_lados):
        self.numero_de_lados = numero_de_lados
        self.lados = []  

    def agregar_lado(self, lado):
        self.lados.append(lado)

    def __repr__(self):
        return f"Poligono(lados={len(self.lados)})"