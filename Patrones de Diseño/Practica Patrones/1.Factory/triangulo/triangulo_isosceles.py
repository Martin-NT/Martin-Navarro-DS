from triangulo import Triangulo

class TrianguloIsosceles(Triangulo):
    def get_description(self):
        return "Isosceles"

    def get_superficie(self):
        return (self.ladoA + self.ladoB) * self.ladoC / 2