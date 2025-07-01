import copy
from abc import ABC, abstractmethod

#Prototype (interfaz)
class RecursoPrototype(ABC):
    @abstractmethod
    def clonar(self):
        pass

#ConcretePrototype
class RecursoDigital(RecursoPrototype):
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

    def clonar(self):
        return copy.deepcopy(self)

    def mostrar(self):
        print(f"{self.__class__.__name__}: '{self.titulo}' de {self.autor} [{self.categoria}]")

#SubclassPrototype (otra variante de recurso)
class Libro(RecursoDigital):
    def __init__(self, titulo, autor, categoria, paginas):
        super().__init__(titulo, autor, categoria)
        self.paginas = paginas

    def mostrar(self):
        print(f"{self.__class__.__name__}: '{self.titulo}' de {self.autor} [{self.categoria}] - {self.paginas} páginas")

class Revista(RecursoDigital):
    def __init__(self, titulo, autor, categoria, numero_edicion):
        super().__init__(titulo, autor, categoria)
        self.numero_edicion = numero_edicion

    def mostrar(self):
        print(f"{self.__class__.__name__}: '{self.titulo}' - Edición {self.numero_edicion} [{self.categoria}]")

# === Cliente ===
def cliente():
    print("Creando recursos originales...")
    libro_original = Libro("Python Avanzado", "Ana Torres", "Programación", 320)
    revista_original = Revista("Tech Today", "Carlos Ruiz", "Tecnología", 42)

    libro_original.mostrar()
    revista_original.mostrar()

    print("\nClonando recursos...")
    libro_clon = libro_original.clonar()
    libro_clon.titulo = "Python Intermedio"
    libro_clon.paginas = 280

    revista_clon = revista_original.clonar()
    revista_clon.numero_edicion = 43

    libro_clon.mostrar()
    revista_clon.mostrar()

# === Ejecutar cliente ===
if __name__ == "__main__":
    cliente()
