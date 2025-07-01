from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def reservar(self, destino):
        pass
    
    @abstractmethod
    def calcular_costo(self, destino):
        pass