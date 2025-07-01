class Ciudad:
    def __init__(self, nombre, poblacion, capital=False):
        self.nombre = nombre
        self.poblacion = poblacion
        self.capital = capital

    def __repr__(self):
        return f"Ciudad({self.nombre}, Poblacion={self.poblacion})"
