class Provincia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ciudades = []

    def agregar_ciudad(self, ciudad):
        self.ciudades.append(ciudad)

    def ciudades_en_deficit(self):
        return [ciudad for ciudad in self.ciudades if ciudad.esta_en_deficit()]

    def mas_de_mitad_en_deficit(self):
        return len(self.ciudades_en_deficit()) > len(self.ciudades) / 2

    def __repr__(self):
        return f"Provincia({self.nombre}, Ciudades={len(self.ciudades)})"
