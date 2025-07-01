from transporte import Transporte

class Camion(Transporte):
    def __init__(self, tipo):
        self.tipo = tipo

    def entregar(self):
        print(f"\n--> Entregando por carretera con un camion{self.tipo}")