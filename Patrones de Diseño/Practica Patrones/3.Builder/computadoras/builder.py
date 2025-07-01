# builder.py
from abc import ABC, abstractmethod

# Builder: Define los métodos para configurar un producto
class Builder(ABC):
    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def set_memoria(self, memoria):
        pass

    @abstractmethod
    def set_discos(self, discos):
        pass

    @abstractmethod
    def set_teclado(self, teclado):
        pass

    @abstractmethod
    def set_marca(self, marca):
        pass

    @abstractmethod
    def build(self):
        pass
