from unidad import Guerrero

class GuerreroHumano(Guerrero):
    def atacar(self):
        print("Guerrero humano ataca")

    def defender(self):
        print("El guerrero humano defiende")

class GuerreroOrco(Guerrero):
    def atacar(self):
        print("Guerrero orco ataca")

    def defender(self):
        print("El guerrero orco defiende")