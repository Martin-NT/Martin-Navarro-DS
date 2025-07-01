from comando import Comando

class Television(Comando):
    def ejecutar(self):
        print("Ejecutando el comando de televisor")

    def deshacer(self):
        print("Deshaciendo el comando de televisor")
    
class Lampara(Comando):
    def ejecutar(self):
        print("Ejecutando el comando de lampara")

    def deshacer(self): 
        print("Deshaciendo el comando de lampara")

class SistemaSonido(Comando):
    def ejecutar(self):
        print("Ejecutando el comando de sistema sonido")

    def deshacer(self):
        print("Deshaciendo el comando de sistema sonido")