from procesador_pago import ProcesadorPago

class MercadoPago(ProcesadorPago):
    def pagar(self, monto):
        print(f"--> Pagando ${monto} con Mercado Pago")