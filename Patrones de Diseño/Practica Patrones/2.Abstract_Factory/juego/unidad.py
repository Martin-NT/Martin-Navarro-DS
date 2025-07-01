from abc import ABC, abstractmethod

class Arquero(ABC):
    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def defender(self):
        pass

class Guerrero(ABC):
    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def defender(self):
        pass