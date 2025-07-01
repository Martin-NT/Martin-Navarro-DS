from fabrica_menu import FabricaMenu
from pasta import Pasta
from cerveza import Cerveza

class FabricaItaliana(FabricaMenu):
    def crear_comida(self):
        return Pasta()

    def crear_bebida(self):
        return Cerveza()