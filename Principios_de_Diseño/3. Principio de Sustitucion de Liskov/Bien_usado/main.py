from rectangulo import Rectangulo
from cuadrado import Cuadrado

def print_area(figura):
    print(f"Área del {figura.nombre}: {figura.area()}")

# Prueba con un rectángulo
rect = Rectangulo(4, 5)
print_area(rect)  # Área del Rectángulo: 20

# Prueba con un cuadrado
cuad = Cuadrado(4)
print_area(cuad)  # Área del Cuadrado: 16
