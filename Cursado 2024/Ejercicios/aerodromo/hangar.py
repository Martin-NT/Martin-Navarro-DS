class Hangar:
    def __init__(self, numero, capacidad, ubicacion):
        self.numero = numero
        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.aviones = []  
    def agregar_avion(self, avion):
        if len(self.aviones) < self.capacidad:
            self.aviones.append(avion)
        else:
            raise ValueError("Hangar lleno.")

    def __repr__(self):
        return f"Hangar({self.numero}, Ubicación={self.ubicacion}, Aviones={len(self.aviones)})"
