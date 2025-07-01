from posicion import Posicion

class Depto(Posicion):
    def __init__(self, nombre):
        self.nombre = nombre
        self.posiciones = []
        
    def agregar_posicion(self, posicion):
        if isinstance(posicion, Posicion):
            self.posiciones.append(posicion)
        else:
            raise TypeError("Solo se pueden agregar posiciones de tipo Posicion.")

    def mostrar_informacion(self, nivel=0):
        espacio = ' ' * (nivel * 2)
        print(f"{espacio}Departamento: {self.nombre}")
        for posicion in self.posiciones:
            posicion.mostrar_informacion(nivel + 1)

    def calcular_presupuesto(self):
        presupuesto_total = sum([posicion.calcular_presupuesto() for posicion in self.posiciones])
        return presupuesto_total