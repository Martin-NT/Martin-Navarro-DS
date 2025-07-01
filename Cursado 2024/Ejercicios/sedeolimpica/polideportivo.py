from compdeportivo import ComplejoDeportivo

class Polideportivo(ComplejoDeportivo):
    def __init__(self, nombre, localizacion, jefe_organizacion, area_ocupada, deportes):
        super().__init__(nombre, localizacion, jefe_organizacion, area_ocupada)
        self.deportes = deportes

 
    def __repr__(self):
        return super().__repr__() + f", Deportes={len(self.deportes)} , {self.deportes}"
