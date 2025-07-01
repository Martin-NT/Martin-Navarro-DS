class Pais:
    def __init__(self, nombre):
        self.nombre = nombre
        self.provincias = []  
        self.limita_con = []  


    def agregar_provincia(self, provincia):
        self.provincias.append(provincia)

    def agregar_frontera(self, pais):
        self.limita_con.append(pais)

    def __repr__(self):
        return f"Pais({self.nombre}, Provincias={len(self.provincias)})"