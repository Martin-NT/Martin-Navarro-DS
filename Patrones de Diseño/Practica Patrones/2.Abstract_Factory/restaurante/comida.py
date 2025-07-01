from abc import ABC, abstractmethod

class Comida(ABC):
    @abstractmethod
    def preparar(self):
        pass

    @abstractmethod
    def servir(self):
        pass
