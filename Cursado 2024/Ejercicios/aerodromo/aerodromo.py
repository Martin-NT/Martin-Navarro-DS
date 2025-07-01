class Aerodromo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hangares = []  

    def agregar_hangar(self, hangar):
        self.hangares.append(hangar)

    def __repr__(self):
        return f"Aerodromo({self.nombre}, Hangares={len(self.hangares)})"
