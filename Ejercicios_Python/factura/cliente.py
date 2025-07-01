from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, dni, email):
        super().__init__(nombre, dni) #sirve para llamar al constructor de la clase padrE.
        self.email = email
        
    def get_datos(self):
        super().get_datos()
        print(f"Email: {self.email}")   