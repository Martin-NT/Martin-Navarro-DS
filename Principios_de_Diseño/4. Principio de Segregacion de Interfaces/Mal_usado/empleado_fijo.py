from empleado import Empleado

class EmpleadoFijo(Empleado):
    def calcular_salario(self):
        return "Salario fijo calculado"

    def reportar_horas(self):
        return "Reporte de horas enviado"

    def tomar_descanso(self):
        return "Empleado fijo toma un descanso"

    def __str__(self):
        return "Empleado Fijo"
