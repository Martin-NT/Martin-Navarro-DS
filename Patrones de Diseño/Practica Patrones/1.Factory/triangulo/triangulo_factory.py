from abc import ABC, abstractmethod

class TrianguloFactory(ABC):
    @abstractmethod
    def crear_triangulo(self,ladoA,ladoB,ladoC):
        pass