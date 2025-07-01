from persona import Persona 

class Administrador(Persona):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
        self.rol = "Administrador" #Si siempre sera administrador
        #Si quiero que sea dinamico es self.rol = rol (como nombre y dni)
        
    def get_datos(self):
        super().get_datos()
        print(f"Rol: {self.rol}")