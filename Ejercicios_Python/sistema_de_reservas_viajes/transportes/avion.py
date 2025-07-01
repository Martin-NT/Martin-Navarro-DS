from interfaces.transporte import Transporte

class Avion(Transporte):
    def reservar(self, destino):
        print(f"--> Reservando Avion para {destino}")

    def calcular_costo(self, destino):
        print(f"--> Calculando costo de Avion para {destino}")
        print(f"--> Costo de Avion para {destino}: $5000")