from triangulo_factory import TrianguloFactory
from triangulo_isosceles import TrianguloIsosceles

class TrianguloIsoscelesFactory(TrianguloFactory):
    def crear_triangulo(self,ladoA,ladoB,ladoC):
        return TrianguloIsosceles(ladoA,ladoB,ladoC)