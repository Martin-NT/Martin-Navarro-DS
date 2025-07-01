from rectangulo import Rectangulo
from cuadrado import Cuadrado

def print_area(figura: Rectangulo):  # Espera un Rectángulo
    print(f"Área del rectángulo: {figura.area()}")

# Prueba con un rectángulo normal
rect = Rectangulo(4, 5)
print_area(rect)  # ✅ Área del rectángulo: 20

# Prueba con un cuadrado
cuadrado = Cuadrado(4)  # Ahora Cuadrado debería funcionar bien, pero al heredar de Rectángulo, cambia su lógica
print_area(cuadrado)  # 🚨 Área del rectángulo: 16, lo cual es incorrecto ya que se esperaba un comportamiento de rectángulo
