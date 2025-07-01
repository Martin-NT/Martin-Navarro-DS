from empleado import Empleado

class Contratista(Empleado):
    def calcular_salario(self):
        return "Pago por proyecto calculado"

    def reportar_horas(self):
        return "ERROR: Un contratista no reporta horas"

    def tomar_descanso(self):
        return "ERROR: Un contratista no toma descansos"

    def __str__(self):
        return "Contratista"
