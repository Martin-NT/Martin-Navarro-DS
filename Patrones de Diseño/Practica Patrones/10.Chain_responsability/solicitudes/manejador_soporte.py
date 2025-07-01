
from abc import ABC, abstractmethod

class ManejadorSoporte(ABC):
    def __init__(self):
        self.siguiente_manejador = None

    def set_siguiente(self,manejador):
        self.siguiente_manejador = manejador

    @abstractmethod
    def manejar_solicitud(self,complejidad):
        pass