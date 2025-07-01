from transporte_factory import TransporteFactory
from avion import Avion

class AvionFactory(TransporteFactory):
    def crear(self):    
        return Avion()