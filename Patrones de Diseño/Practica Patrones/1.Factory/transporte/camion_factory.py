from transporte_factory import TransporteFactory
from camion import Camion

class CamionFactory(TransporteFactory):
    def __init__(self,tipo):
        self.tipo = tipo    

    def crear(self):
        return Camion(self.tipo)