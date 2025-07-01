from modelos.empleado_fijo import EmpleadoFijo
from modelos.contratista import Contratista
from interfaces.reportable import Reportable
from interfaces.descanso import Descanso

def imprimir_info(empleado):
    print(f"{empleado}: {empleado.calcular_salario()}")
    if isinstance(empleado, Reportable):
        print(f"{empleado}: {empleado.reportar_horas()}")
    if isinstance(empleado, Descanso):
        print(f"{empleado}: {empleado.tomar_descanso()}")

if __name__ == "__main__":
    fijo = EmpleadoFijo()
    contratista = Contratista()

    imprimir_info(fijo)
    print("-" * 40)
    imprimir_info(contratista)
