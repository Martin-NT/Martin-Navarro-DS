from interfaces.transporte import Transporte

class Tren(Transporte):
    def reservar(self, destino):
        print(f"--> Reservando Tren para {destino}")

    def calcular_costo(self, destino):
        print(f"--> Calculando costo de Tren para {destino}")
        print(f"--> Costo de Tren para {destino}: $2000")