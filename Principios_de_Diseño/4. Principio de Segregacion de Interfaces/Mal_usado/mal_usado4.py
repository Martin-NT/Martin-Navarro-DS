#Los clientes no deberían estar forzados a  depender de interfaces que no utilizan.

from abc import ABC, abstractmethod

# ❌ INTERFAZ CON MÉTODOS INNECESARIOS
class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass  # Todos los empleados tienen salario, esto está bien.

    @abstractmethod
    def reportar_horas(self):
        pass  # No todos los empleados reportan horas (ej: empleados con salario fijo)

    @abstractmethod
    def tomar_descanso(self):
        pass  # No todos los empleados necesitan esto (ej: contratistas)

# ✅ Empleado Fijo: Debe implementar TODO aunque no necesite todo
class EmpleadoFijo(Empleado):
    def calcular_salario(self):
        return "Salario fijo calculado"

    def reportar_horas(self):
        return "Reporte de horas enviado"

    def tomar_descanso(self):
        return "Empleado fijo toma un descanso"

# ✅ Contratista: Implementa métodos que NO NECESITA
class Contratista(Empleado):
    def calcular_salario(self):
        return "Pago por proyecto calculado"

    def reportar_horas(self):
        return "ERROR: Un contratista no reporta horas"

    def tomar_descanso(self):
        return "ERROR: Un contratista no toma descansos"

#🚨 ¿Por qué esto viola ISP?
# 🔴 El problema es que Contratista debe implementar reportar_horas() y tomar_pausa(), aunque no los necesite.
# 🔴 Esto hace que tenga métodos inútiles o con implementaciones forzadas como "ERROR: Un contratista no reporta horas".
# 🔴 Esto va en contra del principio, porque estamos obligando a clases a implementar métodos innecesarios.