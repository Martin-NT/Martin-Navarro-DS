from abc import ABC, abstractmethod

class ElementoMenu(ABC):
    @abstractmethod
    def mostrar_detalles(self):
        pass

    @abstractmethod
    def obtener_precio(self):    
        pass