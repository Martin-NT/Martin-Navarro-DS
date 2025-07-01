#En lugar de una sola interfaz gigante, creamos interfaces más pequeñas y específicas.

from abc import ABC, abstractmethod

# 🔹 Interfaz para empleados con salario
class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

    def __str__(self):
        return "Empleado"

# 🔹 Interfaz para empleados que reportan horas
class Reportable(ABC):
    @abstractmethod
    def reportar_horas(self):
        pass

# 🔹 Interfaz para empleados que tienen descansos
class Descanso(ABC):
    @abstractmethod
    def tomar_descanso(self):
        pass

# ✅ Empleado Fijo: Implementa solo lo que necesita
class EmpleadoFijo(Empleado, Reportable, Descanso):
    def calcular_salario(self):
        return "Salario fijo calculado"

    def reportar_horas(self):
        return "Reporte de horas enviado"

    def tomar_descanso(self):
        return "Empleado fijo toma un descanso"

    def __str__(self):
        return "Empleado Fijo"

# ✅ Contratista: Solo implementa lo que usa
class Contratista(Empleado):
    def calcular_salario(self):
        return "Pago por proyecto calculado"

    def __str__(self):
        return "Contratista"

# 🔥 Prueba
def imprimir_info(empleado: Empleado):
    print(f"{empleado}: {empleado.calcular_salario()}")
    if isinstance(empleado, Reportable):
        print(f"{empleado}: {empleado.reportar_horas()}")
    if isinstance(empleado, Descanso):
        print(f"{empleado}: {empleado.tomar_descanso()}")

# Creamos las instancias
fijo = EmpleadoFijo()
contratista = Contratista()

# Imprimimos la información
imprimir_info(fijo)
print("-" * 40)  # Separador
imprimir_info(contratista)


#🎯 ¿Por qué ahora cumple con ISP?
# ✅ Cada clase implementa solo los métodos que realmente necesita.
# ✅ No forzamos al Contratista a implementar reportar_horas() y tomar_descanso().
# ✅ El código es más flexible y fácil de mantener.

#🚀 Resumen del principio ISP
# ❌ Mal diseño: Una interfaz con demasiados métodos obliga a clases a implementar cosas que no usan.
# ✅ Buen diseño: Separamos las interfaces en partes más pequeñas y específicas para que cada clase implemente solo lo que necesita.