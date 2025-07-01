from transporte_factory import TransporteFactory
from barco import Barco

class BarcoFactory(TransporteFactory):
    def crear(self):
        return Barco()