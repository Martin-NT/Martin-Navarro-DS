from representante import Representante


class Lider(Representante):
    def __init__(self, nombre, direccion, telefono, fecha_nacimiento, cuit, fecha_ingreso, fecha_promocion):
        super().__init__(nombre, direccion, telefono, fecha_nacimiento, cuit, fecha_ingreso)
        self.fecha_promocion = fecha_promocion
        self.equipo = []  # Equipo de vendedores

    def agregar_vendedor(self, vendedor):
        self.equipo.append(vendedor)

    def calcular_comision(self, porcentaje):
        # Comisión propia más la de su equipo
        comision_propia = super().calcular_comision(porcentaje)
        comision_equipo = sum(vendedor.calcular_comision(porcentaje) for vendedor in self.equipo)
        return comision_propia + comision_equipo

    def __repr__(self):
        return super().__repr__() + f", Equipo={len(self.equipo)}"
