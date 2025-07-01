from producto import Producto

class Comida(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        
    def obtener_precio(self):
        return self.precio