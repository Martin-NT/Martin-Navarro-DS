from abc import ABC, abstractmethod

class Bebida(ABC):
    @abstractmethod
    def preparar(self):
        pass

    @abstractmethod
    def servir(self):
        pass