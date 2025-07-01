from abc import ABC, abstractmethod

class Charger(ABC):
    @abstractmethod
    def get_type(self):
        pass
