from procesador_pago import ProcesadorPago

class Criptomoneda(ProcesadorPago):
    def pagar(self, monto):
        print(f"--> Pagando ${monto} con Criptomonedas")