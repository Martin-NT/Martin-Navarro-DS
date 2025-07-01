from auto_builder import AutoBuilder
from motor import Motor

class FordBuilder(AutoBuilder):
    def buid_marca(self):
        self.auto.marca = "Ford"

    def buid_modelo(self):
        self.auto.modelo = "Mustang"

    def buid_motor(self):
        self.auto.motor = Motor("V8", 250)

    def build_puertas(self):
        self.auto.cant_puertas = 5