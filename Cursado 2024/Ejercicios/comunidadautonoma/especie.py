class Especie:
    def __init__(self, nombre_cientifico, nombre_vulgar, num_individuos):
        self.nombre_cientifico = nombre_cientifico
        self.nombre_vulgar = nombre_vulgar
        self.num_individuos = num_individuos

    def __repr__(self):
        return f"Especie({self.nombre_vulgar}, Científico={self.nombre_cientifico}, Individuos={self.num_individuos})"
