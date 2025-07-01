from especie import Especie


class Vegetal(Especie):
    def __init__(self, nombre_cientifico, nombre_vulgar, num_individuos, floracion, periodo_floracion=None):
        super().__init__(nombre_cientifico, nombre_vulgar, num_individuos)
        self.floracion = floracion
        self.periodo_floracion = periodo_floracion if floracion else None

    def __repr__(self):
        return super().__repr__() + f", Floración={self.floracion}, Periodo={self.periodo_floracion}"
