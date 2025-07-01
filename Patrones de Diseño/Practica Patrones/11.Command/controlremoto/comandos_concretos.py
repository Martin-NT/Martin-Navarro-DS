from comando import Comando

class ComandoEncenderTelevision(Comando):
    def __init__(self, television):
        self.television = television

    def ejecutar(self):
        self.television.ejecutar()

    def deshacer(self):
        self.television.deshacer()

class ComandoApagarTelevision(Comando):
    def __init__(self, television):
        self.television = television

    def ejecutar(self):
        self.television.deshacer()

    def deshacer(self):
        self.television.ejecutar()

class ComandoEncenderLampara(Comando):
    def __init__(self, lampara):
        self.lampara = lampara

    def ejecutar(self):
        self.lampara.ejecutar()

    def deshacer(self):
        self.lampara.deshacer()

class ComandoApagarLampara(Comando):
    def __init__(self, lampara):
        self.lampara = lampara

    def ejecutar(self):
        self.lampara.deshacer()

    def deshacer(self):
        self.lampara.ejecutar()

class ComandoEncenderSistemaSonido(Comando):
    def __init__(self, sistema_sonido):
        self.sistema_sonido = sistema_sonido

    def ejecutar(self):
        self.sistema_sonido.ejecutar()

    def deshacer(self):
        self.sistema_sonido.deshacer()

class ComandoApagarSistemaSonido(Comando):
    def __init__(self, sistema_sonido):
        self.sistema_sonido = sistema_sonido

    def ejecutar(self):
        self.sistema_sonido.deshacer()

    def deshacer(self):
        self.sistema_sonido.ejecutar()