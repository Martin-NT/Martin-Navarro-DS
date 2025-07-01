from abc import ABC, abstractmethod

#Clase Abstracta
class Producto(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def obtener_nombre(self):
        return self.nombre

    @abstractmethod
    def obtener_precio(self):
        pass
