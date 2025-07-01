from compdeportivo import ComplejoDeportivo

class ComplejoUnicoDeporte(ComplejoDeportivo):
    def __init__(self, nombre, localizacion, jefe_organizacion, area_ocupada, deporte):
        super().__init__(nombre, localizacion, jefe_organizacion, area_ocupada)
        self.deporte = deporte

    def __repr__(self):
        return super().__repr__() + f", Deporte={self.deporte}"
