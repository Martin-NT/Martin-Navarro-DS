class Representante:
    def __init__(self, nombre, direccion, telefono, fecha_nacimiento, cuit, fecha_ingreso):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.cuit = cuit
        self.fecha_ingreso = fecha_ingreso
        self.clientes = []  # Cartera de clientes
        self.ventas = []  # Lista de ventas realizadas

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def registrar_venta(self, venta):
        self.ventas.append(venta)

    def calcular_comision(self, porcentaje):
        total_ventas = sum(venta.precio for venta in self.ventas)
        return total_ventas * porcentaje / 100

    def __repr__(self):
        return f"Representante({self.nombre}, Ventas={len(self.ventas)})"
