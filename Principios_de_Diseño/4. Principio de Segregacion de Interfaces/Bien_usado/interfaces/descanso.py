from abc import ABC, abstractmethod

class Descanso(ABC):
    @abstractmethod
    def tomar_descanso(self):
        pass
