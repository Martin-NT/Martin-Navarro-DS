from plato import Plato
from combo import Combo

def main():
    print("\n🎉 Bienvenido al sistema de Menú del Restaurante 🎉")

    # Crear platos individuales
    plato1 = Plato("🍔 Hamburguesa", 5.50)
    plato2 = Plato("🍟 Papas Fritas", 2.50)
    plato3 = Plato("🥤 Refresco", 1.50)
    plato4 = Plato("🥗 Ensalada", 3.00)

    # Crear combos simples
    combo1 = Combo("\nCombo Básico")
    combo1.agregar_elemento(plato1)
    combo1.agregar_elemento(plato2)
    combo1.agregar_elemento(plato3)

    combo2 = Combo("\nCombo Saludable")
    combo2.agregar_elemento(plato4)
    combo2.agregar_elemento(plato3)

    # Crear combo compuesto
    combo_grande = Combo("\nCombo Familiar")
    combo_grande.agregar_elemento(combo1)
    combo_grande.agregar_elemento(combo2)
    combo_grande.agregar_elemento(Plato("🍰 Postre", 4.00))

    # Mostrar combos
    print("\n🧾 Detalles del menú disponible:\n")
    combo1.mostrar_detalles()
    combo2.mostrar_detalles()
    combo_grande.mostrar_detalles()


if __name__ == "__main__":
    main()