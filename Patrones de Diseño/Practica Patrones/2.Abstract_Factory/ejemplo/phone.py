from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def get_type(self):
        pass
