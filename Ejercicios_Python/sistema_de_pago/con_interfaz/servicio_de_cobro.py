from procesador_pago import ProcesadorPago

class ServicioDeCobro:
    def realizar_pago(self, monto, metodo_pago: ProcesadorPago):
        metodo_pago.pagar(monto)
