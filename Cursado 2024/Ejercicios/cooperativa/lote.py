class Lote:
    def __init__(self, nombre, minerales):
        self.nombre = nombre
        self.minerales = set(minerales) 
        self.historial_siembra = [] 

    def agregar_siembra(self, tipo_cereal):
        self.historial_siembra.append(tipo_cereal)

    def puede_sembrar_pastura(self):
        return "Pastura" not in self.historial_siembra

    def __repr__(self):
        return f"Lote({self.nombre}, Minerales={self.minerales}, Historial={self.historial_siembra})"
