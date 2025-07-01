class Venta:
    def __init__(self, fecha, producto, precio, cliente):
        self.fecha = fecha
        self.producto = producto
        self.precio = precio
        self.cliente = cliente

    def __repr__(self):
        return f"Venta(Fecha={self.fecha}, Producto={self.producto.nombre}, Precio={self.precio}, Cliente={self.cliente.nombre})"
