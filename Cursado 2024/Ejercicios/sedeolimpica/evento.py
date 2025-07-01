class Evento:
    def __init__(self, nombre, tipo, fecha, duracion, participantes, cant_comisarios, materiales):
        self.nombre = nombre
        self.tipo = tipo
        self.fecha = fecha
        self.duracion = duracion
        self.participantes = participantes
        self.cant_comisarios = cant_comisarios 
        self.materiales = materiales  

        
    def __repr__(self):
        return f"Evento({self.nombre}, Tipo={self.tipo}, Fecha={self.fecha}, Participantes={self.participantes})"
