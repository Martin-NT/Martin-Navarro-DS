from estrategia_descuento import EstrategiaDescuento

class DescuentoPorcentaje(EstrategiaDescuento):
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    def calcular_total(self, productos):
        total_sin_descuento = sum(producto.obtener_precio() for producto in productos)
        descuento = total_sin_descuento * (self.porcentaje / 100)
        total_con_descuento = total_sin_descuento - descuento
        print("--> Calculando total con descuento")
        print (f"--> Total con descuento: ${total_con_descuento}")
        return total_con_descuento
        