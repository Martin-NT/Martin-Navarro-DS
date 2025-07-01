class ComunidadAutonoma:
    def __init__(self, nombre, organismo_responsable):
        self.nombre = nombre
        self.organismo_responsable = organismo_responsable
        self.parques = []  # Lista de parques gestionados por esta CA

    def agregar_parque(self, parque):
        self.parques.append(parque)

    def __repr__(self):
        return f"ComunidadAutonoma({self.nombre}, Parques={len(self.parques)})"
