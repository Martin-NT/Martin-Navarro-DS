class Lote:
    def __init__(self, id,tipo,minerales):
        self.id = id
        self.tipo = tipo
        self.minerales = minerales
        self.historial_siembra = []

    def satisface_requerimientos(self,cereal):
        return cereal.cumple_requerimientos(self)