class Ciudad:
    def __init__(self, nombre, imp1, imp2, imp3, imp4, imp5, gastos):
        self.nombre = nombre
        self.ingresos = imp1 + imp2 + imp3 + imp4 + imp5
        self.gastos = gastos

    def esta_en_deficit(self):
        return self.gastos > self.ingresos

    def __repr__(self):
        estado = "Déficit" if self.esta_en_deficit() else "Superávit"
        return f"Ciudad({self.nombre}, Ingresos={self.ingresos}, Gastos={self.gastos}, Estado={estado})"
