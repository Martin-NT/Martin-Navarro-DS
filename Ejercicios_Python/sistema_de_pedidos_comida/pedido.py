from estrategia_descuento import EstrategiaDescuento

class Pedido():
    def __init__(self, estrategia_descuento: EstrategiaDescuento):
        self.productos  = []
        self.estrategia_descuento = estrategia_descuento
        
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"--> Agregando {producto.obtener_nombre()} al pedido")
        
    def calcular_total(self):
        return self.estrategia_descuento.calcular_total(self.productos)
