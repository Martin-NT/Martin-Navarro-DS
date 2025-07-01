# computadora_builder.py
from computadora import Computadora
from builder import Builder

# ConcreteBuilder: Implementación concreta de los métodos de construcción
class ComputadoraBuilder(Builder):
    def __init__(self):
        self.computadora = Computadora()

    def set_cpu(self, cpu):
        self.computadora.cpu = cpu

    def set_memoria(self, memoria):
        self.computadora.memoria = memoria

    def set_discos(self, discos):
        self.computadora.discos = discos

    def set_teclado(self, teclado):
        self.computadora.teclado = teclado

    def set_marca(self, marca):
        self.computadora.marca = marca

    def build(self):
        computadora_final = self.computadora
        self.computadora = Computadora()  # Reiniciar para una nueva construcción
        return computadora_final
