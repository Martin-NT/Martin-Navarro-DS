#En lugar de forzar a Cuadrado a heredar de Rectangulo, creamos una interfaz común Forma.
from abc import ABC, abstractmethod

# 1️⃣ Definimos una clase base abstracta
class Forma(ABC): #Forma es una interfaz común para todas las figuras geométricas.
    @abstractmethod #@abstractmethod obliga a las subclases a implementar su propio método area().
    def area(self): #Esto garantiza que todas las formas tendrán una implementación del área.
        pass  # Obliga a las subclases a definir `area()`

# 2️⃣ Definimos `Rectangulo` sin relación con `Cuadrado`
class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return f"Rectángulo: {self.base * self.altura}"

# 3️⃣ Definimos `Cuadrado` por separado
class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return f"Cuadrado: {self.lado * self.lado}"

# 🔥 Prueba
def print_area(figura: Forma):  # Espera una instancia de `Forma`
    print(f"Área del {figura.area()}")

rect = Rectangulo(4, 5)
print_area(rect)  # ✅ Área del Rectángulo: 20

cuadrado = Cuadrado(4)  # No sobrescribimos la clase Cuadrado
print_area(cuadrado)  # ✅ Área del Cuadrado: 16

# ✔️ print_area() recibe una Forma, pero no necesita saber si es un Rectangulo o un Cuadrado.
# ✔️ Llamamos a figura.area() y cada subclase responde según su propia implementación.
# ✔️ Podemos sustituir Rectangulo por Cuadrado sin errores ni cambios inesperados.

#🎯 ¿Por qué el código corregido cumple con LSP?
# ✅ Rectangulo y Cuadrado son entidades independientes, sin modificar comportamientos esperados.
# ✅ Forma garantiza que todas las subclases tengan un método area() sin afectar el programa.
# ✅ Podemos intercambiar Rectangulo y Cuadrado sin que print_area() falle o tenga lógica incorrecta.

#🚀 Conclusión
# ✔️ Las subclases pueden reemplazar la clase base sin causar errores.
# ✔️ No modificamos el comportamiento de Rectangulo de forma inesperada.
# ✔️ El código sigue siendo flexible y fácil de extender sin romper nada.