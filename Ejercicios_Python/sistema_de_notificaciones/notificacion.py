from abc import ABC, abstractmethod
#Interfaz
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje, destinatario):
        pass