from abc import ABC, abstractmethod

class ManejadorDescuentos(ABC):
    def __init__(self):
        self.siguiente_manejador = None

    def set_siguiente(self,manejador):
        self.siguiente_manejador = manejador

    @abstractmethod
    def aplicar_descuento(self,precio):
        pass