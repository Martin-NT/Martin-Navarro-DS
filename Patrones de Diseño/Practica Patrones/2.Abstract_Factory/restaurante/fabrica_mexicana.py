from fabrica_menu import FabricaMenu
from taco import Taco
from tequila import Tequila

class FabricaMexicana(FabricaMenu):
    def crear_comida(self):
        return Taco()

    def crear_bebida(self):    
        return Tequila()