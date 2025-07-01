class Avion:
    def __init__(self, matricula, fecha_adquisicion, modelo, capacidad, peso ):
        self.matricula = matricula
        self.fecha_adquisicion = fecha_adquisicion
        self.modelo = modelo
        self.capacidad = capacidad
        self.peso = peso
    

    def __repr__(self):
        return f"Avion({self.matricula}, Modelo={self.modelo}, Capacidad={self.capacidad}, Peso={self.peso})"
