from cliente import Cliente
from detalle_factura import DetalleFactura

class Factura():
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.detalles = []
        
    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)
        
    def calcular_total(self):
        total = 0
        for detalle in self.detalles:
            total += detalle.calcular_subtotal()
        return total
    
    def mostrar_factura(self):
        print(f"\nFactura Nº: {self.numero}")
        print(f"Cliente: {self.cliente.nombre} - DNI: {self.cliente.dni}")
        print("Detalles:")
        for detalle in self.detalles:
            detalle.mostrar_detalle()
            print(f"Subtotal: ${detalle.calcular_subtotal()}")
        print(f"\nTotal: ${self.calcular_total()}")
