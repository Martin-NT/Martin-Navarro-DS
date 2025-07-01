class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.platos_favoritos = {}  # Diccionario: {Restaurante: [Platos]}

    def agregar_plato_favorito(self, restaurante, plato):
        if restaurante not in self.platos_favoritos:
            self.platos_favoritos[restaurante] = []
        self.platos_favoritos[restaurante].append(plato)

    def __repr__(self):
        return f"Persona({self.nombre}, Platos Favoritos={(self.platos_favoritos)})"
