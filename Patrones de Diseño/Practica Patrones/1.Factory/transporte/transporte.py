from abc import ABC, abstractmethod

# Interfaz
class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass
