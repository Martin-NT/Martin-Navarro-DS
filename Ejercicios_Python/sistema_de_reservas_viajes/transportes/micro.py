from interfaces.transporte import Transporte

class Micro(Transporte):
    def reservar(self, destino):
        print(f"--> Reservando Micro para {destino}")
    
    def calcular_costo(self, destino):
        print(f"--> Calculando costo de Micro para {destino}")
        print(f"--> Costo de Micro para {destino}: $1000")