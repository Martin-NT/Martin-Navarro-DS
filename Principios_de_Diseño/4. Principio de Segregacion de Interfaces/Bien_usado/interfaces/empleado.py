from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

    def __str__(self):
        return "Empleado"
