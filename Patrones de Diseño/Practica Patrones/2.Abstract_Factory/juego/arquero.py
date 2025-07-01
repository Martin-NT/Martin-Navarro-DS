from unidad import Arquero

class ArqueroHumano(Arquero):
    def atacar(self):
        print("Arquero humano ataca")

    def defender(self):
        print("El arquero humano defiende")

class ArqueroOrco(Arquero):
    def atacar(self):
        print("Arquero orco ataca")

    def defender(self):        
        print("El arquero orco defiende")           