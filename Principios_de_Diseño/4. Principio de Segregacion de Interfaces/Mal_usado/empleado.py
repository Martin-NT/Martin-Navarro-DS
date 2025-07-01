from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def reportar_horas(self):
        pass  # No todos los empleados reportan horas

    @abstractmethod
    def tomar_descanso(self):
        pass  # No todos los empleados necesitan esto
