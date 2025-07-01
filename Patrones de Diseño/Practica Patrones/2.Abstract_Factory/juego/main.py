from fabrica_humanos import FabricaHumanos
from fabrica_orcos import FabricaOrcos

def simular_batalla(fabrica1, fabrica2):
    guerrero1 = fabrica1.crear_guerrero()
    arquero1 = fabrica1.crear_arquero()
    guerrero2 = fabrica2.crear_guerrero()
    arquero2 = fabrica2.crear_arquero()

    print("\nBatalla entre guerreros:")
    guerrero1.atacar()
    guerrero2.defender()
    guerrero2.atacar()
    guerrero1.defender()

    print("\nBatalla entre arqueros:")
    arquero1.atacar()
    arquero2.defender()
    arquero2.atacar()
    arquero1.defender()

if __name__ == "__main__":
    print("Simulación de batalla entre humanos y orcos:")
    fabrica_humanos = FabricaHumanos()
    fabrica_orcos = FabricaOrcos()
    
    simular_batalla(fabrica_humanos, fabrica_orcos)