class Artista:
    def __init__(self, nombre, fecha_nacimiento, fecha_defuncion, pais_origen, estilo_principal):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_defuncion = fecha_defuncion
        self.pais_origen = pais_origen
        self.estilo_principal = estilo_principal

    def __repr__(self):
        return f"Artista({self.nombre}, Estilo={self.estilo_principal})"
