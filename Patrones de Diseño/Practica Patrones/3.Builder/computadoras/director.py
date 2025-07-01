# director.py
from computadora_builder import ComputadoraBuilder

class Director:
    def __init__(self, builder: ComputadoraBuilder):
        self.builder = builder

    def construir_computadora(self):
        # Aquí se definen los pasos para construir una computadora completa
        self.builder.set_cpu(4)
        self.builder.set_memoria(16)
        self.builder.set_discos(1)
        self.builder.set_teclado(True)
        self.builder.set_marca("Dell")
        return self.builder.build()
