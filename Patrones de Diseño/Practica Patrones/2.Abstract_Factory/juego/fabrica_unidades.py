from abc import ABC, abstractmethod

class FabricaUnidades(ABC):
    @abstractmethod
    def crear_arquero(self):
        pass

    @abstractmethod
    def crear_guerrero(self):
        pass