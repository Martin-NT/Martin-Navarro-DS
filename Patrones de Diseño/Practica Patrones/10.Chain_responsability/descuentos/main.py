from cliente_fiel import DescuentoClienteFiel
from temporada import DescuentoTemporada
from por_volumen import DescuentoPorVolumen

def main():
    descuento_temporada = DescuentoTemporada()
    descuento_cliente_fiel = DescuentoClienteFiel()
    descuento_por_volumen = DescuentoPorVolumen()

    # Configurar la cadena de responsabilidad
    descuento_temporada.set_siguiente(descuento_cliente_fiel)
    descuento_cliente_fiel.set_siguiente(descuento_por_volumen)

    # Monto inicial de la compra
    monto_inicial = 150.00
    print(f"Monto inicial: ${monto_inicial:.2f}")

    # Aplicar la cadena de descuentos
    monto_final = descuento_temporada.aplicar_descuento(monto_inicial)
    print(f"Monto final: ${monto_final:}")

if __name__ == "__main__":
    main()