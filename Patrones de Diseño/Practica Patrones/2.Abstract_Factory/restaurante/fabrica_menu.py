from abc import ABC, abstractmethod

class FabricaMenu(ABC):
    @abstractmethod
    def crear_comida(self):
        pass

    @abstractmethod
    def crear_bebida(self):
        pass