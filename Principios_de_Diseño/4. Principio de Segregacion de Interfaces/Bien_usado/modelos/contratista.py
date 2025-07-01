from interfaces.empleado import Empleado

class Contratista(Empleado):
    def calcular_salario(self):
        return "Pago por proyecto calculado"

    def __str__(self):
        return "Contratista"
