class ComplejoDeportivo:
    def __init__(self, nombre, localizacion, jefe_organizacion, area_ocupada):
        self.nombre = nombre
        self.localizacion = localizacion
        self.jefe_organizacion = jefe_organizacion
        self.area_ocupada = area_ocupada
        self.eventos = [] 

    def agregar_evento(self, evento):
        self.eventos.append(evento)

    def __repr__(self):
        return f"ComplejoDeportivo({self.nombre}, Localización={self.localizacion}, Eventos={len(self.eventos)})"
