from auto_builder import AutoBuilder
from motor import Motor

class FiatBuilder(AutoBuilder):
    def buid_marca(self):
        self.auto.marca = "Fiat"

    def buid_modelo(self):
        self.auto.modelo = "500"

    def buid_motor(self):
        self.auto.motor = Motor("V6", 200)

    def build_puertas(self):
        self.auto.cant_puertas = 4      
        