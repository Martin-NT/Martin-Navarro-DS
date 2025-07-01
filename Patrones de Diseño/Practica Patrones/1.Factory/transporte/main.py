from camion_factory import CamionFactory
from avion_factory import AvionFactory
from barco_factory import BarcoFactory

def simular_entrega(factory):
    transporte = factory.crear()
    transporte.entregar()

if __name__ == "__main__":
    factories = [
        CamionFactory(tipo=" de pasajeros"),
        AvionFactory(),
        BarcoFactory()
    ]

    for factory in factories:
        simular_entrega(factory)
        print("-" * 80)  
