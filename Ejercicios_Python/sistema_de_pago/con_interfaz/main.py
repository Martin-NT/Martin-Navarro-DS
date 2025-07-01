from servicio_de_cobro import ServicioDeCobro
from metodos.tarjeta_credito import TarjetaCredito
from metodos.mercado_pago import MercadoPago
from metodos.criptomoneda import Criptomoneda

# (acá puedo agregar funciones o clases auxiliares)

if __name__ == "__main__":
    servicio = ServicioDeCobro()
        
    tarjeta = TarjetaCredito()
    mercado = MercadoPago()
    cripto = Criptomoneda()

    print("=== Ejecución de pagos ===")
    servicio.realizar_pago(1000, tarjeta)
    servicio.realizar_pago(750, mercado)
    servicio.realizar_pago(5000, cripto)
