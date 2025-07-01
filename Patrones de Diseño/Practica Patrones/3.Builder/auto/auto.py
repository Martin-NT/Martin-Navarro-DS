class Auto:
    def __init__(self):
        self.cant_puertas = None
        self.modelo = None
        self.marca = None
        self.motor = None

    def  __str__(self):
        return f"Modelo: {self.modelo}, Marca: {self.marca}, Motor: {self.motor}, Puertas: {self.cant_puertas}"
