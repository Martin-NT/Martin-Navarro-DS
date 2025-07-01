from lote import Lote

class Cooperativa:
    def __init__(self,nombre):
        self.nombre = nombre
        self.lotes = []

    def agregar_lote(self,lote):
        self.lotes.append(lote)

    def sugerir_cereal(self,lote,cereales):
        for cereal in cereales:
            if lote.satisface_requerimientos(cereal):
                return cereal
        return None