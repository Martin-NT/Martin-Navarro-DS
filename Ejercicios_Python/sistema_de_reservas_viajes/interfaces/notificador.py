from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensaje, destinatario):
        pass