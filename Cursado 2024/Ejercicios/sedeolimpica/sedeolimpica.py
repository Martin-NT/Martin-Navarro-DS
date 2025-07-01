class SedeOlimpica:
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.complejos = []  

    def agregar_complejo(self, complejo):
        self.complejos.append(complejo)

    def __repr__(self):
        return f"SedeOlimpica({self.nombre}, Complejos={len(self.complejos)}, Presupuesto={self.presupuesto})"
