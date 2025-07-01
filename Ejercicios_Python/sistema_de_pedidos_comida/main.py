from pedido import Pedido
from comida import Comida
from bebida import Bebida
from sin_descuento import SinDescuento
from descuento_porcentaje import DescuentoPorcentaje

def separador():
    print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    print("\n=== 📋 Inicio del sistema de pedidos de comida ===\n")
    print("🧾 Pedido 1: Sin descuento")
    pedido1 = Pedido(SinDescuento())
    pedido1.agregar_producto(Comida("🍕 Pizza", 2000))
    pedido1.agregar_producto(Bebida("🥤 Gaseosa", 800))
    total1 = pedido1.calcular_total()

    separador()

    print("🧾 Pedido 2: Con 10% de descuento")
    pedido2 = Pedido(DescuentoPorcentaje(10))
    pedido2.agregar_producto(Comida("🍔 Hamburguesa", 2500))
    pedido2.agregar_producto(Bebida("💧 Agua", 600))
    total2 = pedido2.calcular_total()
