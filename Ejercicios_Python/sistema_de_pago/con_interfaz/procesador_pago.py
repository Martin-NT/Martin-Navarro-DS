from abc import ABC, abstractmethod
#Interfaz
class ProcesadorPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass
