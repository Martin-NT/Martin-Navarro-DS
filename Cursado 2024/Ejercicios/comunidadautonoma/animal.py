from especie import Especie


class Animal(Especie):
    def __init__(self, nombre_cientifico, nombre_vulgar, num_individuos, periodo_celo, alimentacion):
        super().__init__(nombre_cientifico, nombre_vulgar, num_individuos)
        self.periodo_celo = periodo_celo
        self.alimentacion = alimentacion  # Herbívoro, Carnívoro, Omnívoro
        self.alimentos = []  # Lista de alimentos (vegetales o animales)

    def agregar_alimento(self, alimento):
        self.alimentos.append(alimento)

    def __repr__(self):
        return super().__repr__() + f", Celo={self.periodo_celo}, Alimentación={self.alimentacion}, Alimentos={len(self.alimentos)}"
