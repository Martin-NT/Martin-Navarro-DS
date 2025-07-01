from fabrica_unidades import FabricaUnidades
from arquero import ArqueroOrco
from guerrero import GuerreroOrco

class FabricaOrcos(FabricaUnidades):
    def crear_arquero(self):
        return ArqueroOrco()

    def crear_guerrero(self):        
        return GuerreroOrco()