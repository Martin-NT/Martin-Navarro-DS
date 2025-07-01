from cliente import Cliente
from administrador import Administrador
from factura import Factura
from detalle_factura import DetalleFactura

def mostrar_encabezado(texto: str):
    print("\n" + "=" * 40)
    print(f"{texto.upper():^40}")
    print("=" * 40)

def main():
    # Crear administrador
    admin = Administrador("Martin Navarro", "45141159")

    # Crear cliente
    cliente = Cliente("Martina Rizzotti", "45379157", "martina@email.com")

    # Crear factura asociada al cliente
    factura = Factura(numero=1001, cliente=cliente)

    # Crear y agregar detalles
    detalles = [
        DetalleFactura("Monitor", 2, 100000),
        DetalleFactura("Mouse", 1, 5000),
        DetalleFactura("Teclado", 1, 8000)
    ]

    for detalle in detalles:
        factura.agregar_detalle(detalle)

    # Mostrar datos del administrador
    mostrar_encabezado("Administrador que genera la factura")
    admin.get_datos()

    # Mostrar datos del cliente
    mostrar_encabezado("Datos del Cliente")
    cliente.get_datos()

    # Mostrar detalles de factura
    mostrar_encabezado(f"Datos de Facturas")
    factura.mostrar_factura()


if __name__ == "__main__":
    main()
