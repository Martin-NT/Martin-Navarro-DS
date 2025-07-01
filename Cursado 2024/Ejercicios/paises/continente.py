class Continente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.paises = []  

    def agregar_pais(self, pais):
        self.paises.append(pais)

    def __repr__(self):
        return f"Continente({self.nombre}, Paises={len(self.paises)})"