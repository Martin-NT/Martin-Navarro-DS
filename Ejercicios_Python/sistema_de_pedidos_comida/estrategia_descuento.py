from abc import ABC, abstractmethod
#Interfaz
class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular_total(self, productos):
        pass
