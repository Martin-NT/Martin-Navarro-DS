from triangulo_factory import TrianguloFactory
from triangulo_escaleno import TrianguloEscaleno

class TrianguloEscalenoFactory(TrianguloFactory):
    def crear_triangulo(self,ladoA,ladoB,ladoC):
        return TrianguloEscaleno(ladoA,ladoB,ladoC)