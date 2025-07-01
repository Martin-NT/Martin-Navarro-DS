class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.restaurantes = []  # Lista de restaurantes en la ciudad

    def agregar_restaurante(self, restaurante):
        self.restaurantes.append(restaurante)

    def __repr__(self):
        return f"Ciudad({self.nombre}, Restaurantes={len(self.restaurantes)})"
