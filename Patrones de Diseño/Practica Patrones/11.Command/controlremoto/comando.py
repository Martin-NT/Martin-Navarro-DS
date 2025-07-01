from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def deshacer(self):
        pass