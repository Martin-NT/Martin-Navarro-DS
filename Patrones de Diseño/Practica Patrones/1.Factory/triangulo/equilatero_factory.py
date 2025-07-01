from triangulo_factory import TrianguloFactory
from triangulo_equilatero import TrianguloEquilatero

class TrianguloEquilateroFactory(TrianguloFactory):
    def crear_triangulo(self,ladoA,ladoB,ladoC):    
        return TrianguloEquilatero(ladoA,ladoB,ladoC)