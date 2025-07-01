class Area:
    def __init__(self, nombre, superficie):
        self.nombre = nombre
        self.superficie = superficie  # en km²
        self.especies = []  # Lista de especies en el área
        self.guardas = []  # Lista de guardas asignados al área

    def agregar_especie(self, especie):
        self.especies.append(especie)

    def agregar_guarda(self, guarda):
        self.guardas.append(guarda)

    def __repr__(self):
        return (f"Area({self.nombre}, Superficie={self.superficie} km², "
                f"Especies={len(self.especies)}, Guardas={len(self.guardas)})")
