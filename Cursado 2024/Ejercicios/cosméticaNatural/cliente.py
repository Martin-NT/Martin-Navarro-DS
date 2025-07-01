class Cliente:
    def __init__(self, nombre, direccion, telefono, fecha_ingreso):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_ingreso = fecha_ingreso

    def __repr__(self):
        return f"Cliente({self.nombre}, Ingreso={self.fecha_ingreso})"
