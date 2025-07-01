class Provincia:
    def __init__(self, nombre, capital=False):
        self.nombre = nombre
        self.ciudades = []  
        self.limita_con = []
        self.capital = capital  

    def agregar_ciudad(self, ciudad):
        self.ciudades.append(ciudad)

    def agregar_frontera(self, limite):
        self.limita_con.append(limite)

    def __repr__(self):
        return f"Provincia({self.nombre}, Ciudades={len(self.ciudades)})"
