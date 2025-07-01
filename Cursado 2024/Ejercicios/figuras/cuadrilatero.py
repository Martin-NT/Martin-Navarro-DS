from poligono import Poligono


class Cuadrilatero(Poligono):
    def __init__(self):
        super().__init__(4)

    def dibujar(self):
        print("Dibujando un Cuadrilátero")
