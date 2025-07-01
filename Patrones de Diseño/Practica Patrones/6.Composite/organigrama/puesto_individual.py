from posicion import Posicion

class PuestoIndividual(Posicion):
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto
    
    def mostrar_informacion(self,nivel=0):
        espacio = ' ' * (nivel * 2)
        print(f"{espacio}Puesto: {self.nombre} - Presupuesto: ${self.presupuesto:.2f}")

    def calcular_presupuesto(self):
        return self.presupuesto