from empleado_fijo import EmpleadoFijo
from contratista import Contratista

def imprimir_info(empleado):
    print(f"{empleado}: {empleado.calcular_salario()}")
    print(f"{empleado}: {empleado.reportar_horas()}")
    print(f"{empleado}: {empleado.tomar_descanso()}")

if __name__ == "__main__":
    fijo = EmpleadoFijo()
    contratista = Contratista()

    imprimir_info(fijo)
    print("-" * 40)
    imprimir_info(contratista)
