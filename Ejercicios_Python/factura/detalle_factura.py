
class DetalleFactura:
    def __init__(self, producto, cantidad, precio_unitario):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
    
    def mostrar_detalle(self):
        print(f"\n- Producto: {self.producto}")
        print(f"- Cantidad: {self.cantidad}")
        print(f"- Precio unitario:  ${self.precio_unitario}")
        
    def calcular_subtotal(self):
        subtotal = self.cantidad * self.precio_unitario
        return subtotal