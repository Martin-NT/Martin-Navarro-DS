from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass
