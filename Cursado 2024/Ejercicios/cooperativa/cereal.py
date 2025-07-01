class Cereal:
    def __init__(self, nombre, tipo, minerales_requeridos):
        self.nombre = nombre
        self.tipo = tipo  
        self.minerales_requeridos = set(minerales_requeridos)

    def __repr__(self):
        return f"Cereal({self.nombre}, Tipo={self.tipo}, Minerales Requeridos={self.minerales_requeridos})"
