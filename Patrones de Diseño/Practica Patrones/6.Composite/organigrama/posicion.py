from abc import ABC, abstractmethod

class Posicion(ABC):
    @abstractmethod
    def mostrar_informacion(self):
        pass

    @abstractmethod
    def calcular_presupuesto(self):
        pass