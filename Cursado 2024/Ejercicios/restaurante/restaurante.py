class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = []  # Lista de platos servidos

    def agregar_plato(self, plato):
        if len(self.menu) < 20:
            self.menu.append(plato)
        else:
            raise ValueError("El menú no puede tener más de 20 platos")

    def __repr__(self):
        return f"Restaurante({self.nombre}, Platos={len(self.menu)})"
