from triangulo import Triangulo

class TrianguloEquilatero(Triangulo):
    def get_description(self):
        return "Equilatero"

    def get_superficie(self):
        return self.ladoA + self.ladoB + self.ladoC