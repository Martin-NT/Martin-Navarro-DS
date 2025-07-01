from abc import ABC, abstractmethod
# Interfaz
class EstadoReproductor(ABC):
    @abstractmethod
    def reproducir(self, reproductor):
        pass

    @abstractmethod
    def pausar(self, reproductor):
        pass

    @abstractmethod
    def detener(self, reproductor):
        pass
    
    @abstractmethod
    def avanzar_cancion(self):
        pass

    @abstractmethod
    def retroceder_cancion(self):
        pass