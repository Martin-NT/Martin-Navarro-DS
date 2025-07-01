from abc import ABC, abstractmethod

class Triangulo(ABC):
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_superficie(self):
        pass