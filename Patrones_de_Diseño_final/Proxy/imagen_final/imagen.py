from abc import ABC, abstractmethod

class Imagen(ABC):
    @abstractmethod
    def mostrar(self):
        pass
