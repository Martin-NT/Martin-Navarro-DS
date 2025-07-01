from abc import ABC, abstractmethod

class Cereal(ABC):
    def __init__(self,nombre,requerimientos):
        self.nombre = nombre
        self.requerimientos = requerimientos

    @abstractmethod
    def cumple_requerimientos(self,lote):
        pass

class GranosGruesos(Cereal):
    def cumple_requerimientos(self, lote):
        return all(mineral in lote.minerales for mineral in self.requerimientos)
    
class GranosFinos(Cereal):
    def cumple_requerimientos(self, lote):
        return all(mineral in lote.minerales for mineral in self.requerimientos)
    
class Pasturas(Cereal):
    def cumple_requerimientos(self, lote):
        if any(isinstance(cereal,Pasturas) for cereal in lote.historial_siembra):
            return False
        return all(mineral in lote.minerales for mineral in self.requerimientos)