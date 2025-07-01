from elemento_menu import ElementoMenu

class Combo(ElementoMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar_elemento(self, elemento):
        if isinstance(elemento, ElementoMenu):
            self.elementos.append(elemento)
        else:
            raise TypeError("--> Solo se pueden agregar elementos de tipo ElementoMenu.")
    
    def mostrar_detalles(self):
        print(f"{self.nombre}")
        for elemento in self.elementos:
            elemento.mostrar_detalles()
        print((f"\n--> Total del '{self.nombre}': ${self.calcular_total()}"))

    def obtener_precio(self):
        return self.calcular_total()
    
    def calcular_total(self):
        return sum([elemento.obtener_precio() for elemento in self.elementos])