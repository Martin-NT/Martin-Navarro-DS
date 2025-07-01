from fabrica_italiana import FabricaItaliana
from fabrica_mexicana import FabricaMexicana

def mostrar_menu(nombre: str, fabrica):
    print(f"\nMenu de {nombre}")
    
    comida = fabrica.crear_comida()
    bebida = fabrica.crear_bebida()

    comida.preparar()
    comida.servir()

    bebida.preparar()
    bebida.servir()
    print("-" * 30)

def main():
    mostrar_menu("Italia", FabricaItaliana())
    mostrar_menu("México", FabricaMexicana())

if __name__ == "__main__":
    main()
