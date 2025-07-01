from triangulo import Triangulo

class TrianguloEscaleno(Triangulo):
    def get_description(self):
        return "Escaleno"

    def get_superficie(self):
        return self.ladoA * self.ladoB * self.ladoC