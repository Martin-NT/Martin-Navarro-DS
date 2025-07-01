class Comisario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.eventos_asignados = []  
        
    def asignar_evento(self, evento):
        self.eventos_asignados.append(evento)

    def __repr__(self):
        return f"Comisario({self.nombre}, Eventos Asignados={len(self.eventos_asignados)})"
