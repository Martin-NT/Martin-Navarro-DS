from abc import ABC, abstractmethod
#Clase Abstracta
class Persona(ABC):
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        
    def get_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.dni}")