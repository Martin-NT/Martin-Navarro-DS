from puesto_individual import PuestoIndividual
from depto import Depto

def main():
    # Crear departamentos
    departamento1 = Depto("Departamento 1")
    departamento2 = Depto("Departamento 2")
    departamento3 = Depto("Departamento 3")

    # Crear puestos individuales
    puesto1 = PuestoIndividual("Gerente", 10000)
    puesto2 = PuestoIndividual("Jefe", 100000)
    puesto3 = PuestoIndividual("Vendedor1", 20000)
    puesto4 = PuestoIndividual("Vendedor2", 3000)
    puesto5 = PuestoIndividual("Técnico", 50000)

    # Agregar puestos a departamentos
    departamento1.agregar_posicion(puesto1)
    departamento1.agregar_posicion(puesto2)
    departamento2.agregar_posicion(puesto3)
    departamento2.agregar_posicion(puesto4)
    departamento3.agregar_posicion(puesto5)

    # Mostrar información de los departamentos
    departamento1.mostrar_informacion()
    departamento2.mostrar_informacion()
    departamento3.mostrar_informacion()

    # Calcular el presupuesto total de los departamentos
    presupuesto_total = departamento1.calcular_presupuesto()
    presupuesto_total += departamento2.calcular_presupuesto()
    presupuesto_total += departamento3.calcular_presupuesto()

    print(f"El presupuesto total de los departamentos es: ${presupuesto_total:.2f}")

if __name__ == "__main__":
    main()