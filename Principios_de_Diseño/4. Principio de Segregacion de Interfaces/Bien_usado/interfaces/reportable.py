from abc import ABC, abstractmethod

class Reportable(ABC):
    @abstractmethod
    def reportar_horas(self):
        pass
