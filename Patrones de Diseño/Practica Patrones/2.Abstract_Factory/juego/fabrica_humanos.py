from fabrica_unidades import FabricaUnidades
from arquero import ArqueroHumano
from guerrero import GuerreroHumano

class FabricaHumanos(FabricaUnidades):
    def crear_arquero(self):
        return ArqueroHumano()

    def crear_guerrero(self):
        return GuerreroHumano()