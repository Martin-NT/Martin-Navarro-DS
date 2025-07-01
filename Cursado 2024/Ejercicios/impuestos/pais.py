class Pais:
    def __init__(self, nombre):
        self.nombre = nombre
        self.provincias = []

    def agregar_provincia(self, provincia):
        self.provincias.append(provincia)

    def ciudades_en_deficit(self):
        deficit = []
        for provincia in self.provincias:
            deficit.extend(provincia.ciudades_en_deficit())
        return deficit

    def provincias_afectadas(self):
        return [provincia for provincia in self.provincias if provincia.mas_de_mitad_en_deficit()]

    def __repr__(self):
        return f"Pais({self.nombre}, Provincias={len(self.provincias)})"
