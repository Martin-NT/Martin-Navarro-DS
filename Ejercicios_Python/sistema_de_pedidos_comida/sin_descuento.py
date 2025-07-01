from estrategia_descuento import EstrategiaDescuento

class SinDescuento(EstrategiaDescuento):
    def calcular_total(self, productos):
        total = sum(producto.obtener_precio() for producto in productos)
        print("--> Calculando total sin descuento")
        print (f"--> Total sin descuento: ${total}")
        return total
