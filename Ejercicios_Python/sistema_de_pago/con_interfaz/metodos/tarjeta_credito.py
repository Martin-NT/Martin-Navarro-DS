from procesador_pago import ProcesadorPago

class TarjetaCredito(ProcesadorPago):
    def pagar(self, monto):
        print(f"--> Pagando ${monto} con Tarjeta de Crédito")