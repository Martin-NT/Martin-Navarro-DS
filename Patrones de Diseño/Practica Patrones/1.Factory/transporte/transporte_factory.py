from abc import ABC, abstractmethod

# Interfaz
class TransporteFactory(ABC):
    @abstractmethod
    def crear(self):
        pass