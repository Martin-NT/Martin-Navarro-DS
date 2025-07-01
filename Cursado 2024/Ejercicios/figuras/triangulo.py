from poligono import Poligono


class Triangulo(Poligono):
    def __init__(self):
        super().__init__(3)

    def dibujar(self):
        print("Dibujando un Triángulo")