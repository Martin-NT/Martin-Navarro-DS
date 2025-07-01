from procesador_pago import ProcesadorPago
from metodos.tarjeta_credito import TarjetaCredito
from metodos.mercado_pago import MercadoPago

if __name__ == "__main__":
    procesador = ProcesadorPago()
    
    print("Ejemplos de uso:")
    tarjeta = TarjetaCredito()
    procesador.realizar_pago(tarjeta)

    mercadopago = MercadoPago()
    procesador.procesador_pago(mercadopago)
